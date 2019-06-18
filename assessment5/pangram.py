#1
from string import ascii_lowercase as al

def ispangram(string):
    return set(al) - set(string.lower()) == set([]) #comparing the difference with empty set
       
string = input()
print(ispangram(string))


#2
consonant = "bcdfghjklmnpqrstvwxyz"
vowel = "aeiou"

def compute_impurity_index(string):
    string = (string.strip()).lower()
    length = len(string)

    if (length == 26):
        impurity_index = 0
    else:
        impurity_index = add2impurity(string, length)
        
    return impurity_index

def add2impurity(string, length):
    add  = 0
    for i in range(length):
        if string.count(string[i]) == 2 and string[i] in vowel:
            add += 0.5
        elif string.count(string[i]) == 2 and string[i] in consonant:
            add += 0.7
        else:
            add = count_more_than2(string, string[i], add )
    return add

def count_more_than2(string, string[i], add):
    count =  string.count(string[i])
    if (count == 3):
        return add + 1
    else:
        return add + 3
   
    
string = input()
compute_impurity_index(string)




