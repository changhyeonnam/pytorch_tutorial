
# Training Data
x_data = [1.0, 2.0, 3.0]
y_data = [2.0, 4.0, 6.0]

w = 1.0  # a random guess: random value
lr = 0.01
'''
 epoch 10 동안 계속 loop를 돌면서, w 업데이트. 
 epoch,updated weight, loss 출력 
    각 데이터셋의 gradinet 출력
'''

def forward(x,w) :
    return w*x

def loss(x,w,y):
    y_predict = forward(x,w)
    return (y_predict-y)*(y_predict-y)

'''
(y-w*x)^2를 w에 대해 편미분
2 * (x) * (x * w -y)
'''

def gradient(x,w,y):
    return 2 * x * (x * w -y)

# before training
print("Prediction (before training)",f'default weight: {w} forward(x=4,default w=1) : {forward(4,w)}')

for epoch in range (10):
    for x_val,y_val in zip(x_data,y_data):
        predict_val = forward(x_val,w)
        grad = gradient(x_val,w,y_val)
        w = w - lr * grad
        print(f'\t gradient: {x_val}, {y_val}, {round(grad,2)}')
        l = loss(x_val,w,y_val)
    print(f'progress: {epoch}, w={round(w,2)}, loss={round(l,2)}')

print(f'Predicted score (after training) : {forward(4,w)}')