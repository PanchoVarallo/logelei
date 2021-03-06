import networkx as nx
from abc import ABCMeta, abstractmethod

from logelei.Y2019Nr41 import GraphComponents
from logelei.Y2019Nr41.GraphComponents import Order


class _Rule(metaclass=ABCMeta):
    @abstractmethod
    def valid(self, path):
        pass


class Validator:
    """
    A validator with a list of list of rules.

    Parameters
    ----------
    name : list[list[_Rule]].
        The list of list of rules.

    Examples
    --------
    >>> anna = GraphComponents.Person("Anna", GraphComponents.Gender.FEMININE)
    >>> frank = GraphComponents.Person("Frank", GraphComponents.Gender.MASCULINE)
    >>> Validator([[DistanceInBetween(True, frank, anna, 0, Order.ORDERED)]])
    """

    def __init__(self, list_of_list_of_rules):
        self.__list_of_list_of_rules = list_of_list_of_rules

    def apply_rules(self, graph):
        """
        Most important method. Apply rules on a graph.

        Parameters
        ----------
        name : Graph
            The graph.

        Examples
        --------
        After defining three persons, we define that Frank sits to the left of Anna and
        apply the rule on the graph. The final path solution is
        [[Jolanda, Frank, Anna, Jolanda]] and it has to be read counterclockwise.

        >>> anna = GraphComponents.Person("Anna", GraphComponents.Gender.FEMININE)
        >>> frank = GraphComponents.Person("Frank", GraphComponents.Gender.MASCULINE)
        >>> jolanda = GraphComponents.Person("Jolanda", GraphComponents.Gender.FEMININE)
        >>> graph = GraphComponents.Graph([jolanda, anna, frank])
        >>> Validator([[DistanceInBetween(True, frank, anna, 0, GraphComponents.Order.ORDERED)]]).apply_rules(graph)
        >>> final_path = GraphComponents.Graph.get_graph_paths(graph)
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


class InBetweenGender(_Rule):
    """
    Rule to define that a person sits between to persons of the same gender.

    Parameters
    ----------
    allowed : bool
        If true, the rule is fulfilled.
    person  : Person
        The person.
    gender : Gender
        The gender of the two neighbors.

    Examples
    --------
    After defining anna, we define that she sits between two men.

    >>> anna = GraphComponents.Person("Anna", GraphComponents.Gender.FEMININE)
    >>> InBetweenGender(True, anna, GraphComponents.Gender.MASCULINE)
    """
    def __init__(self, allowed, person, gender):
        self.__allowed = allowed
        self.__person = person
        self.__gender = gender

    def valid(self, path):
        """
        Checks if a path fulfills the rule.

        Parameters
        ----------
        path : path from NetworkX
            A path from NetworkX. Every logelei.Y2019Nr41.Validator._Rule has to implement this method.
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
    """
    Rule to define how two persons sit in relation to each other.

    Parameters
    ----------
    allowed : bool
        If true, the rule is fulfilled.
    left_person : Person
        The person on the left.
    right_person : Person
        The person on the right.
    in_between : int
        Number of persons in between the two persons.
    ordered : Order
        If ORDERED, the order is relevant.

    Examples
    --------
    After defining persons, we define that Frank sits directly to the left of Anna.

    >>> anna = GraphComponents.Person("Anna", GraphComponents.Gender.FEMININE)
    >>> frank = GraphComponents.Person("Frank", GraphComponents.Gender.MASCULINE)
    >>> DistanceInBetween(True, frank, anna, 0, Order.ORDERED)
    """
    def __init__(self, allowed, left_person, right_person, in_between, ordered):
        self.__allowed = allowed
        self.__left_person = left_person
        self.__right_person = right_person
        self.__in_between = in_between
        self.__ordered = ordered

    def __str__(self):
        return self.__allowed

    def valid(self, path):
        """
        Checks if a path fulfills the rule.

        Parameters
        ----------
        path : path from NetworkX
            A path from NetworkX. Every logelei.Y2019Nr41.Validator._Rule has to implement this method.
        """
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
