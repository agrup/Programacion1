# Una variable es un espacio donde se guradan valores
#ejemplo 1 guardar valores en una

#puedo guardar un string
variable1 = "Lo que guardo en la varible"

#puedo guardar un numero entero
variable2 = 2020

#puedo guardar un numero real
variable3 = 9.45

#puedo guardar el valor de otra variable
variable4 = variable3

#puedoo hacer asignaciones multiples
variable5, variable6 = variable4, variable2


print(variable1)
print(variable2)
print(variable3)
print(variable4)
print(variable5)
print(variable6)

#operaciones con variables

variable7 = 10
variable8 = 20

resultado = variable7 + variable8

print(resultado)

variable9 = "Hola "
variable10 = "Mundo"


saludo = variable9 +variable10
 
print(saludo)

# no podemos usar tipos diferentes

variable11 = "10"
variable12 = 20

#error = variable11 + variable12

#pero podemos castear (transformar) a un tipo de valor conocido

resultado = int(variable11) + variable12

