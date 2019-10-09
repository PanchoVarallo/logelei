from Logelei.year2019number41.Order import Order
from Logelei.year2019number41.__SingleRule import __SingleRule


class DistanceInBetween(__SingleRule):
    def __init__(self, allowed, left_person, right_person, in_between, ordered):
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
            if node.person.name == self.__left_person \
                    and path[index + 1 + self.__in_between].person.name == self.__right_person:
                if self.__allowed:
                    return True
                else:
                    return False
            if self.__ordered == Order.UNORDERED:
                if path[index + 1 + self.__in_between].person.name == self.__left_person \
                        and node.person.name == self.__right_person:
                    if self.__allowed:
                        return True
                    else:
                        return False
        if self.__allowed:
            return False
        else:
            return True
