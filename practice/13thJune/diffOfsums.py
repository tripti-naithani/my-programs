def difference(n):
    sum1 = sumOfsquares(n)
    sum2 = squareOfsum(n)
    diff = abs(sum1 - sum2)
    return diff

def sumOfsquares(n):
    return (n * (n + 1) * (2 * n + 1)) // 6

def squareOfsum(n):
    return pow((n * (n + 1)) // 2 , 2)

n = int(input())
print(difference(n))

