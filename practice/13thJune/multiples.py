def sum_of_multiples(num1, num2, limit):
    multiples = []
    for i in range(1, limit):
        if (i % num1 == 0 or i % num2 == 0 ):
            multiples.append(i)
    return sum(multiples)

num1 = int(input())
num2 = int(input())
limit = int(input())
print(sum_of_multiples(num1, num2, limit))

