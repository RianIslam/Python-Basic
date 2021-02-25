def method_name(a,b):
    print("A method")

class Person:
    def __init__(self,person_name,date_of_birth,ht):
        self.name =person_name
        self.date_of_birth = date_of_birth
        self.height = ht



    def get_name(self):
        return self.name

    def get_summary(self):
        return f"name: {self.name}, DOB: {self.date_of_birth}, Height: {self.height}"

method_name(23,45)

a_person = Person("Rian Islam", "1009", "6 feet")


print(a_person.get_summary())
