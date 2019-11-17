# Методом перестановок упорядочить по убыванию массив, содержащий 12 целых чисел
import random


def swap(param, param1):
    a = param
    param = param1
    param1 = a
    return param, param1


mass = []
random.seed(5)
for i in range(12):
    mass.append(random.randrange(100))
print(mass)
for i in range(11):
    for j in range(11):
        if mass[j] < mass[j + 1]:
            mass[j], mass[j + 1] = swap(mass[j], mass[j + 1])
print(mass)
