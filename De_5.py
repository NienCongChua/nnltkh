import numpy as np
import matplotlib.pyplot as plt

def nhap_mang():
    try:
        n = int(input("Enter n: "))
        x = np.empty(n)
        y = np.empty(n)
        for i in range(n):
            x[i] = float(input(f"a[{i}] = "))
        for i in range(n):
            y[i] = float(input(f"b[{i}] = "))
        return x, y
    except:
        return ValueError

def convert_a(x):
    try:
        tmp = x
        k = int(input("Enter k: "))
        if tmp.size % k == 0:
            return tmp.reshape(k, tmp.size // k)
        else: raise ValueError
    except:
        print("Khong the chuyen doi.", end="\t")
        return ValueError
        
def dang_mieng(x):
    plt.figure(figsize=(10, 10))
    plt.pie(x, labels=[str(i) for i in x], autopct="%1.1f%%")
    plt.title("Do thi dang mieng")
    plt.show()

def dang_duong(x):
    plt.plot(x, marker="o", linestyle="--", color="r")
    plt.title("Đồ thị dạng đường")
    plt.xlabel("Trục x")
    plt.ylabel("Trục y")
    plt.grid(True)
    plt.show()


a, b = nhap_mang()
print(a)
print(b)
print(convert_a(a))
print(sum(b[2:6]))
a = np.sort(a)
b = np.sort(b)[::-1]
print(np.concatenate((a, b)))
dang_mieng(a)
dang_duong(b)
