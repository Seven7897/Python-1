x = int(input("Ввведите точку по x : "))
y = int(input("Ввведите точку по y : "))
if x > 0 and y > 0 :
    print("Первая четверть")
if x < 0 and y > 0 :
    print("Вторая четверть")
if x < 0 and y < 0 :
    print("Третья четверть")
if x > 0 and y < 0 :
    print("Четвертая четверть")
