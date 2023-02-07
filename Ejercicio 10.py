#Ejercicio 10

import random

import numpy as np

f=4
c=1

m=np.random.randint (1,6,size=(5,6))
   
print(m)

for f in range (5):
    for c in range (6):
        if f==4:
            m[f,c]=0

print(m)