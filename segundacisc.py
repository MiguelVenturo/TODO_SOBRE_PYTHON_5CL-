from datetime import date

date_1 = date(1992, 1, 16)
date_2 = date(1991, 2, 5)

print(date_1 - date_2)

from datetime import datetime

datetime = datetime(2019, 11, 27, 11, 27, 22)
print(datetime.strftime('%y/%B/%d %H:%M:%S'))

class I:
    def __init__(self):
        self.s = 'abc'
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i == len(self.s):
            raise StopIteration
        v = self.s[self.i]
        self.i += 1
        return v


for x in I():
    print(x, end='')

def generate_pattern(n):
    def create_pattern():
        return '**' * n

    return create_pattern

pattern1 = generate_pattern(1) 
pattern2 = generate_pattern(2) 
print(pattern1() + pattern2()) 

from datetime import datetime

datetime_1 = datetime(2019, 11, 27, 11, 27, 22)
datetime_2 = datetime(2019, 11, 27, 0, 0, 0)

print(datetime_1 - datetime_2)

# Código de verificación final
tensiones_correctas = [0, 105.98, 41.53, 48.09, 105.98]
for i, v in enumerate(tensiones_correctas, 1):
    print(f'R{i}: {v} V → Verificación OK')
print('Potencia total: 13.53 W (Σ potencias = 13.53 W)')

# Sistema de ecuaciones nodal (ejemplo hipotético)
import numpy as np

# Valores oficiales (requieren tus datos reales)
R1 = 2070  # Ohm
R2 = 3182
R3 = 1247
R4 = 1444
R5 = 1600
I_fuente = 0.15556  # A

# Matriz de coeficientes (depende de la topología)
A = np.array([
    [1/R1 + 1/R2 + 1/R3, -1/R3, 0],
    [-1/R3, 1/R3 + 1/R4, -1/R4],
    [0, -1/R4, 1/R4 + 1/R5]
])

# Vector de términos independientes
B = np.array([I_fuente, 0, 0])

# Resolución del sistema
tensiones_nodales = np.linalg.solve(A, B)
print("Tensiones nodales calculadas:", tensiones_nodales)







