# conda install pytorch torchvision cudatoolkit=10.2 -c pytorch
# pip install torch===1.5.0 torchvision===0.6.0 -f https://download.pytorch.org/whl/torch_stable.html
# https://www.youtube.com/watch?v=jexkKugTg04
import torch
import numpy as np

print(torch.cuda.is_available())

t = torch.Tensor()
print(type(t))

print(t.dtype)
print(t.device)
print(t.layout)

# cuda:0 - index of GPU
device = torch.device("cuda:0")
print(device)

t1 = torch.tensor([1, 2, 3])
t2 = torch.tensor([1., 2., 3.])
t3 = t1.cuda()

print(t1.dtype)
print(t2.dtype)
print(t3.dtype)

print(t1.device)
print(t3.device)


data = np.array([1, 2, 3])
print(type(data))


print(torch.Tensor(data))
print(torch.tensor(data))
print(torch.as_tensor(data))
print(torch.from_numpy(data))

print(torch.eye(2))
print(torch.zeros(2, 2))
print(torch.ones(2, 2))
print(torch.rand(2, 2))
