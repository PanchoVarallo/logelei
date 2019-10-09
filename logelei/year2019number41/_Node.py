from logelei.year2019number41 import Person


class _Node:
    def __init__(self, person: Person, seat: int, number: int):
        """
        Constructor.

        Parameters
        ----------
        person : Person
        seat : int
        number : int
        """
        self.person = person
        self.seat = seat
        self.number = number

    def __repr__(self):
        return self.person.name
