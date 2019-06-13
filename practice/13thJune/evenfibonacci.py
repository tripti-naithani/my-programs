def generate_fibonacci(limit):
    prev1 = 1
    prev2 = 2
    curr = 0
    fibonacci = [1, 2]
    while (1):
        curr, prev1, prev2 = calculate_previous(curr, prev1, prev2)
        if(curr < limit):
            fibonacci.append(curr)
        else:
            break         
    return fibonacci

def calculate_previous(curr, prev1, prev2):
    curr = prev1 + prev2
    prev1 = prev2
    prev2 = curr
    return curr, prev1, prev2
        
def sumOf_evenFibonacci(fibonacci_seq):
    return sum([number for number in fibonacci if number % 2 == 0])

fibonacci = generate_fibonacci(4000000)
print(sumOf_evenFibonacci(fibonacci))
