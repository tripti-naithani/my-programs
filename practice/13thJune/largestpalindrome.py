def ispalindrome(num):
    return num == int(str(num)[::-1])

def largest_palindrome():
    rangee = list(range(999, 99, -1))
    return max([num1 * num2 for num1 in rangee for num2 in rangee if ispalindrome(num1 * num2)])

print(largest_palindrome())
