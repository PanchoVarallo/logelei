from logelei.year2019number41 import Gender
from logelei.year2019number41.Order import Order
from logelei.year2019number41.Person import Person
from logelei.year2019number41.__Rule import _Rule


class DistanceInBetween(_Rule):

    def __init__(self, allowed, left_person, right_person, in_between, ordered):
        """
        Constructor.

        Parameters
        ----------
        allowed : bool
            if true, this rule ensures the defined order, otherwise it prohibits it
        left_person : Person
        right_person : Person
        in_between : int
            number of persons in between the two persons
        ordered : Order
            if Order.ORDERED, the order is relevant, otherwise it is not

        Examples
        --------
        After defining two persons, we define that frank has to sit directly to the left of anna.

        >>> anna = Person("Anna", Gender.FEMININE)
        >>> frank = Person("Frank", Gender.MASCULINE)
        >>> DistanceInBetween(True, frank, anna, 0, Order.ORDERED)
        """
        self.__allowed = allowed
        self.__left_person = left_person
        self.__right_person = right_person
        self.__in_between = in_between
        self.__ordered = ordered

    def __str__(self):
        return self.__allowed

    def valid(self, path):
        cut = -1 - self.__in_between
        for index, node in enumerate(path[:cut]):
            if node.person == self.__left_person \
                    and path[index + 1 + self.__in_between].person == self.__right_person:
                if self.__allowed:
                    return True
                else:
                    return False
            if self.__ordered == Order.UNORDERED:
                if path[index + 1 + self.__in_between].person == self.__left_person \
                        and node.person == self.__right_person:
                    if self.__allowed:
                        return True
                    else:
                        return False
        if self.__allowed:
            return False
        else:
            return True
