import sympy

def primeNo_10001st():
    prime_list = [num for num in range(2, 120000) if sympy.isprime(num)]
    return prime_list[10000]

print(primeNo_10001st())
