#Ejercicio 14

import numpy as np

m=np.random.randint (9,size=(6,6))

print(m)

for f in range (6):
    for c in range (6):
        m[f,c]=0
        if f==c:
            m[f,c]=1
print(m)