# -*- coding: utf-8 -*-
"""

Laboratorium z Przetwarzanie multimediów
sem. 2019/2020
Autor: Marcin Wilczewski
"""
# =============================================================================
# 
# 1. http://www.scipy-lectures.org/intro/numpy/array_object.html
# 2. http://www.scipy-lectures.org/intro/matplotlib/index.html
# 3. ftp://ftp.cea.fr/pub/unati/people/educhesnay/pystatml/StatisticsMachineLearningPythonDraft.pdf
# 
# =============================================================================

import numpy as np
import matplotlib.pyplot as plt


# Zadanie 1
# Narysuj wykres funkcji sin(x) oraz sin(x) + epsilon(x), gdzie epsilon(x) jest liczbą losową (rozkład jednostajny)
# z przedzialu 0..0.1
# Uwaga: skorzystaj z numpy.random.rand
def random_gen(shape=1, low=0., high=0.1):
    return (np.random.rand(shape) * (high - low) + low)[0]

def sin_eps(x):
    return np.sin(x) + random_gen()


def graph_ex1():
    x = np.arange(0, 5 * np.pi, 0.1)
    y = np.sin(x)
    plt.plot(x, y)
    plt.show()

    y1 = sin_eps(x)
    plt.plot(x, y1)
    plt.show()


# Zadanie 2
# Przeprowadź 10..10000 z krokiem 10 eksperymentow rzutu kostką szescienna (wybor liczby losowej z przedzialu 1..6).
# W kazdym eksperymencie okresl czestosc (pdp) wyrzucenia okreslonej liczby oczek, np. "1".
# Czestosc w funkcji liczby oczek nanies na wykres.

def throw_dice(size: int):
    return np.random.randint(low=1, high=7, size=size)


def conduct_experiment(low: int = 10, high: int = 10000, step: int = 10):
    pdps = []
    num_iterations = []
    for iteration in range(low, high, step):
        # print(iteration)
        num_iterations.append(iteration)
        exp = throw_dice(iteration)
        # print(exp)
        pdp = []
        for i in range(1, 7, 1):
            pdp.append(exp.count(i) / iteration)
        pdps.append(pdp)
    # print(pdps)
    # print(num_iterations)

    count = np.zeros(6)
    for exp in pdps:
        print(f"Adding {exp}: count now: {count}")
        count = np.add(count, exp)

    dots = [1, 2, 3, 4, 5, 6]

    plt.bar(dots, height=count)
    plt.ylabel("PDP")
    plt.xlabel("Dice dot")
    plt.title(f"Probability in getting Dice dots for {high} iterations")
    plt.show()

    # print(count)


# Zadanie 3
# Utworz wektor 1000 liczb losowych z przedzialu 1..100, a nastepnie oblicz niezaleznie liczbę elementów parzystych i nieparzystych

def odd_and_even(low: int = 1, high: int = 100, size: int = 1000):
    numbers = np.random.randint(low=low, high=high, size=1000)
    even = [i for i in numbers if i % 2 == 0]
    odd = [i for i in numbers if i % 2 != 0]
    print(f"Numbers: {numbers}")
    print(f"Odd: {odd}")
    print(f"Even: {even}")


# Zadanie 4
# Utworz macierz 5x5 liczb losowych z przedzialu 0..9.
# a nastepnie stworz nowa macierz, w ktorej elmenty parzyste wyjsciowej macierzy zastap 1, a nieparzyste 0

def matrix_creator(size: int = 5):
    matrix = np.matrix(np.random.randint(low=0, high=9, size=(size, size)))

    print(matrix)

    matrix_copy = matrix.copy()

    for i in range(size):
        for j in range(size):
            if matrix_copy[i, j] % 2 == 0:
                matrix_copy[i, j] = 1
            else:
                matrix_copy[i, j] = 0

    print(matrix_copy)


# Zadanie 5
# Utworz macierz 10x10 liczb losowych z przedzialu 0..9,
# a nastepnie skrajne podmacierze 3x3 (gorny lewy rog, gorny prawy rog, itd) zastap macierzą 1

def change_matrxi(size: int = 10):
    matrix = np.matrix(np.random.randint(low=0, high=9, size=(size, size)))
    # Nie wiem jak zrobić to zadanie ?!


# Zadanie 6
# Wygeneruj dwa wektory liczb losowych. Następnie wyznacz ich sumę oraz iloczyn skalarny.

def vector_operations():
    vec1 = np.random.randint(low=0, high=100, size=10)
    vec2 = np.random.randint(low=0, high=100, size=10)

    sum1 = np.sum(vec1)
    sum2 = np.sum(vec2)
    inner = np.inner(vec1, vec2)

    print(vec1)
    print(vec2)
    print(sum1)
    print(sum2)
    print(inner)


vector_operations()

if __name__ == '__main__':
    # EX1
    print("EX1")
    graph_ex1()

    # EX2
    print("EX2")
    conduct_experiment()

    # EX3
    print("EX3")
    odd_and_even()

    # EX4
    print("EX4")
    matrix_creator()

    # EX6
    print("EX6")
    vector_operations()