import numpy as np

print("Сжатие")


def encode(a):
    el_num = []
    el_cnt = []
    cnt = 1
    for i in range(len(a)):
        if i < len(a) - 1 and a[i] == a[i + 1]:
            cnt += 1
            continue
        else:
            el_num.append(a[i])
            el_cnt.append(cnt)
            cnt = 1
    return np.array(el_num), np.array(el_cnt)


a = np.array([1, 2, 2, 2, 3, 3, 1, 1, 1, 5, 5, 2, 3, 3, 3, 3])
print(encode(a))

print("Склеивание")


def transform(X, a=1):
    """
    param X: np.array[batch_size, n]
    """
    result = []
    for row in X:
        new_row = [a if i % 2 != 0 else row[i] ** 3 for i in range(len(row))][::-1]
        new_row = np.hstack([row, new_row])
        result.append(new_row)
    return np.array(result)


z = np.array([[1, 2, 3, 4, 5]])

a = np.array([[100, 200, 300, 400, 500]])
b = np.array([[1, 2, 3], [7, 5, 3], [21, 3, 4]])
c = np.array([[6, 0, 2], [4, 2, 0], [-1, 2, 3]])

print(transform(z, -100))
print(transform(a, 2))
print(transform(b, 3))
print(transform(c, -1))

print("Накопительная сумма")


def cumsum(A):
    # param A: np.array[m,n]
    result = np.array([np.cumsum(x) for x in A])
    return result


a = np.array([[1, 2, 3], [7, 5, 3], [21, 3, 4]])
b = np.array([[6, 0, 2], [4, 2, 0], [-1, 2, 3]])
cumsum(a)
cumsum(b)

print("Сумма четных на главной диаоганали")


def diag_2k(a):
    # param a: np.array[size, size]
    diag_a = np.diagonal(a)
    return diag_a[diag_a % 2 == 0].sum()


a = np.array([[1, 2, 3], [7, 5, 3], [21, 3, 4]])
b = np.array([[6, 0, 2], [4, 2, 0], [-1, 2, 3]])

diag_2k(a)
diag_2k(b)

print("скалярное произведение")


def no_numpy_scalar(v1, v2):
    # param v1, v2: lists of 3 ints
    result = 0
    for i in range(len(v1)):
        result += v1[i] * v2[i]
    return result


def numpy_scalar(v1, v2):
    # param v1, v2: np.arrays[3]
    result = v1.dot(v2)
    return result


a = np.array([1, 2, 3])
b = np.array([7, 5, 3])
print(numpy_scalar(a, b))
print(no_numpy_scalar(a, b))

print("Перемножение матриц")

import numpy as np


def no_numpy_mult(first, second):
    """
    param first: list of "size" lists, each contains "size" floats
    param second: list of "size" lists, each contains "size" floats
    """
    size = len(first)
    result = []
    for index_row_a in range(size):
        new_line = []
        for index_col_b in range(size):
            el = 0
            for i in range(size):
                el += first[index_row_a][i] * second[i][index_col_b]
            new_line.append(el)
        result.append(new_line)
    return result


def numpy_mult(first, second):
    """
    param first: np.array[size, size]
    param second: np.array[size, size]
    """
    result = first.dot(second)
    return result


a = np.array([[1, 2, 3], [7, 5, 3], [21, 3, 1]])
b = np.array([[1, 0, 2], [4, 1, 0], [-1, 2, 3]])
print(no_numpy_mult(a, b))
print(numpy_mult(a, b))

print("-" * 30)

a = [1, 2, 3]
b = np.array(a, dtype="str")
b = np.array(a, dtype="float")

print(a, b)

print(np.dtype)
print(b.dtype)

c = np.linspace(10, 32, 12)
print(c[1] - c[0])

print(c)
