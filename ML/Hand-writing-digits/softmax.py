import numpy as np

class Softmax():
    def __init__(self,input_len,number_of_nodes):
        self.weights = np.random.randn(input_len,number_of_nodes) / input_len
        self.biases = np.zeros(number_of_nodes)

    def forward(self,inputs):
        self.last_input_shape = inputs.shape
        inputs = inputs.flatten()
        self.last_input = inputs
        input_len,nodes = self.weights.shape
        totals = np.dot(inputs,self.weights) + self.biases
        self.last_totals = totals
        exp = np.exp(totals)
        return exp / np.sum(exp,axis=0)
        
    def backpropagate(self,d_L_d_out,lr):
        for i,gradient in enumerate(d_L_d_out):
            if gradient == 0:
                continue
            
            t_exp = np.exp(self.last_totals)
            S = np.sum(t_exp)
            
            d_out_d_t = -t_exp[i] * t_exp / (S**2)
            d_out_d_t[i] = t_exp[i] * (S - t_exp[i]) / (S**2)
            
            d_t_d_w = self.last_input # array 1d with size (H x W x Filter_num)
            d_t_d_b = 1
            d_t_d_input = self.weights
            
            d_L_d_t = gradient * d_out_d_t # array 1d 10 elements
            d_L_d_w =  d_t_d_w[np.newaxis].T @ d_L_d_t[np.newaxis]
            
            d_L_d_b = d_L_d_t * d_t_d_b
            d_L_d_input = d_t_d_input @ d_L_d_t # d_L_d_input is arr 1d size (H x W x Filter_num)
            
            self.weights = self.weights - lr * d_L_d_w
            self.biases = self.biases - lr * d_L_d_b

            return d_L_d_input.reshape(self.last_input_shape)
        