import numpy as np

#d = np.arange(6).reshape((3, 2))
#a = np.array([1,2])
#print(d)
#b = d @ a
#print(b)
#c = np.random.randn(5,3)
#print(a[0:2])
#print(np.array([[1,2,3], [4,5,6]]))
#a = np.array([[[1,2,3], [4,5,6]],[[7,8,9],[10,11,12]], [[13,14,15],[16,17,18]]])
#print(a)
#print(a.shape)
#output = np.zeros((4, 4, 2))
#print(output)
#a = np.array([[-1,0,1], [-2,0,2], [-1,0,1]])
#b = np.array([[1,2,3], [4,5,6], [7,8,9]])
#c = a*b
filters = np.random.randn(8,3,3) / 9
d_L_d_filter = np.zeros(filters.shape)
print(d_L_d_filter[2])
'''
test_mask = np.array([[[-1,0,1], [-2,0,2], [-1,0,1]],
                       [[0,0,0], [0,0,0], [0,0,0]]
                       ])
sobel_mask = np.array([[-1,0,1], [-2,0,2], [-1,0,1]])
test_img = np.array([[0,0,0,0,0,0], [0,0,50,0,29,0],
          [0,0,80,31,2,0], [0,33,90,0,75,0],
          [0,0,9,0,95,0], [0,0,0,0,0,0]
          ])
# test cnn with input_img and sobel_mask
output_cnn = np.array([[180,31,-120,-31],
                       [300,29,-192,-62],
                       [269,-35,-97,-31],
                       [108,-33,157,0]
                      ])
print(np.array([[-1,0,1], [-2,0,2], [-1,0,1]]))


a = np.array([[[ 0,  1],
        [ 2,  3],
        [ 4,  5]],

       [[ 6,  7],
        [ 8,  9],
        [10, 11]],

       [[12, 13],
        [14, 15],
        [16, 17]],

       [[18, 19],
        [20, 21],
        [22, 23]]])
print(np.sum(a,axis=(1,2)))
'''