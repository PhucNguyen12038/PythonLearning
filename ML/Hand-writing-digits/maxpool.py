import numpy as np

class MaxPool():
    def im_regions(self,image):
        h,w,_ = image.shape
        new_h = h // 2
        new_w = w // 2
        for i in range(new_h):
            for j in range(new_w):
                im_region = image[(i*2):(i*2+2),(j*2):(j*2+2)]
                yield im_region,i,j
        
    def forward(self,inputs):
        self.last_inputs = inputs
        h,w,number_of_filter = inputs.shape
        new_h = h // 2
        new_w = w // 2
        output = np.zeros((new_h,new_w,number_of_filter))
        for im_region,i,j in self.im_regions(inputs):
            output[i,j] = np.amax(im_region,axis=(0,1))
        return output
    
    def backpropagate(self,d_L_d_outs):
        # d_L_d_outs is H/2 x W/2 x N
        d_L_d_inputs = np.zeros(self.last_inputs.shape)
        
        for im_region,i,j in self.im_regions(self.last_inputs):
            h,w,k = im_region.shape
            amax = np.amax(im_region,axis=(0,1))
            for i2 in range(h):
                for j2 in range(w):
                    for k2 in range(k):
                        if(im_region[i2,j2,k2] == amax[k2]):
                            d_L_d_inputs[(i*2+i2),(j*2+j2),k2] = d_L_d_outs[i,j,k2]
        return d_L_d_inputs
        