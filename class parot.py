class Parrot:
    species = "bird"

    def __init__(self, name, age):
        self.name = name
        self.age = age

macaw = Parrot("Ryan", 3)
cockatoo = Parrot("stellar", 5)

print("Species:", Parrot.species)
print("Parrot 1 Name:", macaw.name)
print("Parrot 1 Age:", macaw.age)
print("Parrot 2 Name:", cockatoo.name)
print("Parrot 2 Age:", cockatoo.age)
