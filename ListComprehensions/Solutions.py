# this will create a list of squares from 1(Included) to 11(Excluded)
squares = [x**2 for x in range(1,11)]
print(squares)


# Even numbers
even = [x for x in range(1,21) if x%2==0]
# Second approach using range step paramenter
even = [x for x in range(2,21,2)]
print(even)
odd = [x for x in range(1,21,2)]
print(odd)


# Find lengths of strings
words = ["hello", "world", "python", "list", "comprehension"]
lengthWords = [len(x) for x in words]
print(lengthWords)


# UpperCase the Strings
uppercased = [x.upper() for x in words]
print(uppercased)


# Create a list from 1 to 50 that are divisible by 3 and 5
divisible = [x for x in range(1,51) if x%3==0 and x%5==0]
print(divisible)

# Flatten a list of lists
list_of_lists = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
flattenedList = [x for y in list_of_lists for x in y]
print(flattenedList)


# create a tuple of key:value pair from a dictionary
dict_sample = {"a": 1, "b": 2, "c": 3}
tupleList = [(y,x) for x,y in enumerate(dict_sample)]
# Other Approach
tupleList = [(key,value) for key,value in dict_sample.items()]
print(tupleList)
# Expected Output: [("a", 1), ("b", 2), ("c", 3)]


# List comprehension can comtain nested functions
from math import pi
rounded = [str(round(pi,i)) for i in range(7)]
print(rounded)


# Generating a 3x3 matrix 
matrix = [[value for _ in range(3)] for value in range(3)]
print(matrix)



# Prime Numbers 
def check_prime(value):
    if value < 2:
        return False
    
    for i in range(2,int(value**0.5)+1):
        if value%i==0:
            return False
    return True

prime = [x for x in range(50) if check_prime(x)==True]
print(prime)


words = ["apple", "banana", "cherry", "date","zaid"]
# Expected Output: ['elppa', 'banana', 'yrrehc', 'date']
reversedWords = [word[::-1] if len(word)%2 != 0 else word for word in words]
# word[::-1] is used to reverse the string 
reversedWords = [word[::-1] if words.index(word)%2==0  else word for word in words]
print(reversedWords)
