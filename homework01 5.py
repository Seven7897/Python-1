import math
Xa = int(input("Введите координаты первой точки по Х : "))
Ya = int(input("Введите координаты первой точки по y : "))
Xb = int(input("Введите координаты второй точки по Х : "))
Yb = int(input("Введите координаты второй точки по y : "))
AB = math.sqrt((Xb - Xa)**2 + (Yb - Ya)**2) 
print(round(AB, 3))
