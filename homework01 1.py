day =  int (input ("Введите день недели :  90"))
if day > 0 and day < 8 :
    if day > 5 :
        print('Выходной день') 
    else :
        print('Будний день') 
else :
    print(f"число {day} не является днем недели")