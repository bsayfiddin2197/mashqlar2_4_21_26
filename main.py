class Animal:
    def __init__(self, type, sound):
        self.type = type
        self.sound = sound

    def make_sound(self):
        print(f"{self.type} {self.sound}laydi")


k6 = Animal("Mushuk", "miyov")
k6.make_sound()

class Movie:
    def __init__(self, title, genre):
        self.title = title
        self.genre = genre

    def info(self):
        print(f"Title: {self.title}")
        print(f"Genre: {self.genre}")


k7 = Movie("Avatar", "Robotics")
k7.info()

class Laptop:
    def __init__(self, model, ram):
        self.model = model
        self.ram = ram

    def show_specs(self):
        print(f"Model: {self.model}")
        print(f"RAM: {self.ram}")

k8 = Laptop("HP", "16GB")
k8.show_specs()

class Teacher:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject

    def teach(self):
        print(f"{self.name} {self.subject} o\'qitadi")

k9 = Teacher("Ali", "Matematika")
k9.teach()

class Phone:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def show_price(self):
        print(f"Brand: {self.brand}")
        print(f"Price: {self.price}")

k10 = Phone("Samsung", 120)
k10.show_price()
