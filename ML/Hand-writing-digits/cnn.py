import mnist
import numpy as np
from conv import Conv
from maxpool import MaxPool
from softmax import Softmax
import cv2


'''
input_img = np.array([[0,0,0,0,0,0], [0,0,50,0,29,0],
          [0,0,80,31,2,0], [0,33,90,0,75,0],
          [0,0,9,0,95,0], [0,0,0,0,0,0]
          ])
'''
train_images = mnist.train_images()[:1000]
train_labels = mnist.train_labels()[:1000]
test_images = mnist.test_images()[:1000] # test image size: 28 x 28
test_labels = mnist.test_labels()[:1000]

conv = Conv(8)   # 28 x 28 -> 26 x 26 x 8
pool = MaxPool() # 26 x 26 x 8 -> 13 x 13 x 8
softmax = Softmax(13*13*8,10) # 10 nodes for 10 digits 0 -> 9

def forward(images,labels):
    # transform image from [0->255] to [-0.5->0.5]
    out = conv.forward((images / 255)-0.5)
    out = pool.forward(out)
    out = softmax.forward(out)
    
    loss = -np.log(out[labels])
    if np.argmax(out) == labels:
        acc = 1
    else:
        acc = 0
    return out,loss,acc

def train(image,label,learning_rate=0.005):
    out,loss,acc = forward(image,label)
    gradient = np.zeros(10)
    gradient[label] = - 1 / out[label]
    
    gradient = softmax.backpropagate(gradient,learning_rate)
    gradient = pool.backpropagate(gradient)
    gradient = conv.backpropagate(gradient,learning_rate)
    return loss,acc
    

'''
cv2.imshow('image',test_images)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''

print("CNN MNIST initialized")

for epoch in range(1):
    print('---Epoch {}---'.format(epoch))
    permutation = np.random.permutation(len(train_images))
    train_images = train_images[permutation]
    train_labels = train_labels[permutation]
    
    loss = 0
    number_of_correct = 0
    
    # zip to pair image and label, enumerate to number the order
    for i, (img,label) in enumerate(zip(train_images,train_labels)):
        l,acc = train(img,label,0.005)
        loss += l
        number_of_correct += acc
        
        if i % 100 == 99:
            print("[Step %d] Past 100 steps: Average Loss %.3f | Accuracy: %d%%" %(i+1,loss/100,number_of_correct))
            loss = 0
            number_of_correct = 0

print('\n--- Testing CNN ---')
loss = 0
number_of_correct = 0
for im, label in zip(test_images,test_labels):
    _, l, acc = forward(im,label)
    loss += l
    number_of_correct += acc
    
number_tests = len(test_images)
print('Test Loss: ',loss / number_tests)
print('Test Accuracy: ',number_of_correct / number_tests)




