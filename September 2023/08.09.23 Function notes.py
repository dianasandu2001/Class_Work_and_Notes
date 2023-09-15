#example 1
def greet(name): #define the funtion, name is the parametor
    print("Hi, soon i am going to be free", name) #body
    return

greet("Diana") #diana is an argument

#example 2
def greet(times):
    for i in range(times):
        print("i am super person!" + str(i+1) + " times")

greet(2)

#example 3
def greet(name, times):
    for i in range(times):
        print(name + " " + "You are super person!" + str(i+1) + " " + " times")
greet("blop", 5)

#example 4
def groccery(items):
    for item in items:
        print("- " + item)

shopping_list = ["cheese", "pasta", "fish"]
groccery(shopping_list)
shopping_list.append("icecream")
groccery(shopping_list)

def calculation(a, b):
    addition = a + b
    return addition

num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
addition = calculation(num1, num2)
print("The sum of your function is: ", addition)


