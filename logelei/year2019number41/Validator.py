import networkx as nx


class Validator:
    def __init__(self, list_of_list_of_rules):
        self.__list_of_list_of_rules = list_of_list_of_rules

    def validate_and_reduce(self, graph):
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
