class Dog:
    def __init__(self, breed, color):
        self.breed = breed
        self.color = color

Dog1 = Dog("German Shepherd", "Brown")

Dog2 = Dog("Lab", "Black")

print("Dog1 ====> Breed:", Dog1.breed, "| Color:", Dog1.color)
print("Dog2 ====> Breed:", Dog2.breed, "| Color:", Dog2.color)
