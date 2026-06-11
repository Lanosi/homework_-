# import sys
# sys.setrecursionlimit(10000)   # увеличиваем глубину рекурсии
#
# def F(n):
#     if n == 1:
#         return 1
#     if n > 1:
#         return (3 * n + 5) * F(n - 1)
#
# print(F(2073) // F(2070))

# #аналитикой
result = 1
for k in range(2071, 2074):
    result *= (3 * k + 5)
print(result)
