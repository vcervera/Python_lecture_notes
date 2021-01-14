class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = ages
        self.is_hungry = True

    def eat_food(self):
        if self.is_hungry:
            self.is_hungry = False
        else:
            print("But I'm not hungry!")
    
    def have_birthday(self):
        self.age += 1

    def greet(self, other_person):
        print(f"Hello, {other_person}. My name is {self.name}")

person = Human("Logan", 25)

print(person.name)

person.eat_food()
person.eat_food()

person.greet('Joe')
person.greet('Tom')