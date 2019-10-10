from logelei.year2019number41 import Person, Gender
from logelei.year2019number41.__Rule import _Rule


class InBetweenGender(_Rule):
    def __init__(self, allowed, person, gender):
        """
        Constructor

        Parameters
        ----------
        allowed : bool
            if true, this rule ensured that the rule is fulfilled, otherwise it ensures that the rule is not filfilled 
        person  : Person
        gender : Gender

        Examples
        --------
        After defining anna, we define that she has to sit between two men.

        >>> anna = Person("Anna", Gender.FEMININE)
        >>> InBetweenGender(True,  anna, Gender.MASCULINE)
        """
        self.__allowed = allowed
        self.__person = person
        self.__gender = gender

    def valid(self, path):
        for index, node in enumerate(path[1:-1]):
            shifted_index = index + 1
            if node.person == self.__person \
                    and path[shifted_index + 1].person.gender == self.__gender \
                    and path[shifted_index - 1].person.gender == self.__gender:
                if self.__allowed:
                    return True
                else:
                    return False
        if self.__allowed:
            return False
        else:
            return True
