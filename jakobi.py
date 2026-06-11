import numpy as np

# Матрица коэффициентов
A = np.array([
    [3.476, 0.259, 0.376, 0.398],
    [0.425, 4.583, 0.417, 0.328],
    [0.252, 0.439, 3.972, 0.238],
    [0.265, 0.291, 0.424, 3.864]
])

# Вектор свободных членов
b = np.array([0.871, 0.739, 0.644, 0.581])

# Точность
eps = 0.0001

# Начальное приближение
x = np.zeros(4)

iteration = 0

while True:
    x_new = np.zeros(4)

    for i in range(4):
        s = 0
        for j in range(4):
            if i != j:
                s += A[i][j] * x[j]

        x_new[i] = (b[i] - s) / A[i][i]

    print(f"Итерация {iteration + 1}: {x_new}")

    if np.max(np.abs(x_new - x)) <= eps:
        break

    x = x_new.copy()
    iteration += 1

print("\nРешение:")
print(x_new)
print("Количество итераций:", iteration + 1)