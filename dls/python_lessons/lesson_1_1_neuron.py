print("\n Собственный класс \"Нейрон\"")
#  Собственный класс "Нейрон"
#  Реализуйте класс "Нейрон", у которого будет несколько методов:
#  -   __init__. Принимает на вход массив весов нейрона - w = (w_1, ..., w_n), а также функцию активации f (аргумент по умолчанию f(x) = x). Сохраняет веса и функцию внутри класса.
#  - forward. Принимает на вход массив x = (x_1, ... , x_n) --- входы нейрона. Возвращает f(w_1x_1 + ... + w_nx_n).
#  - backlog. Возвращает массив xx, который подавался на вход функции forward при её последнем вызове. Если ранее функция forward не вызывалось, возвращает None.
#  В этом задании функция print вам не понадобится. Результаты выполнения функций нужно возвращать, а не печатать!
from functools import reduce


class Neuron:

    def __init__(self, w, f=lambda x: x):
        self.w = w
        self.func_activ = f
        self.x = None

    def forward(self, x):
        self.x = x
        sum_xw = sum([i * j for i, j in zip(x, self.w)])
        activation = self.func_activ(sum_xw)
        return activation

    def backlog(self):
        return self.x


ne = Neuron([1, 2, 3])
res = ne.forward([4, 5, 6])
print(res)
assert res == 32

print("\n Обработка текста")


# Обработка текста
# Дан список текстов, слова в которых разделены пробелами (можно считать, что знаков препинания нет). Часть слов является "мусорными": в них присутствуют цифры и спецсимволы. # Отфильтруйте такие слова из каждого текста.
# Используйте функции str.split, str.isalpha, str.join, а также list comprehensions.
# Пример ввода:
# ['1 thousand devils', 'My name is 9Pasha', 'Room #125 costs $100', '888']
# Пример вывода:
# ['thousand devils', 'My name is', 'Room costs', '']
# В этом задании функция print вам не понадобится. Результаты выполнения функций нужно возвращать, а не печатать!
# Если в тексте все слова являются мусорными, текст должен преобразоваться в пустую строку.
def process(sentences: list) -> list:
    result = []
    for word in sentences:
        result.append(" ".join([x for x in word.split(" ") if x.isalpha()]))
    return result


a = ['1 thousand devils', 'My name is 9Pasha', 'Room #125 costs $100', '888']
b = process(a)
print(b)
assert b == ['thousand devils', 'My name is', 'Room costs', '']

print("\n Создание массивов")


# Создание массивов
# Дан массив A[0,\ldots,N-1]A[0,…,N−1]. Реализуйте функцию cumsum_and_erase(...), принимающую один обязательный аргумент A и один опциональный аргумент erase, по умолчанию равный 1.
# Функция должна выполнять следующие действия:
# - сформировать массив B[0,\ldots, N-1]B[0,…,N−1], где B_i = A_0 + \ldots + A_{i}Bi=A0+...+Ai - массив частичных сумм массива AA;
# - удалить из массива BB все элементы, равные параметру eraseerase; получить массив C;
# - вернуть C в качестве ответа
# Постарайтесь сделать это за время O(N) без использования Numpy.
# Пример работы функции:
# A = [5, 1, 4, 5, 14]
# B = cumsum_and_erase(A, erase=10)
# assert B == [5, 6, 15, 29], "Something is wrong! Please try again"
# В этом задании функция print вам не понадобится. Результаты выполнения функций нужно возвращать, а не печатать!

def cumsum_and_erase(a: list, erase: int = 1) -> list:
    b = []
    for i in range(len(a)):
        val = sum(a[0:i + 1])
        if val != erase:
            b.append(val)
    return b


A = [5, 1, 4, 5, 14]
B = cumsum_and_erase(A, erase=10)
print(B)
assert B == [5, 6, 15, 29], "Something is wrong! Please try again"

print("\n Слайсы")
# Слайсы
# Дан list x:
# x = [1, 2, 3, 4, 5]
# x[<YOUR CODE>] = [-1, -3, -5]
# x
# Заполните слайс вместо <YOUR CODE>, чтобы результатом стал следующий list:
# [-5, 2, -3, 4, -1]
# Ничего больше менять в коде, например, создавать x или печатать его, не нужно!

x = [1, 2, 3, 4, 5]
x[len(x)::-2] = [-1, -3, -5]
print(x)
print(x)
[-5, 2, -3, 4, -1]

print("\n Хитрая сортировка")
# Хитрая сортировка
# Пусть у нас есть следующий список, в котором элементы -- tuple из строк:
# items = [('one', 'two'), ('three', 'four'), ('five', 'six'), ('string', 'a')]
# Мы хотим отсортировать этот список по последней букве второго элемента каждого tuple, т.е. получить такой список:
# sorted_items = [ ('string', 'a'), ('one', 'two'), ('three', 'four'), ('five', 'six'),]
# Напишите код вместо "<YOUR CODE>" в следующем выражении, чтобы получить верную сортировку.
# sorted_items = sorted(items, key=lambda x: <YOUR CODE>)
# P.S.: в ответе не должно фигурировать слово len .
# В этом задании функция print вам не понадобится. Необходимо лишь заполнить пропуск.
# Напишите программу. Тестируется через stdin → stdout

items = [('one', 'two'), ('three', 'four'), ('five', 'six'), ('string', 'a')]
sorted_items = sorted(items, key=lambda x: x[1][-1])
print(sorted_items)

print("\n Почти двойной факториал")


# Почти двойной факториал
#
# Реализуйте функцию almost_double_factorial(n), вычисляющую произведение всех нечётных натуральных чисел, не превосходящих nn.
# В качестве аргумента ей передаётся натуральное (ноль -- натуральное) число n \leqslant 100n⩽100.
# Возвращаемое значение - вычисленное произведение.
#
# Комментарий. В случае, если n = 0, требуется вернуть 1.
#
# В этом задании функция print вам не понадобится. Результаты выполнения функций нужно возвращать, а не печатать!

def almost_double_factorial(n: int) -> int:
    if n == 0:
        return 1
    res = 1
    for x in range(n + 1):
        if x % 2 == 1:
            res *= x
    return res


res = almost_double_factorial(5)
print(res)
