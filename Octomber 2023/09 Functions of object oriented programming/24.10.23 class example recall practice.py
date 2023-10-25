class Person:
    def __init__(self, name:str, height:int):
        self.name = name
        self.height = height

    def __str__(self):
        return self.name

class Room:
    def __int__(self):
        self.persons = []

    def add(self, person: Person):
        self.persons.append(person)

    def is_empty(self):
        return(len(self.persons)) == 0

    def print_info(self):
        total_height = 0
        for person in self.person:
            total_height += person.height
        print(f"There are {len(self.persons)}"
              f"persons in the classromm, and their combined height is: "
              f"{total_height} cm")
        for person in self.persons:
            print(f"{person.name} is {person,height} cm")

    def tallest(self):
        tallest_person = None
        height_of_the_tallest = 0
        for person in self.person:
            if tallest_person is None or person.height >= height_of_the_tallest:
                tallest_person = person
                height_of_the_tallest = person.height

        return  tallest_person

    def remove_tallest(self):
        tallest_person = self.tallest()
        if tallest_person:
            seld.persons.remove(tallest_person)

        return tallest_person

room = Room()

print("is this room empty? ", room.is_empty())
print("The tallest person is: ", room.tallest())

room.add(Person("Lihini", 160))
room.add(Person("Anatolii", 178))
room.add(Person("Ricardo", 180))
room.add(Person("Nhi", 160))
room.add(Person("Manoor", 177))

room.print_info()
remove = room.remove_tallest(self)
print(f"Remove from the room this tallest person: {removed.name}")