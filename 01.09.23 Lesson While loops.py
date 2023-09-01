
#this is a basic while loop
i = 1
while i < 11:
    print(i)
    i = i + 1

#this loop asks how many greetings and counts them
greetings = int(input("How many greetings do you want to display?"))
count_greeting = 0
while count_greeting < greetings:
    print("Good morning!")
    count_greeting += 1
    # count_greeting = count_greeting + 1 (this is the same as the line above)

#this asks what to do next and only stops when the user tells the program to stop
command = input("Tell me what to do?")
while command != "stop":
    print(f"Executing your command: {command}")
    command = input("Tell me what to do next:")
print("Execution is stopped")

#rolling dice until
import random
dice1 = dice2 = roll_numb = 0
while (dice1 !=6 or dice2 !=6):
    dice1 = random.randint (1,6)
    dice2 = random.randint (1,6)
    roll_numb += 1
print(f"The dice were rolled {roll_numb} times.")

#learning how to put breaks so the loop doesn't crash your pc
command = input("Tell me what to do?")
while command != "stop":
    if command == "MAYDAY":
        break
    print(f"Executing your command: {command}")
    command = input("Tell me what to do next:")
print("Execution is stopped")

first_numb = 1
while first_numb <= 5:
    second_numb = 1
    while second_numb <=5:
        print(f"{first_numb} times {second_numb} is {first_numb * second_numb}")
        second_numb += 1
    first_numb += 1