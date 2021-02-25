# pytorch lecture 01~05

Created: Feb 25, 2021 11:39 AM

### Why Pytorch?

1.  more Pythonic (imperative) 

- Flexible
- intuitive and cleaner code
- Easy to debug

2. More Neural Networkic

- write code as the networks
- forward/ backward

### Model design : Linear Model

input x, predict y. 

y_hat = x * w 

error = (y-y_hat)^2

Trainging Loss(error) : ( y_hat - y )^2 

### Back-propagation and Autograd