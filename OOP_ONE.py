def method_name(a,b):
    print("A method")

class Person:
    def __init__(self,person_name: str,date_of_birth: int,ht :int):
        self.name =person_name
        self.date_of_birth = date_of_birth
        self.height = ht

    def get_year_of_birth(self):
        return self.date_of_birth


    def get_name(self):
        return self.name

    def get_summary(self):
        return f"name: {self.name}, DOB: {self.date_of_birth}, Height: {self.height}"

    def set_name(self,new_name):
        if self.__has_any_number(new_name):
            print("Sorry person name can't have number")

    # def __has_any_number(self,string):
    #     return  "0" in string

class Student(Person):
    def __init__(self,person_name:str,date_of_birth: int,email_id:str,student_id:str):
        super().__init__(person_name,date_of_birth)
        self.id = student_id
        self.email = email_id

    def get_summary(self):
        return f"Name{self.get_name()} Email: {self.email} Birth:{self.date_of_birth()}"

student = Student("A",3000,"a@google.com","123435435")
print(student.get_summary())
student.set_name("rian")
print(student.get_summary())