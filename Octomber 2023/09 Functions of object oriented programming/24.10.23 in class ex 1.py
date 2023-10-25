class Vissitor:
    def __int__(self, name: str, height: int):
        self.name = name
        self.height = height

class Attractions:
    def __int__(self, name:str, minimum_height:int):
        self. visitor_list = []
        self.name = name
        self.minimum_height = minimim_height

    def sef_check_height(self, person:Visitor):
        if person.height >= self.mimimum_height:
            self.visitor_list.append(person)
            print(f"{person.name} is eligible")

        else:
            print(f"{person.name} is too short to enter :(")

    def __str__(self):
        for person in self.visitor_list:
            print(person.name)
        return f"{self.name} has now {len(self.visitor_list)} visitors"

roller_coaster = Attractions("Roller coaster", 120)
Jiayue = Visitor("Jiayue", 165)
Juho = Visitor("Juho", 186)
Melika = Visitor("Melika", 169)
Chau = Visittor("Chau", 69)

roller_coaster.check_height(Jiayue)
roller_coaster.check_height(Juho)
roller_coaster.check_height(Melika)
roller_coaster.check_height(Chau)

print(roller_coaster)
