# Question 15: Build a Custom compartor
import functools

class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

people = [
    Person("Alice", 30, "New York"),
    Person("Bob", 25, "Los Angeles"),
    Person("Charlie", 35, "Chicago"),
    Person("David", 25, "Houston")
]

def custom_comparator(person1, person2):
    if person1.age < person2.age:
        return -1
    elif person1.age > person2.age:
        return 1
    else:
        if person1.name < person2.name:
            return -1
        elif person1.name > person2.name:
            return 1
        else:
            return 0

sorted_people = sorted(people, key=functools.cmp_to_key(custom_comparator))

for person in sorted_people:
    print(person.name, person.age, person.city)