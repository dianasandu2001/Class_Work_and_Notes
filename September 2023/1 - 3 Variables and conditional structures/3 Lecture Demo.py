x = int(input("give a num"))
if x >= 10:
    print(x, " is a greater than 10 ")
else:
    print(x, " is a smaller than 10")

# Comparison operators
x = 10
y = 12
# Output: x > y is False
print('x > y  is', x > y)
# Output: x < y is True
print('x < y  is', x < y)
# Output: x == y is False
print('x == y is', x == y)
# Output: x != y is True
print('x != y is', x != y)
# Output: x >= y is False
print('x >= y is', x >= y)
# Output: x <= y is True
print('x <= y is', x <= y)

# Arithmetic operators
x = 15
y = 4
# Output: x + y = 19
print('x + y =', x + y)
# Output: x - y = 11
print('x - y =', x - y)
# Output: x * y = 60
print('x * y =', x * y)
# Output: x / y = 3.75
print('x / y =', x / y)
# Output: x // y = 3
print('x // y =', x // y)
# Output: x ** y = 50625
print('x ** y =', x ** y)


# Logical operators
x = True
y = False
# Output: x and y is False
print('x and y is',x and y)
# Output: x or y is True
print('x or y is',x or y)
# Output: not x is False
print('not x is',not x)

i = -7
if i==0:
    if(i>0):
        print("number is possitive")
    else:
        print("number is 0")
else:
    print("number is negative")