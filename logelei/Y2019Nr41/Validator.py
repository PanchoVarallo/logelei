import networkx as nx
from abc import ABCMeta, abstractmethod

from logelei.Y2019Nr41.GraphComponents import Order


class Validator:
    def __init__(self, list_of_list_of_rules):
        self.__list_of_list_of_rules = list_of_list_of_rules

    def validate_and_reduce(self, graph):
        """
        Method where a Graph .

        Parameters
        ----------
        graph : Graph
            the created Graph

        Examples
        --------
        >>>
        >>>
        >>> Validator([[DistanceInBetween(True, frank, anna, 0, Order.ORDERED)]])

        """
        nodes_to_remove = set()
        paths = list(nx.all_simple_paths(graph.nx_graph, source=graph.source_node, target=graph.target_node))
        for path in paths:
            valid_path = True
            for list_of_rules in self.__list_of_list_of_rules:
                valid_rule = False
                for rule in list_of_rules:
                    if rule.valid(path):
                        valid_rule = True
                    if valid_rule:
                        break
                if not valid_rule:
                    valid_path = False
                    break
            if not valid_path:
                path_nodes_to_remove = self.__get_path_nodes_to_remove(graph, path)
                nodes_to_remove.update(path_nodes_to_remove)
        for node in nodes_to_remove:
            graph.nx_graph.remove_node(node)
        return graph

    @staticmethod
    def __get_path_nodes_to_remove(graph, path):
        path_nodes_to_remove = set()
        for node in reversed(path[1:-1]):
            predecessors = list(tuple(graph.nx_graph.predecessors(node)))
            successors = list(tuple(graph.nx_graph.successors(node)))
            if len(predecessors) == 1 and len(successors) == 1:
                path_nodes_to_remove.add(node)
        return path_nodes_to_remove


class _Rule(metaclass=ABCMeta):
    @abstractmethod
    def valid(self, path):
        pass


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
        """
        Constructor.

        Parameters
        ----------
        list_of_list_of_rules : list of (list of _Rule)

        Examples
        --------
        Examples should be written in doctest format, and should illustrate how
        to use the function.

        >>>
        >>>
        >>> Validator([[DistanceInBetween(True, frank, anna, 0, Order.ORDERED)]])

        """
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


class DistanceInBetween(_Rule):

    def __init__(self, allowed, left_person, right_person, in_between, ordered):
        """
        Constructor.

        Parameters
        ----------
        allowed : bool
            if true, this rule ensured that the rule is fulfilled, otherwise it ensures that the rule is not filfilled
        left_person : Person
        right_person : Person
        in_between : int
            number of persons in between the two persons
        ordered : Order
            if Order.ORDERED, the order is relevant, otherwise it is not

        Examples
        --------
        After defining persons, we define that frank has to sit directly to the left of anna.

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