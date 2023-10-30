#Outcome:
#
#Trung is enrolled in courses: ['Mathematics', 'Physics']
#Amir is enrolled in courses: ['Physics']
#Time is enrolled in courses: ['Mathematics', 'History']
#Mathematics has the following students: ['Trung', 'Timo']
#Physics has the following students: ['Trung', 'Amir']
#History has the following students: ['Timo']

class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.courses = []

    def enroll(self, course):
        self.courses.append(course)

    def list_courses(self):
        return[course.name for course in self.courses]

class Course:

    def __init__(self, course_id, name):
        self.course_id = course_id
        self.name = name
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def list_students(self):
        return[student.name for student in self.students]

student1 = Student(1, "Trung")
student2 = Student(2, "Amir")
student3 = Student(3, "Timo")

course1 = Course(101, "Mathematics")
course2 = Course(102, "Physics")
course3 = Course(103, "History")

student1.enroll(course1)
student1.enroll(course2)
student2.enroll(course2)
student3.enroll(course1)
student3.enroll(course3)

course1.add_student(student1)
course1.add_student(student3)
course2.add_student(student1)
course2.add_student(student2)
course3.add_student(student3)

print(f"{student1.name} is enrolled in courses: {student1.list_courses()}")
print(f"{student2.name} is enrolled in courses: {student2.list_courses()}")
print(f"{student3.name} is enrolled in courses: {student3.list_courses()}")

print(f"{course1.name} has the following students: {course1.list_students()}")
print(f"{course2.name} has the following students: {course2.list_students()}")
print(f"{course3.name} has the following students: {course3.list_students()}")