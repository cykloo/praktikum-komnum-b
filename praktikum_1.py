import matplotlib.pyplot as plt
import numpy as np

# Definisi fungsi f(x)
def f(x):
    return x**3 - x - 2  # Contoh fungsi; bisa diganti sesuai kebutuhan

# Implementasi metode Regula Falsi
def regula_falsi(a, b, tol=1e-5, max_iter=100):
    if f(a) * f(b) >= 0:
        print("Metode gagal: f(a) dan f(b) harus beda tanda.")
        return None

    iterasi = 0
    hasil_iterasi = []

    while iterasi < max_iter:
        # Titik tengah menggunakan Regula Falsi (interpolasi linear)
        c = b - (f(b)*(b-a))/(f(b)-f(a))

        hasil_iterasi.append((iterasi+1, a, b, c, f(c)))

        if abs(f(c)) < tol:
            break

        if f(a)*f(c) < 0:
            b = c
        else:
            a = c

        iterasi += 1

    # Menampilkan tabel iterasi
    print(f"{'Iter':<6}{'a':<12}{'b':<12}{'c':<12}{'f(c)':<12}")
    for row in hasil_iterasi:
        print(f"{row[0]:<6}{row[1]:<12.6f}{row[2]:<12.6f}{row[3]:<12.6f}{row[4]:<12.6f}")

    print(f"\nAkar aproksimasi: {c:.6f}")
    return c

# Menjalankan fungsi
akar = regula_falsi(1, 2)

# Membuat grafik fungsi
x_vals = np.linspace(0, 3, 400)
y_vals = f(x_vals)

plt.figure(figsize=(8, 5))
plt.plot(x_vals, y_vals, label='f(x)')
plt.axhline(0, color='black', linestyle='--')
plt.axvline(akar, color='red', linestyle='--', label=f'Akar ≈ {akar:.5f}')
plt.title('Grafik Fungsi dan Akar dengan Regula Falsi')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)
plt.show()
