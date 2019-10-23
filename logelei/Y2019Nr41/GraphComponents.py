import copy
import networkx as nx
from enum import Enum


class Person:
    """
    Defines Person initialized with name and gender.
    Parameters
    ----------
    name : str
        the name of the person
    gender : Gender
        the gender of the person
    """
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def __eq__(self, other):
        if not isinstance(other, Person):
            return NotImplemented
        return self.name == other.name and self.gender == other.gender

    def __repr__(self):
        return self.name + "|" + self.gender.__str__()


class Gender(Enum):
    """
    Defines MASCULINE and FEMININE gender.
    """
    MASCULINE = 1
    FEMININE = 2


class Graph:
    """
    Defines graph of all possibilities how persons can sit.

    ----------
    persons : list of Person
        the list of persons that are going to sit at the table.
    """
    def __init__(self, persons):
        self.__persons = persons
        self.__build_graph(persons)

    def __build_graph(self, persons):
        nx_graph = nx.DiGraph()
        source_node = _Node(persons[0], 1, 0)
        target_node = _Node(persons[0], len(persons) + 1, 1)
        nx_graph.add_nodes_from([source_node, target_node])
        seat = 2
        self.__add_predecessors(nx_graph, source_node, target_node, seat, persons[1:])
        self.nx_graph = nx_graph
        self.source_node = source_node
        self.target_node = target_node

    def __add_predecessors(self, nx_graph, source_node, target_node, seat, persons):
        for index, person in enumerate(persons):
            node = _Node(person, seat, index)
            nx_graph.add_node(node)
            nx_graph.add_edge(source_node, node)
            if len(persons) == 1:
                nx_graph.add_edge(node, target_node)
            remaining_persons = copy.deepcopy(persons)
            remaining_persons.pop(index)
            self.__add_predecessors(nx_graph, node, target_node, seat + 1, remaining_persons)

    @staticmethod
    def get_graph_paths(graph):
        return list(nx.all_simple_paths(graph.nx_graph, source=graph.source_node, target=graph.target_node))

    @staticmethod
    def get_number_of_graph_paths(graph):
        return len(list(nx.all_simple_paths(graph.nx_graph, source=graph.source_node, target=graph.target_node)))


class _Node:
    def __init__(self, person: Person, seat: int, number: int):
        self.person = person
        self.seat = seat
        self.number = number

    def __repr__(self):
        return self.person.name


class Order(Enum):
    """
    Defines ORDERED and UNORDERED rule.
    """
    ORDERED = 1
    UNORDERED = 2