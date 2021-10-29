#Public key encryption relies on certain really large numbers being computationally hard to factor to keep data
#secure. 

#For this challenge, we'll factor some numbers that are a little easier to deal with. 

#Your goal is to write a python function to find the prime factorization of a given number.
#It should take an integer value as the input and then return a list containing all of its prime factors. 

#For example calling the function with an input of 630 should return a list containing the values:
#two, three, three, five and seven.
#Those are prime numbers and if you multiply them together, the product is 630. 

#Calling your function on a prime number like 13, should return a list with just a single value, that prime number.

#Prime numbers: 2, 3, 5, 7, 11, 13, 17...

def get_prime_prime_factors(N):
    factors = list()
    divisor = 2
    while(divisor <= N):
        if (N % divisor) == 0:
            factors.append(divisor)
            N = N/divisor
        else:
            divisor += 1
    print(factors)    
N = int(input("Ingrese un numero entero: "))
get_prime_prime_factors(N)

#My solution:
primos = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53]
n = int(input("Ingrese un numero entero para obtener la lista de primos: "))
i = 0
fprimo = list()
x = int(primos[i])  
while(x <= n):
    if (n % x) == 0:
        fprimo.append(x)
        n = n/x
    else:
        i = i+1
    x = int(primos[i])
print("La lista de numeros primos del numero ingresado es: ",fprimo)

