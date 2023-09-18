#first function is print, one of the many built in functions
print("Good morning")
#you can get the good morning to be on separet lines by making 2 functions:
print("Good")
print("morning")
#or by using \n in the middle:
print("Good\nmorning")

#user inputs (you can call them anything), another of the many built in functions
user = input("Enter your name: ")
print("Nice to meet you, " + user + "!")
#or another way to write it is (simpler in my opinion)
print(f"Nice to meet you {user}!")
# the 'user' (in this case) is a variable (just like in math) that can then be used in the code.
# the = here means that we assigned the input from the user, the name user (like x=5)

# if we only want to print the user:
print(user)
# u only need "" if it is a string (like a word or a sentance, everything that is not esplicitly defined in the code is automatically a string)

#types of variables:
#string
#number (interger or int in code, long(unlimited int), float or complex)
    #an int can store numbers between -2147483648 to 2147483647 including end points
        #u can use an _ to make he number more readable
            #(12_345_678_900 will be printed out as 12345678900)
    #comands for imaginary numbers are

        numb = 4 + 3j
        print(numb.real)
        print(numb.imag
#boolean (if it's true or false)
#list, tuple or dictionary

#matematical operations
        # Addition +, subtraction -, multiplication *, division /
        # Remainder %, floor division // (rounds the result down to the nearest whole number, the whole number part of the result), exponention operator **

#output formatting
        print(f"The temperature in Celsius: {celcius:6.2f}")
        # in celcius:6.2f
                #6 means 6 characters ong
                #.2 means 2 decimal points
                # f means float
        # other options include: <20s (string printed in a field of 20 characters, to the left)
                # and 8d (intiger in a field of 8 chracters wide)
import math
n = 12
while n > 0:
        print(f"{'Pi':{n}s}:{math.pi:10.5f}")
        n= n-1
        # the n was 12 in the example,  it means how many characters wide the space is.
        # the 10.5f, pi will have 5 decimals but the whole this is in a 10 character wide space, meaning there will be 3 empty spaces since the decimal point is one and the 3 (whole number of pi) is another
                #math.pi is for importing pi and math.e is for e
