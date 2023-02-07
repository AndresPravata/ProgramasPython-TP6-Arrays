#Ejercicio 6

import random

import numpy as np

i=1

v=np.random.randint (6,size=(16))
   
print(v)

for i in range (16):
    if v[i] == 0:
        v[i]=-1
        
print(v)      