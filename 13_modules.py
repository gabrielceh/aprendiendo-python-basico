# Modules

import my_module # modulo propio
from my_module import subtract_two_number
from my_module import multiply_two_number as multiply, divide_two_number

import math # modulo del sistema
from math import pi



print(my_module)
print(f"Suma 3 + 6: {my_module.add_two_number(3,6)}")
print(f"Resta 3 - 6: {subtract_two_number(3,6)}")
print(f"Multiplicar 3 x 6: {multiply(3,6)}")
print(f"Dividir 6 x 3: {divide_two_number(6,3)}")


print(math.pow(2,3))
print(pi)
