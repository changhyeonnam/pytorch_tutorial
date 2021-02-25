import torch

'''
torch.tensor(data, *, dtype=None, device=None, requires_grad=False, pin_memory=False) → Tensor

1. data (array_like) 
    –   Initial data for the tensor. Can be a list, tuple, NumPy ndarray, scalar, and other types.
2. dtype (torch.dtype, optional) 
    –   the desired data type of returned tensor. Default: if None, infers data type from data.
3. device (torch.device, optional) 
    –   the desired device of returned tensor. Default: if None, uses the current device for the default tensor type (see torch.set_default_tensor_type()). 
        device will be the CPU for CPU tensor types and the current CUDA device for CUDA tensor types.
4. requires_grad (bool, optional) 
    –   If autograd should record operations on the returned tensor. Default: False.
5. pin_memory (bool, optional) 
    –   If set, returned tensor would be allocated in the pinned memory. Works only for CPU tensors. Default: False.
'''

t1 = torch.tensor([[0.1,1.2],[2.2,3.1],[4.9,5.2]])
print(t1)
