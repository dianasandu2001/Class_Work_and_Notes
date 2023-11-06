class People:
    def __init__(self, first_name, last_name, occupation, birth_date):
        self.first_name = first_name
        self.last_name = last_name
        self.occupation = occupation
        self.birth_date = birth_date

    def job_status(self):
        return self.occupation

    def set_job(self, new_job):
        self.occupation = new_job

    def print_details(self):
        print(self)

class Student(People):
    def __init__(self, first_name, last_name, occupation, birth_date, major):
        super().__init__(first_name, last_name, occupation, birth_date)
        self.major = major
        self.courses = []

    def add_course(self, course):
        self.courses.append(course)

class Teacher(People):

    def __init__(self, first_name, last_name, occupation, birth_date):
        

person1 = Student("Diana", "Sandu", "Potential Game Dev", "09.08.2001", "Game development")
person1.print_details()