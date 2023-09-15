#example 1
name = []
name = input("Enter your name: ")
index = 0
while name != "" and index < len(name):
    print(name[index])
    index += 1

#example 2
name = input("Enter your name: ")
for i in name:
    print(i)

#example 3
number = list(range(1, 5))
print(number)

#example 4
for number in range(1, 6, 2):
    print(number)

#example 5
for greet in range(3):
    print("Good morning!")