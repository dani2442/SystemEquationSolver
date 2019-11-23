"""
@author: Daniel Lopez Montero

Solve linear system of equations for nxm matrix.
Ax=B
"""
import numpy as np
from practica import resolver,rango,rango_ampliada,discutir

A=np.float64([[1,1,-1],[2,-2,1],[3,-1,0]])
B=np.float64([[1,0,2]])

#Ejemplo 1
"""
#A=np.float64([[1,1,-1],[2,-1,1],[3,-1,0]])
#B=np.float64([[1,0,2]])
"""

#Ejemplo 2
"""
#A=np.float64([[2,-1,1],[1,4,-2][,3,-5,1]])
#B=np.float64([[6,0,4]])
"""

#Ejemplo 3
"""
#A=np.float64([[1,1,2],[3,-1,-2],[-1,2,1]])
#B=np.float64([[0,0,0]])
"""

#Ejemplo 4
"""
#A=np.float64([[1,1,1],[1,-1,0],[1,3,2]])
#B=np.float64([[0,0,0]])
"""

#Ejemplo 5
"""
#A=np.float64([[2,-1,1],[1,4,1],[-1,5,0]])
#B=np.float64([[0,3,3]])
"""

#Ejemplo 6
"""
A=np.float64([[1,1,1],[1,1,1],[1,1,1]])
B=np.float64([[1,1,1]])
"""

#Ejemplo 7
"""
A=np.float64([[0,0,0],[0,0,0],[0,0,0]])
B=np.float64([[0,0,0]])
"""

#Ejemplo 8
"""
A=np.float64([[2,1,0],[-2,1,0],[1,1.5,-2]])
B=np.float64([[-1.5,-1,-2]])
"""


print(rango(A))

print(rango_ampliada(A,B))

print(discutir(A,B))

print(resolver(A,B))