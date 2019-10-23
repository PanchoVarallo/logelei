from unittest import TestCase

import logelei.Y2019Nr41.GraphComponents as gc
import logelei.Y2019Nr41.Validator as vl


class TestYear2019Number41(TestCase):
    def test_actual_task(self):

        # Define persons
        jolanda = gc.Person("Jolanda", gc.Gender.FEMININE)
        anna = gc.Person("Anna", gc.Gender.FEMININE)
        frank = gc.Person("Frank", gc.Gender.MASCULINE)
        tina = gc.Person("Tina", gc.Gender.FEMININE)
        torsten = gc.Person("Torsten", gc.Gender.MASCULINE)
        sabine = gc.Person("Sabine", gc.Gender.FEMININE)
        thomas = gc.Person("Thomas", gc.Gender.MASCULINE)
        lena = gc.Person("Lena", gc.Gender.FEMININE)
        graph = gc.Graph([jolanda, anna, frank, tina, torsten, sabine, thomas, lena])

        # Define rules. Note: rules are list of list of rules, e.g. [[e1], [e2], [e3, e4]]].
        # This means that e1 and e2 and (e3 or e4) have to be fulfilled.
        rules = [[vl.DistanceInBetween(False, anna, frank, 0, gc.Order.UNORDERED)],
                 [vl.DistanceInBetween(False, tina, torsten, 0, gc.Order.UNORDERED)],
                 [vl.DistanceInBetween(True, thomas, jolanda, 0, gc.Order.UNORDERED)],
                 [vl.InBetweenGender(True, sabine, gc.Gender.MASCULINE)],
                 [vl.DistanceInBetween(True, frank, tina, 0, gc.Order.ORDERED),
                  vl.DistanceInBetween(True, tina, lena, 0, gc.Order.ORDERED)],
                 [vl.DistanceInBetween(True, tina, torsten, 0, gc.Order.UNORDERED),
                  vl.DistanceInBetween(True, tina, torsten, 1, gc.Order.UNORDERED)],
                 [vl.DistanceInBetween(False, anna, lena, 0, gc.Order.UNORDERED)],
                 [vl.DistanceInBetween(False, anna, lena, 1, gc.Order.UNORDERED)]]

        assert gc.Graph.get_number_of_graph_paths(graph) == 5040, "We initially expect 5040 possible solutions"
        # Apply the rules and reduce the graph
        vl.Validator(rules).apply_rules(graph)
        assert gc.Graph.get_number_of_graph_paths(graph) == 1, "We finally expect 1 possible solutions"
        # Print the final path that fulfils all rules
        final_path = gc.Graph.get_graph_paths(graph)
        for path in final_path:
            assert path[0].person == jolanda
            assert path[1].person == lena
            assert path[2].person == frank
            assert path[3].person == tina
            assert path[4].person == anna
            assert path[5].person == torsten
            assert path[6].person == sabine
            assert path[7].person == thomas
            assert path[8].person == jolanda
        print("\n" + str(final_path))

    def test_minimal(self):
        jolanda = gc.Person("Jolanda", gc.Gender.FEMININE)
        anna = gc.Person("Anna", gc.Gender.FEMININE)
        frank = gc.Person("Frank", gc.Gender.MASCULINE)
        graph = gc.Graph([jolanda, anna, frank])

        rules = [[vl.DistanceInBetween(True, frank, anna, 0, gc.Order.ORDERED)]]

        assert gc.Graph.get_number_of_graph_paths(graph) == 2, "We initially expect 2 possible solutions"
        vl.Validator(rules).apply_rules(graph)
        assert gc.Graph.get_number_of_graph_paths(graph) == 1, "We finally expect 1 possible solutions"
        final_path = gc.Graph.get_graph_paths(graph)
        for path in final_path:
            assert path[0].person == jolanda
            assert path[1].person == frank
            assert path[2].person == anna
            assert path[3].person == jolanda