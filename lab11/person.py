class Person():
    def __init__(self, p_name, p_age, p_height):
        self.__name = p_name
        self.__age = p_age
        self.__height = p_height
        self.public_prop = "i'm public"

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    def __del__(self):
        print("This person object is destroyed by the garbage collector")


person1 = Person("Phil", 20, 6)
print(str(person1.name))
person1.name = "Mike"
print(str(person1.name))