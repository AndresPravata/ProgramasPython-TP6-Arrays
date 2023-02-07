#Ejercicio 5

import numpy as np
i=1
nros =[]

for i in range (6):
    num = int(input ("Ingrese 6 números: "))
    nros.append (num)
    
v=np.array (nros)

print(v)
