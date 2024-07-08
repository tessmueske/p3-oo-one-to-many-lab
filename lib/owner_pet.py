class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        if pet_type.lower() not in Pet.PET_TYPES:
            raise Exception("Invalid pet type")
        self.pet_type = pet_type
        self.name = name
        self.owner = owner
        Pet.all.append(self)

class Owner:
    def __init__(self, name):
        self.name = name
        self._pets = []

    def pets(self):
        new_pets = []
        for pet in Pet.all:
            if self == pet.owner:
                new_pets.append(pet)
        return new_pets

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("Only instances of Pet can be added")
        if pet.owner is not None:
            raise Exception("Pet already has an owner")
        pet.owner = self
        self._pets.append(pet)

    def get_sorted_pets(self):
        def get_pet_name(pet):
            return pet.name

        return sorted(self.pets(), key=get_pet_name)