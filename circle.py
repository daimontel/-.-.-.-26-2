import math
class Circle:
def __init__(self, radius: float):
if radius <= 0:
raise ValueError("Радиус должен быть положительным")
self.radius = radius
def area(self) -> float:
return math.pi * (self.radius ** 2)

import math



total = 0

for n in range(1, 51):

    term = (1.9**(2*n + 1)) / (n**n + 2) * math.sin(n)

    total += term



print(total)



import math



product = 1

for n in range(1, 21):

    numerator = n**2 + math.sin(n**3)**3 + 1

    denominator = n**2 + math.cos(n**2)**2 + math.sin(n)

    product *= numerator / denominator



print(product)
