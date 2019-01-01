import numpy as np


# Сигмоида
def nonlin(x, deriv=False):
    if deriv:
        return x*(1-x)
    return 1/(1+np.exp(-x))


# набор входных данных
X = np.array([[0, 0, 1],
              [0, 1, 1],
              [1, 0, 1],
              [1, 1, 1]])

# выходные данные
y = np.array([[0, 0, 1, 1]]).T

# сделаем случайные числа более определёнными
np.random.seed(42)

# инициализируем веса случайным образом со средним 0
syn0 = 2*np.random.random((3, 5)) - 1
syn1 = 2*np.random.random((5, 7)) - 1
syn2 = 2*np.random.random((7, 1)) - 1

for i in range(60000):
    # прямое распространение
    l0 = X
    l1 = nonlin(np.dot(l0, syn0))
    l2 = nonlin(np.dot(l1, syn1))
    l3 = nonlin(np.dot(l2, syn2))

    # как сильно мы ошиблись относительно нужной величины?
    l3_error = y - l3

    if (i % 10000) == 0:
        print('Error:', str(np.mean(np.abs(l3_error))))

    # в какую сторону нужно двигаться?
    # если мы были уверены в предсказании, то сильно менять его не надо
    l3_delta = l3_error * nonlin(l3, deriv=True)

    # как сильно значения l2 влияют на ошибки в l3?
    l2_error = l3_delta.dot(syn2.T)
    l2_delta = l2_error * nonlin(l2, deriv=True)

    # как сильно значения l1 влияют на ошибки в l2?
    l1_error = l2_delta.dot(syn1.T)

    # в каком направлении нужно двигаться, чтобы прийти к l1?
    # если мы были уверены в предсказании, то сильно менять его не надо
    l1_delta = l1_error * nonlin(l1, deriv=True)

    syn2 += l2.T.dot(l3_delta)
    syn1 += l1.T.dot(l2_delta)
    syn0 += l0.T.dot(l1_delta)

print('Выходные данные после тренировки')
print(l3)
