import copy
import networkx as nx

from logelei.year2019number41._Node import _Node


class Graph:
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
