

#Example he gave of exercise 2
scores = []
while True:
    grade = input("Enter your grades, done to terminate")
    if grade == 'done':
        break

    scores.append(grade)
print("\n score")
for index, item in enumerate(scores, start=1):
    print(f"{}")