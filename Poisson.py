import math
print ("Ingrese tiempo")
Tr = float(input())
c = 0.2
Tiempo = 3
print ("Cantidad")
Ca = float(input())

if(Tr == Tiempo):
    Cr = Tr*c
    print("iniciando")
    print("Cantidad de imperfeccion: ", Cr)
    P0= (Cr**Ca)*(2.7182**-Cr)
    print(pow(Cr,Ca))
    P1= (math.factorial(Ca))
    P2= (P0/P1)
    print("Resultado ",P2)
else:
    Cr = Tr*c
    print("Cantidad de imperfecciones: ", Cr)
    P0=(Cr**0)*(2.7182**-Cr)
    P1=(math.factorial(0))
    P2=(P0/P1)
    
    P01=(Cr**0)*(2.7182**-Cr)
    P11=(math.factorial(1))
    P21=(P01/P11)
    
    Pr= 1-(P2+P21)
    print(Pr)

