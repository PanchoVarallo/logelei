from unittest import TestCase

import logelei.year2019number41 as logelei


class TestYear2019Number41(TestCase):
    def test_actual_task(self):

        # Define persons
        jolanda = logelei.Person("Jolanda", logelei.Gender.FEMININE)
        anna = logelei.Person("Anna", logelei.Gender.FEMININE)
        frank = logelei.Person("Frank", logelei.Gender.MASCULINE)
        tina = logelei.Person("Tina", logelei.Gender.FEMININE)
        torsten = logelei.Person("Torsten", logelei.Gender.MASCULINE)
        sabine = logelei.Person("Sabine", logelei.Gender.FEMININE)
        thomas = logelei.Person("Thomas", logelei.Gender.MASCULINE)
        lena = logelei.Person("Lena", logelei.Gender.FEMININE)
        graph = logelei.Graph([jolanda, anna, frank, tina, torsten, sabine, thomas, lena])

        # Define rules. Note: rules are list of list of rules, e.g. [[e1, e2, [e3, e4]]]. This means that
        # e1 and e2 and (e3 or e4) have to be fulfilled.
        rules = [[logelei.DistanceInBetween(False, anna, frank, 0, logelei.Order.UNORDERED)],
                 [logelei.DistanceInBetween(False, tina, torsten, 0, logelei.Order.UNORDERED)],
                 [logelei.DistanceInBetween(True, thomas, jolanda, 0, logelei.Order.UNORDERED)],
                 [logelei.InBetweenGender(True, sabine, logelei.Gender.MASCULINE)],
                 [logelei.DistanceInBetween(True, frank, tina, 0, logelei.Order.ORDERED),
                  logelei.DistanceInBetween(True, tina, lena, 0, logelei.Order.ORDERED)],
                 [logelei.DistanceInBetween(True, tina, torsten, 0, logelei.Order.UNORDERED),
                  logelei.DistanceInBetween(True, tina, torsten, 1, logelei.Order.UNORDERED)],
                 [logelei.DistanceInBetween(False, anna, lena, 0, logelei.Order.UNORDERED)],
                 [logelei.DistanceInBetween(False, anna, lena, 1, logelei.Order.UNORDERED)]]

        assert logelei.Graph.get_number_of_graph_paths(graph) == 5040, "We initially expect 5040 possible solutions"
        # Apply the rules and reduce the graph
        logelei.Validator(rules).validate_and_reduce(graph)
        assert logelei.Graph.get_number_of_graph_paths(graph) == 1, "We finally expect 1 possible solutions"
        # Print the final path that fulfils all rules
        final_path = logelei.Graph.get_graph_paths(graph)
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
        jolanda = logelei.Person("Jolanda", logelei.Gender.FEMININE)
        anna = logelei.Person("Anna", logelei.Gender.FEMININE)
        frank = logelei.Person("Frank", logelei.Gender.MASCULINE)
        graph = logelei.Graph([jolanda, anna, frank])

        rules = [[logelei.DistanceInBetween(True, frank, anna, 0, logelei.Order.ORDERED)]]

        assert logelei.Graph.get_number_of_graph_paths(graph) == 2, "We initially expect 2 possible solutions"
        logelei.Validator(rules).validate_and_reduce(graph)
        assert logelei.Graph.get_number_of_graph_paths(graph) == 1, "We finally expect 1 possible solutions"
        final_path = logelei.Graph.get_graph_paths(graph)
        for path in final_path:
            assert path[0].person == jolanda
            assert path[1].person == frank
            assert path[2].person == anna
            assert path[3].person == jolanda