# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z
# для всех значений предикат.

var_x = input("X->")
var_y = input("Y->")
var_z = input("Z->")
left_expression = not (var_x or var_y or var_z)
right_expression = not var_x and not var_y and not var_z
if left_expression == right_expression:
    print("Утверждение ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z истинно!")
else:
    print("Утверждение ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z ложно!")
