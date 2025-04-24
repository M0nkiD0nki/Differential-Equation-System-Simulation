import numpy as np
import matplotlib.pyplot as plt

# Parametry systemu
R1 = float(input("Podaj wartość rezystancji R1: "))
R2 = float(input("Podaj wartość rezystancji R1: "))
L1 = float(input("Podaj wartość indukcyjnosci L1: "))
L2 = float(input("Podaj wartość indukcyjnosci L2: "))
M = float(input('Podaj wartosc zewn. sily motorycznej U: '))

if(R1<0 or R2<0 or L1<0 or L2<0 or M<0):
    print("Podano bledne wartosci")
    exit()

# Liczba okresów sygnału sinus w przedziale T
L=3

# Czas symulacji
T = 100
h = 0.001
total = int(T / h)

# Tworzenie list na dane
czas = np.linspace(0, T, total)
us = M * np.sin(2 * np.pi * L/T * czas)
up = np.ones(total) * M

# Parametry równań różniczkowych
A = L1 * L2
B = R1 * L1 + L1 * R2 + L2 * R1
C = R1 * R2

# Function to calculate y
def calculate_y(u, total):
    y = np.zeros((3, total))
    for i in range(1, total):
        k1 = h * y[1, i-1]
        l1 = h * (-C/A * y[0, i-1] - B/A * y[1, i-1] - y[2, i-1] + C/A * u[i-1])
        k2 = h * (y[1, i-1] + l1/2)
        l2 = h * (-C/A * (y[0, i-1] + k1/2) - B/A * (y[1, i-1] + l1/2) - (y[2, i-1] + l1/2) + C/A * u[i-1])
        y[0, i] = y[0, i-1] + k2
        y[1, i] = y[1, i-1] + l2
        y[2, i] = y[2, i-1] + y[1, i-1] * h
    return y[2]

yn = calculate_y(up, total)
yns = calculate_y(us, total)
# Rysowanie wykresów
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)

ax1.set_title('Pobudzenie sinusoidalne')
ax1.plot(czas, us)
ax1.grid(True)

ax2.set_title('Pobudzenie skokiem')
ax2.plot(czas, up)
ax2.grid(True)

ax3.set_title('Odpowiedz na pobudzenie sinusoidalne')
ax3.plot(czas, yns)
ax3.set_xlabel('t')
ax3.set_ylabel('H(s)')
ax3.grid(True)

ax4.set_title('Odpowiedz na pobudzenie skokowe')
ax4.plot(czas, yn)
ax4.set_xlabel('t')
ax4.set_ylabel('H(s)')
ax4.grid(True)

plt.tight_layout()
plt.show()