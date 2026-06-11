def search(arr, x):
    """
    Итеративный интерполяционный поиск в отсортированном списке.
    Возвращает: (индекс, количество_сравнений)
    Если элемент не найден, индекс = -1.
    """
    low = 0
    high = len(arr) - 1
    comparisons_cnt = 0

    while low <= high and arr[low] <= x <= arr[high]: # проверка на: массив не пуст и находиться внутри списка

        # Защита от деления на ноль (если все элементы одинаковые)
        if arr[high] == arr[low]:
            if arr[low] == x: # (1)попробовать сделать все элемены одинаковыми в 2х вариантах x == !=
                comparisons_cnt += 1
                return low, comparisons_cnt
            else:
                break

        # Вычисление позиции для интерполяции
        pos = low + ((x - arr[low]) * (high - low)) // (arr[high] - arr[low])

        # Сравнение
        comparisons_cnt += 1
        if arr[pos] == x:
            return pos, comparisons_cnt
        elif arr[pos] < x:
            low = pos + 1
        else:
            high = pos - 1

    # Если не нашли
    return -1, comparisons_cnt


# ----- Проверка работоспособности -----
def test_search():
    # Случай 1: элемент есть
    arr1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    x1 = 60
    idx, cmp1 = search(arr1, x1)
    print(f"Есть в списке: массив {arr1}, ищем {x1}")
    print(f"  Индекс: {idx}, сравнений: {cmp1}\n")

    # Случай 2: элемента нет
    arr2 = [5, 15, 25, 35, 45, 55]
    x2 = 20
    idx2, cmp2 = search(arr2, x2)
    print(f"Нет в списке: массив {arr2}, ищем {x2}")
    print(f"  Индекс: {idx2}, сравнений: {cmp2}\n")


# ----- Анализ числа сравнений при разной размерности -----
def analyze_comparisons():
    import random
    # Создадим отсортированные списки разной длины с равномерным распределением
    sizes = [100, 500, 1000, 5000, 10000]
    # Искать будем случайный элемент из каждого списка (присутствует)
    print("Анализ числа сравнений для интерполяционного поиска")
    print("Размер\tСравнений")
    for size in sizes:
        # Генерируем равномерно распределённые целые числа
        arr = sorted([random.randint(0, size * 10) for _ in range(size)])
        # Берём элемент, который точно есть (например, из середины)
        x = arr[size // 2]
        _, comparisons = search(arr, x)
        print(f"{size}\t{comparisons}")


if __name__ == "__main__":
    test_search()
    analyze_comparisons()