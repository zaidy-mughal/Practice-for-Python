# this will create a list of squares from 1(Included) to 11(Excluded)
squares = [x**2 for x in range(1,11)]
print(squares)


# Even numbers
even = [x for x in range(1,21) if x%2==0]
# Second approach using range step paramenter
# even = [x for x in range(2,21,2)]
print(even)
odd = [x for x in range(1,21,2)]
print(odd)

