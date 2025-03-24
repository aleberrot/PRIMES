import time
import random
from math import isqrt

numeros = [random.randint(1000, 9999) for i in range(15) ]
numeros2 = [i for i in range(1, 101)]

# creates an array of 15 random integers between 1000 and 9999 using list comprehension

def primos(num):
    divisores = []
    for i in range(1, num + 1):
            divisores.append(i)
    print(divisores)

#first_interval = time.time()
#first_interval_end = time.time()
#print(f'Passed {first_interval_end - first_interval} seconds')

def primos_mitad(num):
    divisores = []
    for i in range(1, round(num/2)+ 1):
        if num % i == 0:
            divisores.append(i)
    return f'{num} es primo' if len(divisores) < 2 else f'{num} NO es primo'
    #return [num, divisores]

#second_interval = time.time()
#result = list(map(primos_mitad, numeros2))
#second_interval_end = time.time()

#print(result)
#print(f'La operacion se realizo en  {second_interval_end - second_interval} segundos')


def primos_criba(num):
    if num <= 2:
        return []
    primes = [True] * num
    primes[0] = primes[1] = False
    for i in range(2, isqrt(num)):
        if primes[i]:
            for x in range(i*i, num, i):
                primes[x] = False
    print([i for i in range(num) if primes[i]])

primos_criba(999)
