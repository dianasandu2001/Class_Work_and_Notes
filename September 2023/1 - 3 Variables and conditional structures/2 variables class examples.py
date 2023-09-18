"""
#1 input and typ casting example
num1 = input("Enter the first Number: ")
num2 = input("Enter the second Number: ")
num3 = num1 + num2
print(type(num3))
print("The result is\n", num3)

num1 = int(input("Enter the first Number: "))
num2 = int(input("Enter the second Number: "))
num3 = num1 + num2
print(type(num3))
print("The result is\n", num3)
"""
#2 output formatting
name = "Timo"
age = 25
print("Name:", name, "Age:", age)

name = "Charlie"
age = 22
output = "Name: {} Age: {}".format(name, age)
print(output)
    #you can also print("Name: {} Age: {}".format(name, age)) instead of having it on a separete line

name = "David"
age = 28
output = f"Name: {name} Age: {age}"
print(output)
    #you can also print(f"Name: {name} Age: {age}") instead of having it on a separete line

pi = 3.14159265359
formatted_pi = f"Value of pi: {pi:.14f}"
print(formatted_pi)

pi = 3.14159265359
formatted_pi2 = "Valie of pi: {:.2f}".format(pi) #Display 2 decimal points
print(formatted_pi2)
