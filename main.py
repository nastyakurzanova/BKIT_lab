import sys
import math

#C:\Users\admin\PycharmProjects\pythonProject1\main.py

def get_coef(index, prompt):
    while True:
        try:
            # Пробуем прочитать коэффициент из командной строки???
            print(prompt)  # ?
            coef_str = input()
            # Переводим строку в действительное число
            coef = float(coef_str)
            return coef
           # coef_str = sys.argv[index]
        except:
            continue


def get_roots(a, b, c):
    result = []
    if c == 0:
        root1 = 0
        result.append(root1)
        D = -b / a
        if D > 0:
            root2 = math.sqrt(D)
            root3 = -math.sqrt(D)
            result.append(root2)
            result.append(root3)
    else:
        D = b * b - 4 * a * c
        if D > 0:
            t1 = (-b + math.sqrt(D)) / (2 * a)
            t2 = (-b - math.sqrt(D)) / (2 * a)
            if t1 > 0:
                root1 = math.sqrt(t1)
                root2 = -math.sqrt(t1)
                result.append(root1)
                result.append(root2)
            if t1 == 0.0:
                root = 0
                result.append(root)
            if t1 < 0:
                print('')
            if t2 > 0:
                root3 = math.sqrt(t2)
                root4 = -math.sqrt(t2)
                result.append(root3)
                result.append(root4)
            if t2 == 0.0:
                root = 0
                result.append(root)
            if t2 < 0:
                print('')
        if D == 0:
            t = -b / (2 * a)
            if t > 0:
                root1 = math.sqrt(t)
                root2 = -math.sqrt(t)
                result.append(root1)
                result.append(root2)
            if t == 0.0:
                root = 0
                result.append(root)
            if t < 0:
                print('')
        if D < 0:
            print('')
    return result


def main():
    while (1):
        a = get_coef(1, 'Введите коэффициент А:')
        if a != 0:
            break
        else:
            print('Данный коэффициент не может быть равен 0! Введите новое значение')

    b = get_coef(2, 'Введите коэффициент B:')
    c = get_coef(3, 'Введите коэффициент C:')
    # Вычисление корней
    roots = get_roots(a, b, c)
    # Вывод корней
    len_roots = len(roots)
    if len_roots == 0:
        print('Нет корней :(')
    elif len_roots == 1:
        print('Один корень: {}'.format(roots[0]))
    elif len_roots == 2:
        print('Два корня: {} и {}'.format(roots[0], roots[1]))
    elif len_roots == 3:
        print('Три корня: {} и {} и {}'.format(roots[0], roots[1], roots[2]))
    elif len_roots == 4:
        print('Четыре корня: {} и {} и {} и {}'.format(roots[0], roots[1], roots[2], roots[3]))


# Если сценарий запущен из командной строки
if __name__ == "__main__":
    while True:
        main()
