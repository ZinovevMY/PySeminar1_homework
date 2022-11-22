# Напишите программу,которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).

range_num = int(input("Введите номер четверти: "))
if range_num < 1 or range_num > 4:
    print("Нет такой четверти!")
else:
    if range_num == 1:
        print("Возможные координаты x > 0 и y > 0")
    elif range_num == 2:
        print("Возможные координаты x < 0 и y > 0")
    elif range_num == 3:
        print("Возможные координаты x < 0 и y < 0")
    else:
        print("Возможные координаты x > 0 и y < 0")
