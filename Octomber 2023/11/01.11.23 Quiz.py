class Students:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.courses = []

    def print_info(self):
        print(f"Student I: {self.id}")
        print(f"Student name: {self.name}")
        print("Enrollments: ")
        for course in self.courses:
            print(f"Course: {course.name}")
            print(f"Course Code: {course.id}")
            print(f"Progress: {course.prog}")
            print(f"Instructor: {course.teach}")

class Course:
    def __init__(self, code, name, prog, teach):
        self.code = code
        self.name = name
        self.prog = prog
        self.teach = teach
        self.students = []

    def enroll(self):
        Students
    def update(self):

