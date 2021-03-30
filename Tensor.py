
import torch


####张量的复制#####
clone_flag = 0
if clone_flag:
    a = torch.tensor(2.,requires_grad=True)
    f = 3*a
    f.backward()
    print(a.grad)  #输出f对a的梯度值 3
    a_clone = a.clone()#构建a的clone
    f_2 = 2*a_clone
    f_2.backward()
    print(a_clone.grad)#由于a_clone是中间节点，所以梯度值不会被保存
    print(a.grad)#a_clone的梯度值会叠加在其上面 3+2=5
    #id函数返回对象的标识符，两者不是一个对象
    print(id(a))
    print(id(a_clone))
    #tensor.data_ptr()返回tensor的内存地址
    print(a.data_ptr())
    print(a_clone.data_ptr())


detach_flag = 1
if detach_flag:
    a =torch.tensor(2.,requires_grad=True)
    a_detach = a.detach()
    print("id(a):",id(a),"id(a_detach):",id(a_detach))#id(a): 140622609912512 id(a_detach): 140622609912640
    print("a的内存地址：",a.data_ptr(),"a_detach的内存地址：",a_detach.data_ptr()) #a的内存地址： 140622619874624 a_detach的内存地址： 140622619874624
    f = 3 * a
    f.backward()
    print(a.grad)
    g = 4 * a_detach
    # g.backward()
    # print(a_detach.grad)
    print(a.grad)
    a = torch.tensor(4.,requires_grad=True)
    a = a+2
    print(a_detach)

import torch
import numpy as np
aa = np.array([[1., 2, 3], [4, 5, 6]]).astype(np.float32)
bb = torch.tensor(aa, requires_grad=True)  # 复制了数据
aa[0, 0] = 100
print(bb)
'''
tensor([[1., 2., 3.],
        [4., 5., 6.]], requires_grad=True)
'''


print(aa)
'''
[[100.   2.   3.]
 [  4.   5.   6.]]
'''


cc = bb.detach()
print(cc.requires_grad)  # False
cc[0, 0] = 1000

print(cc)
'''
tensor([[1000.,    2.,    3.],
        [   4.,    5.,    6.]])
'''


print(bb)
