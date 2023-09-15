"""
#tuples are immuable, cannot change
myTuples = (1,2,3)
print(myTuples[1:])
y = (2,)
print(y)
for i in myTuples:
    print(i)
point = (2,4)
x,y = point
print(point)
print(x)

name,age,ciy = ("Diana", 22, "Espoo")
print(age)
#could also wrie in tuples

grades = (1, 40, 32, 13, 43)
total = 0
for grade in grades:
    total += grade
print(f"here is the total {total}")

mean = total / len(grades)
print(mean)

students = []
students.append(("Diana", (90, 60, 84, 93, 100)))
students.append(("Timo", (30, 32, 64, 34, 66)))
students.append(("Outi", (30, 23, 56, 86, 96)))

print(students)
found = False
for i in students:
    print(i)

for student in students:
    if student[0] == "Diana":
        print(f"the name, {student[0]}")
        print(f"The grades, {student[1]}")
        #print(f"the name, {students[0][0]}")
        #print(f"The grades, {student[0][1]}")

        avg = sum(student[1])/len(student[1])
        print(f"The average of the {student[0]}, is {avg}")

        found = True
        break
    if not found:
        print("Sorry wrong name")

students.append(("Dave", (0, 2, 43, 99, 0)))

# dictionary
dict = {'Name': 'Diana', 'Name': 'Beth', 'Name': 'Crock', 'Salad': 'Tom'}
print(dict['Name'])
del dict['Name']
print(dict)
"""
student = {
    "name": "Diana",
    "grade": "A",
    "course": ["Math", "Physics", "Programming"]
}

print("Name: ", student["name"])
print("Grade: ", student["grade"])
print("Courses: ", student["course"])

student["age"] = 21
print("Age: ", student["age"])

#interacting through the dictionary

for key, value in student.items():
    print(key + " : ", value)#

# check if a key exists in the dictionary

if "age" in student:
    print("age: ", student["age"])
else:
    print("Not in the dictionary")