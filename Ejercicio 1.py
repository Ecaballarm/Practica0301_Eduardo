# Escribir dos funciones, una función que reciba un número entero positivo n y calcule el número de fibonacci asociado
# a ese número de manera recursiva y otra función que haga la misma operación pero con bucles.
# Con ambas funciones, calcular y comparar el tiempo de ejecución para n = (1, 10, 20, 30 y 40) por fuerza bruta.

import datetime
def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n-1) + fib(n-2)


start_time = datetime.datetime.now()
fib(40)
end_time = datetime.datetime.now()
print("El tiempo de ejecución es: ", end_time - start_time)
