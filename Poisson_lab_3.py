import math
import os
Menu=""""
Menu
1 : Normal
2 : Mayor a X
3 : Mayor a Lambda
4 : Menor a X
5 : Menor a Lambda
"""
pop = True
while pop == True:
    print(Menu)
    Option = int(input("Seleccione una opcion: "))
    if Option is 1:
        print ("distribucion: ")
        print ("Ingrese Lambda: ")
        Lambda_ = int(input())
        print ("Ingrese K = X: ")
        Equis = int(input())
        F = (2.7182**-Lambda_)*(Lambda_**Equis)
        F2 = (math.factorial(Equis))
        Fr = (F/F2)*100
        print ("Resultado porcentual: ", Fr, "%")
        os.system("Pause")
        os.system("cls")
    elif Option is 2:
        print ("distribucion: Mayor a X ")
        print ("Ingrese Lambda: ")
        Lambda_ = int(input())
        print ("Ingrese K = X: ")
        Equis = int(input())
        for i in range (Equis+1, Lambda_+1):
            print("Valor de X: ", i)
            F = (2.7182**-Lambda_)*(Lambda_**i)
            F2 = (math.factorial(i))
            Fr = (F/F2)
            Rf = Fr+Fr
        print ("Resultado Porcentual:", (Rf*100),"%")
        os.system("Pause")
        os.system("cls")
    elif Option is 3:
        print ("distribucion: Mayor a Lambda ")
        print ("Ingrese Lambda: ")
        Lambda_ = int(input())
        max = int(input("ingrese valor maximo: "))
        for i in range (Lambda_+1, max+1):
            print("Valor de X: ", i)
            F = (2.7182**-Lambda_)*(Lambda_**i)
            F2 = (math.factorial(i))
            Fr = (F/F2)
            Rf = Fr+Fr
        print ("Resultado Porcentual:", (Rf*100),"%")
        os.system("Pause")
        os.system("cls")
    elif Option is 4:
        print ("distribucion: Menor a X")
        print ("Ingrese Lambda: ")
        Lambda_ = int(input())
        print ("Ingrese K = X: ")
        Equis = int(input())
        min = int(input("ingrese valor minimo: "))
        for i in range (min, Equis):
            print("Valor de X: ", i)
            F = (2.7182**-Lambda_)*(Lambda_**i)
            F2 = (math.factorial(i))
            Fr = (F/F2)
            Rf = Fr+Fr
        print ("Resultado Porcentual:", (Rf*100),"%")
        os.system("Pause")
        os.system("cls")
    elif Option is 5:
        print ("distribucion: menor a Lambda")
        print ("Ingrese Lambda: ")
        Lambda_ = int(input())
        print ("Ingrese K = X: ")
        Equis = int(input())
        min = int(input("ingrese valor minimo: "))
        for i in range (min, Lambda_):
            print("Valor de X: ", i)
            F = (2.7182**-Lambda_)*(Lambda_**i)
            F2 = (math.factorial(i))
            Fr = (F/F2)
            Rf = Fr+Fr
        print ("Resultado Porcentual:", (Rf*100),"%")
        os.system("Pause")
        os.system("cls")
