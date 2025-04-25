class Person:
    def __new__(cls, *args, **kwargs):
        print("Creating a new Person object")
        instance = super().__new__(cls)
        return instance

    def __init__(self, name, age):
        print("Initializing the Person object")
        self.name = name
        self.age = age


person = Person("John Doe", 30)
print(f"Person's name: {person.name}, age: {person.age}")

# Creating a new Person object
# Initializing the Person object
# Person's name: John Doe, age: 30
