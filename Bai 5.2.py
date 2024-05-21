import numpy as np
#1 nhap mang
def nhap(n, name):
    print('Nhap mang', name)
    a = np.random.rand(n)
    for i in range(n):
        a[i] = float(input(name + "[{}] = ".format(i)))
    return a
n = int(input("n= "))
a = nhap(n, 'a')
b = nhap(n, 'b')
#2,3 tinh toan
print('Mang a: ', a)
print('Mang b: ', b)
c = a + b
d = a-b
e = a*b
f = a/b
print('Mang c: ', c)
print('Mang d: ', d)
print('Mang e: ', e)
print('Mang f: ', f)
#4 su dung ham
print('Mang c: ', c.sum())
print('Mang c: ', c.max())
print('Mang c: ', c.min())
#5 slicing
k = c[2::2]
print('Cac phan tu co chi so chan trong c: ',k)
print('Tong = ', k.sum())
#6 reshape tu 1D thanh 2D
try:
    t = int(input('Nhap so dong cua ma tran: '))
    if n%t != 0: raise ValueError
    k = c.reshape(t, n//t)
    print('Ma tran thu duoc: \n', k)
except:
    print(ValueError, ': Khong the reshap!')