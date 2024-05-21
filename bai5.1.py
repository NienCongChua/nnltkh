import numpy as np
#1
n = int(input("n = "))
a = np.random.rand(n)
print("a= ", a)
print("So chieu cua a: ", a.ndim)
print("Kich thuoc moi chieu: ", a.shape)
print('Do dai cua a: ', len(a))
print('kich thuoc 1 phan tu: ', a.itemsize)
print('kieu cua cac phan tu: ', a.dtype)
#2
b = np.linspace(1, n, 100)
print('b= ',b)
print('so chieu cua a: ', a.ndim)
print('kich thuoc moi chieu: ', a.shape)
print('Do dai cua b: ', len(b))
print('kich thuoc 1 phan tu: ', a.itemsize)
print('kieu cua cac phan tu: ', a.dtype)
#3
c = np.arange(2, 201, 2)
print('Mang c: \n', c)
#4
d = np.ones(100)
print('Mang d:\n', d)
#5
e = np.zeros(100)
print('Mang e:\n', e)
#6
h = np.random.rand(100)
print('Mang h:\n', h)
#7
m = int(input('m = '))
k = np.ones((n, m))
print('Mang k:\n',k)
#8
p = np.eye(n)
print('Mang p:\n', p)
#9
q = np.diag(a)
print('Mang q:\n', q)