def method_name(a,b):
    print("A method")

class Person:
    def __init__(self,person_name):
        self.name =person_name


    def get_name(self):
        return self.name



method_name(23,45)

a_person = Person("Rian Islam")
b_person = Person("Islam")


print(a_person.get_name())
print(b_person.get_name())