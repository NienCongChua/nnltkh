import matplotlib.pyplot as plt
import numpy as np

def nhap():
    print("Nhap cac he ao a, b, c, d cua ham so: ")
    x = float(input("a = "))
    y = float(input("b = "))
    z = float(input("c = "))
    t = float(input("d = "))
    return x, y, z, t

def ve_do_thi():
    a, b, c, d = nhap()
    x = np.linspace(-20, 20, 2000)
    y = a * x ** 3 + b * x ** 2 + c * x + d
    plt.plot(x, y, marker="", linestyle="-", color="g")
    plt.title("Đồ thị của hàm số $y = ax^3 + bx^2 + cx + d$", fontsize=16, color='darkred')
    plt.xlabel("Trục x", fontsize=14, color='green')
    plt.ylabel("Trục y", fontsize=14, color='green')
    plt.grid(True)
    plt.show()


def nhap_mang():
    try:
        n = int(input("Enter n: "))
        x = np.empty(n)
        for i in range (n):
            x[i] = int(input(f"x[{i}] = "))
        return x
    except:
        return ValueError
    

def phan_tu_chan(a):
    a = a[a % 2 == 0]
    print(a)
    print(sum(a))

def chuyen_a(x):
    p = int(input("Enter p: "))
    if x.size % p == 0:
        return a.reshape(p, x.size // p)
    else:
        return np.empty(0)

ve_do_thi()
a = nhap_mang()
phan_tu_chan(a)
a = np.sort(a, kind="heapsort")
print(a)
d = chuyen_a(a)
print(d)