while True:
    try:
        a = list(map(int, input('Укажите произвольный набор чисел через запятую: ').split(',')))
    except Exception:
        print("<<Ошибка!>> Пример ввода чисел: 46,2,26,72,12,27")
    else:
        break

while True:
    try:
        b = list(map(int, input(f'Введите число от {min(list(a))} до {max(list(a))}: ').split(',')))
        if min(list(b)) < min(list(a)) or min(list(b)) > max(list(a)):
            raise ValueError
    except ValueError:
        print(f"Нужно ввести число от {min(list(a))} до {max(list(a))}!")
    else:
        break

array, num = list(map(int, a)), list(map(int, b))
array.extend(num)
print("Список чисел:", array)


def sortArray(array):
    for i in range(1, len(array)):
        x = array[i]
        p = i
        while p > 0 and array[p - 1] > x:
            array[p] = array[p - 1]
            p -= 1
        array[p] = x
    return array
sortA = sortArray(array)
print("Сортировка:", sortA)

def double_search(sortA, element, left, right):
    if left > right:
        return False

    middle = (right + left) // 2
    if element == sortA[middle]:
        return middle
    elif element < sortA[middle]:
        return double_search(sortA, element, left, middle - 1)
    else:
        return double_search(sortA, element, middle + 1, right)

element = min(b)
idx = double_search(sortA, element, 0, len(sortA))

if element == max(sortA):
    Pidx = idx
elif element == min(sortA):
    Pidx = "- не определён, так как введённое число минимальное"
else:
    Pidx = idx - 1

print(f"Последний индекс в списке: {len(sortA)-1}")
print(f"Предшествующий числу {element} индекс:", Pidx)

