from person import Person

class Student(Person):
    def __init__(self, p_name, p_age, p_height, major):
        super().__init__(p_name, p_age, p_height)
        self.major = major
        print("This time it's a Student object")

student1 = Student("Maria", 22, 6, "Computer Science")

print(student1.name)
student1.name = "Anna"
print(student1.name)

print(student1.public_prop)