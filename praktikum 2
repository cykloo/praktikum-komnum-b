import numpy as np
import matplotlib.pyplot as plt

# Fungsi yang ingin diintegrasikan
def f(x):
    return x**2 * np.cos(x**2)

# Fungsi metode Trapezoidal sederhana
def trapezoid(f, a, b, n):
    h = (b - a) / n
    result = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        result += f(a + i * h)
    return result * h

# Fungsi metode Romberg
def romberg(f, a, b, max_iter):
    R = np.zeros((max_iter, max_iter))
    for i in range(0, max_iter):
        n = 2**i
        R[i, 0] = trapezoid(f, a, b, n)
        for k in range(1, i + 1):
            R[i, k] = (4**k * R[i, k-1] - R[i-1, k-1]) / (4**k - 1)
    return R

# Interval integrasi dan jumlah iterasi
a = 1.5
b = 2.5
max_iter = 5

# Jalankan Romberg
R = romberg(f, a, b, max_iter)

# Tampilkan hasil
print("Tabel Romberg:")
for i in range(max_iter):
    print("Iterasi", i, ":", ["{:.10f}".format(val) for val in R[i, :i+1]])

# Plot konvergensi Romberg
romberg_approx = [R[i, i] for i in range(max_iter)]
plt.plot(range(1, max_iter+1), romberg_approx, marker='o', label='Aproksimasi Romberg')
plt.xlabel("Iterasi")
plt.ylabel("Hasil Integral")
plt.title("Konvergensi Integrasi Romberg")
plt.grid(True)
plt.legend()
plt.show()
