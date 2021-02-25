# basic, linear regression
import numpy as np
import matplotlib.pyplot as plt

x_data = [1.0,2.0,3.0]
y_data = [2.0,4.0,6.0]

def forward(x,w):
    return x*w

def loss(x,w,y):
    y_hat = forward(x,w)
    return (y-y_hat)*(y-y_hat)

w_list = []
mse_list = []

for w in np.arange(0.0,4.1,0.1):
    print(f'w: {w}')

    loss_sum = 0
    for x_val,y_val in zip(x_data,y_data):
        predict_val = forward(x_val,w)
        l = loss(x_val,w,y_val)
        loss_sum += l
        print('\t',x_val,y_val,predict_val,l,)

    mse = loss_sum/len(x_data)
    print(f'MSE={mse}')
    w_list.append(w)
    mse_list.append(mse)

plt.plot(w_list,mse_list)
plt.ylabel('Loss')
plt.xlabel('Weight')
plt.show()