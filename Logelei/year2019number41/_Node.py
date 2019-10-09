class _Node:
    """ A node of the graph."""

    def __init__(self, person, seat, number):
        """
        Blub

        Parameters
        ----------
        person
        seat
        number
        """
        self.person = person
        self.seat = seat
        self.number = number

    def __repr__(self):
        return self.person.name
