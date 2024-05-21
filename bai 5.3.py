import numpy as np
#1 nhap mang
def nhap(n, name):
    print('Nhap mang: ', name)
    a = np.random.rand(n)
    for i in range(n):
        a[i] = float(input(name + "[{}] = ".format(i)))
    return a
#2 Ham reshape
def to2d(a, n):
    try:
        t = int(input('Nhap so dong cua mang: '))
        if n%t != 0: raise ValueError
        k = a.reshape(t, n//t)
        return k
    except:
        print(ValueError, ' : Khong the reshape')
        return
n = int(input("n= "))
a = nhap(n, 'a')
a = to2d(a, n)
#3
print('Mang a:\n', a)
if len(a[0]) > 1:
    b = a[:, 0]
    c = a[:, 1]
    b = np.reshape(b, -1)
    c = np.reshape(c, -1)
    print('Cot thu nhat b: ', b)
    print('Cot thu hai c: ', c)

    d = np.concatenate((b, c))
    print('Mang d: ',d)

    k = np.where(d>1)
    print('Vi tri cac phan tu lon hon 1 trong c:', k[0])

d = np.sort(d, kind='heapsort')
print('c da sap xep: ',d)

k = int(input('Nhap vao gia tri can chen: '))
vt = np.searchsorted(d, k)
print('Vi tri thich hop de chen: ', vt)

d = np.insert(d, vt, k)
print('Mang d sau khi chen: ', d)