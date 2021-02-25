import torch
import pdb

# Training Data
x_data = [1.0, 2.0, 3.0]
y_data = [2.0, 4.0, 6.0]
w = torch.tensor([1.0],requires_grad=True)
lr = 0.01

def forward(x):
    return x * w

def loss(y_pred,y_val):
    return (y_pred-y_val)**2

print("Prediction (before training)", 4, forward(4).item())

for epoch in range(10) :
    for x_val, y_val in zip(x_data,y_data) :
        y_pred = forward(x_val)
        l = loss(y_pred,y_val)
        l.backward()
        print(f'\t grad: {x_val},{y_val},{w.grad.item()}')
        w.data = w.data - lr * w.grad.item()

        w.grad.data.zero_()

    print(f'Epoch: {epoch} | Loss: {l.item()}')

print('Prediction (after trainig)', 4, forward(4).item())