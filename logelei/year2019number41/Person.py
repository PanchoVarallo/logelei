from logelei.year2019number41 import Gender


class Person:
    def __init__(self, name, gender):
        """
        Constructor.

        Parameters
        ----------
        name : str
        gender : Gender
        """
        self.name = name
        self.gender = gender

    def __eq__(self, other):
        if not isinstance(other, Person):
            return NotImplemented
        return self.name == other.name and self.gender == other.gender

    def __repr__(self):
        return self.name + "|" + self.gender.__str__()