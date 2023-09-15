print("Please enter a number to calculate its factorial")
numb_input = int(input("Enter your number here: "))

first_numb = 1
second_numb = 1

if numb_input <= 0:
    while numb_input <= 0:
        print("Invalid, Try again")
        numb_input = int(input("Enter again: "))
        while second_numb <= numb_input:
            first_numb = second_numb * first_numb
            second_numb += 1
else:
    while second_numb <= numb_input:
        first_numb = second_numb * first_numb
        second_numb += 1

print(f"Your number's factorial is {first_numb}!")

