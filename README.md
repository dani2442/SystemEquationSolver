# SystemEquationSolver
This project pretends to solve a linear system of equation.
It uses Numpy library and it is fully developed in python.

## Getting Started
You will find a test.py file which ilustrates the different functions implemented.

### Functions
- Rank of coefficient matrix (A)
- Rank of coefficient matrix concatenated with constant matrix (A|B)
- Category of the system of equations (one solution multiple or non-existence solution)
- Solver (Ax=b)

### Example Code
```python
import numpy as np
from practica import resolver,rango,rango_ampliada,discutir

A=np.float64([[1,1,-1],[2,-2,1],[3,-1,0]])
B=np.float64([[1,0,2]])

print(rango(A))

print(rango_ampliada(A,B))

print(discutir(A,B))

print(resolver(A,B))
```
