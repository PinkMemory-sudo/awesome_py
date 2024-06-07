from __future__ import print_function
import torch

x = torch.rand(5, 3)
print(x)

# 是否启用并可访问GPU驱动程序和CUDA
print(torch.cuda.is_available())

# 矢量
temp = torch.FloatTensor([23, 24, 24.5, 26, 27.2, 23.0])
print(temp.size())

# 标量
t = torch.rand(10)
print(t.size())

# 矩阵
