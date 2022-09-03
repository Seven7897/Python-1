day =  int (input ("Введите день недели :"))
if day > 0 and day < 8 :
    if day > 5 :
        print('Выходной день') 
    else :
        print('Будний день') 
else :
    print('число' + day +  'не является днем недели')