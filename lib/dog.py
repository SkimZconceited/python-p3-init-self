#!/usr/bin/env python3

class Dog:
    def __init__(self, name, breed = 'Mutt') -> None:
        self.name = name
        self.breed = breed
        # self.breed = None
        # print(f'{name}')
        pass

    # def saves_self_breed(self, name, breed) -> None:
    #     self.name = name
    #     self.breed = breed
        # print(f"{self.name} {self.breed}")
        # pass
    
    
    pass

fido = Dog("Fido")
# fido.saves_self_breed("Fido", "Dalmatian")
# fido = Dog("Fido", 'Dalmatian')

print(fido.name)
print(fido.breed)

fido = Dog("Fido", "Dalmatian")
print(fido.name)
print(fido.breed)
# print(fido.saves_self_breed("Fido", "Dalmatian"))