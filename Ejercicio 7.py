#Ejercicio 7

import random

import numpy as np

lista=[]

for i in range (3):

    lista.append([random.randint (0,9)])

v=np.random.randint (9,size=(3))

print (lista + lista)
   
print(v + v)