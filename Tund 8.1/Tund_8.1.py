import numpy as np
import matplotlib.pyplot as plt

# 1. Верхняя дуга зонта (вся)
x1 = np.linspace(-12, 12, 400)
y1 = -1/18 * x1**2 + 12

# 2. Центральная дуга (низ)
x2 = np.linspace(-4, 4, 200)
y2 = -1/8 * x2**2 + 6

# 3. Левая нижняя дуга
x3 = np.linspace(-12, -4, 200)
y3 = -1/8 * (x3 + 8)**2 + 6

# 4. Правая нижняя дуга
x4 = np.linspace(4, 12, 200)
y4 = -1/8 * (x4 - 8)**2 + 6

# 5. Левая ручка зонта (нижняя часть)
x5 = np.linspace(-4, -0.3, 200)
y5 = 2 * (x5 + 3)**2 - 9

# 6. Левая ручка зонта (верхняя часть)
x6 = np.linspace(-4, 0.2, 200)
y6 = 1.5 * (x6 + 3)**2 - 10


plt.figure(figsize=(10, 6))
plt.plot(x1, y1, color='navy', linewidth=2, label="верхняя дуга")
plt.plot(x2, y2, color='dodgerblue', linewidth=2)
plt.plot(x3, y3, color='dodgerblue', linewidth=2)
plt.plot(x4, y4, color='dodgerblue', linewidth=2)
plt.plot(x5, y5, color='darkred', linewidth=2)
plt.plot(x6, y6, color='red', linewidth=2)

plt.title("Зонтик ☂", fontsize=16)
plt.grid(True)
plt.axhline(0, color='gray', linewidth=0.5)
plt.axvline(0, color='gray', linewidth=0.5)
plt.axis("equal")  # чтобы пропорции не искажались
plt.tight_layout()
plt.show()

