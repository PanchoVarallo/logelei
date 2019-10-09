from unittest import TestCase

import logelei.year2019number41 as logelei

class TestTask(TestCase):
    def testTask(self):
        graph = logelei.Graph([logelei.Person("Jolanda", logelei.Gender.FEMININE),
                               logelei.Person("Anna", logelei.Gender.FEMININE),
                               logelei.Person("Frank", logelei.Gender.MASCULINE),
                               logelei.Person("Tina", logelei.Gender.FEMININE),
                               logelei.Person("Torsten", logelei.Gender.MASCULINE),
                               logelei.Person("Sabine", logelei.Gender.FEMININE),
                               logelei.Person("Thomas", logelei.Gender.MASCULINE),
                               logelei.Person("Lena", logelei.Gender.FEMININE)])

        rules = [[logelei.DistanceInBetween(False, "Anna", "Frank", 0, logelei.Order.UNORDERED)],
                 [logelei.DistanceInBetween(False, "Tina", "Torsten", 0, logelei.Order.UNORDERED)],
                 [logelei.DistanceInBetween(True, "Thomas", "Jolanda", 0, logelei.Order.UNORDERED)],
                 [logelei.InBetweenGender(True, "Sabine", logelei.Gender.MASCULINE)],
                 [logelei.DistanceInBetween(True, "Frank", "Tina", 0, logelei.Order.ORDERED),
                  logelei.DistanceInBetween(True, "Tina", "Lena", 0, logelei.Order.ORDERED)],
                 [logelei.DistanceInBetween(True, "Tina", "Torsten", 0, logelei.Order.UNORDERED),
                  logelei.DistanceInBetween(True, "Tina", "Torsten", 1, logelei.Order.UNORDERED)],
                 [logelei.DistanceInBetween(False, "Anna", "Lena", 0, logelei.Order.UNORDERED)],
                 [logelei.DistanceInBetween(False, "Anna", "Lena", 1, logelei.Order.UNORDERED)]]

        assert logelei.Graph.get_number_of_graph_paths(graph) == 5040, "We initially expect 5040 possible solutions"
        logelei.Validator(rules).validate_and_reduce(graph)
        assert logelei.Graph.get_number_of_graph_paths(graph) == 1, "We finally expect 1 possible solutions"
        final_path = logelei.Graph.get_graph_paths(graph)
        for path in final_path:
            assert path[0].person.name == "Jolanda"
            assert path[1].person.name == "Lena"
            assert path[2].person.name == "Frank"
            assert path[3].person.name == "Tina"
            assert path[4].person.name == "Anna"
            assert path[5].person.name == "Torsten"
            assert path[6].person.name == "Sabine"
            assert path[7].person.name == "Thomas"
            assert path[8].person.name == "Jolanda"
        print("\n" + str(final_path))