import sympy

def all_factors(number):
    return [i for i in range(1, number + 1) if number % i == 0]

def max_primefactor(factors):
    return max([num for num in factors if sympy.isprime(num)])
    
   
factors = all_factors(13195)
print(max_primefactor(factors))

