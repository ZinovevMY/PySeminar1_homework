# Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.
import math
from decimal import Decimal, ROUND_FLOOR

point1_x = int(input("Введите координату X первой точки: "))
point1_y = int(input("Введите координату Y первой точки: "))
point2_x = int(input("Введите координату X второй точки: "))
point2_y = int(input("Введите координату Y второй точки: "))

distance = Decimal(str(math.sqrt((point2_x - point1_x) ** 2 + (point2_y - point1_y) ** 2)))
print(f"Расстояние между точками с координатами ({point1_x}, {point1_y}) и ({point2_x}, {point2_y}) "
      f"равно {distance.quantize(Decimal('1.00'), ROUND_FLOOR)}")
