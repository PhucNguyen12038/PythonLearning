import numpy as np

class Conv:
    def __init__(self,number_of_filters):
        self.number_of_filters = number_of_filters
        self.filters = np.random.randn(number_of_filters,3,3) / 9
    
    def im_regions(self,image):
        h,w = image.shape
        for i in range(h-2):
            for j in range(w-2):
                im_region = image[i:(i+3),j:(j+3)]
                yield im_region,i,j
    
    def forward(self,inputs):
        self.last_inputs = inputs
        h,w = inputs.shape
        output = np.zeros((h-2,w-2,self.number_of_filters))
        for im_region,i,j in self.im_regions(inputs):
            output[i,j] = np.sum(im_region*self.filters,axis=(1,2))
        return output
    
    def backpropagate(self,d_L_d_outs,lr):
        #d_L_d_outs has size (H-2), (W-2), N of image input
        d_L_d_filter = np.zeros(self.filters.shape)
        for im_region,i,j in self.im_regions(self.last_inputs):
            for k in range(self.number_of_filters):
                d_L_d_filter[k] = d_L_d_outs[i,j,k] * im_region  
        
        self.filters += lr * d_L_d_filter
        return None