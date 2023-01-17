from os import system
from math import sqrt


system('cls')

class Point:
    def __init__(self,x_init,y_init):
        self.x = x_init
        self.y = y_init

    def __str__(self):
        return "".join(["Point(", str(self.x), ", ", str(self.y), ")"])


def distance(A, B):
    return sqrt( (A.x - B.x) ** 2 + (A.y - B.y) ** 2 )


print("\nПрограмма принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.\n")

A_x = int(input('Введите координату точки А по оси Х: '))
A_y = int(input('Введите координату точки А по оси Y: '))
B_x = int(input('Введите координату точки B по оси Х: '))
B_y = int(input('Введите координату точки B по оси Y: '))

A, B = Point(A_x, A_y), Point(B_x, B_y)
print(f"\nРасстояние между: {A}; {B} -> {int(distance(A,B) * 100) / 100}\n")
