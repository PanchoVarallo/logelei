from Logelei.year2019number41.__SingleRule import __SingleRule


class InBetweenGender(__SingleRule):
    def __init__(self, allowed, person, gender):
        self.__allowed = allowed
        self.__person = person
        self.__gender = gender

    def valid(self, path):
        for index, node in enumerate(path[1:-1]):
            shifted_index = index + 1
            if node.person.name == self.__person \
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
