class Person:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def __repr__(self):
        return self.name + "|" + self.gender.__str__()