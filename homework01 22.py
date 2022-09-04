x = int(input("x "))
y = int(input("y "))
z = int(input("z "))
if not(x or y or z) == (not x and not y and not z) :
    print("Правдв")
else:
    print("Ложь")
