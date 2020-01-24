.. _solutions:

Solutions
=========

Solutions for Year 2019
***********************

Edition 41
^^^^^^^^^^
https://www.zeit.de/2019/41/spiele-logelei-41

The Task (in German)
""""""""""""""""""""

Jolanda muss für ihre Feier anhand der Wünsche der Gäste die Sitzordnung an ihrem achteckigen Tisch festlegen.

Anna: "Frank hat so spitze Ellenbogen, der soll nicht neben mir sitzen."

Frank: "Wenn Tina und Torsten nebeneinandersitzen, dann lachen die zu laut."

Sabine: "Da ich schon lange Single bin, möchte ich neben zwei Männern sitzen."

Thomas: "Ich möchte mal wieder neben dir, Jolanda, sitzen."

Tina: "Ich möchte links von mir Frank sitzen haben, dann kann ich dessen Ohrring gebührend bewundern, oder rechts von mir Lena, die hat so ein tolles Tattoo auf ihrem linken Arm."

Torsten: "Ich möchte mit Tina reden können. Tina soll also neben mir sitzen, oder zumindest soll nur eine Person zwischen uns sitzen."

Lena: "Damit ich Annas Parfum nicht riechen muss, sollen mindestens zwei Personen zwischen uns sitzen."

The `Python` Solution
"""""""""""""""""""""

Import the packages.

.. code-block:: python

   import logelei.Y2019Nr41.Validator as vl
   import logelei.Y2019Nr41.GraphComponents as gc

Define the persons.

.. code-block:: python

   jolanda = gc.Person("Jolanda", gc.Gender.FEMININE)
   anna = gc.Person("Anna", gc.Gender.FEMININE)
   frank = gc.Person("Frank", gc.Gender.MASCULINE)
   tina = gc.Person("Tina", gc.Gender.FEMININE)
   torsten = gc.Person("Torsten", gc.Gender.MASCULINE)
   sabine = gc.Person("Sabine", gc.Gender.FEMININE)
   thomas = gc.Person("Thomas", gc.Gender.MASCULINE)
   lena = gc.Person("Lena", gc.Gender.FEMININE)

Define the graph.

.. code-block:: python

   graph = gc.Graph([jolanda, anna, frank, tina, torsten, sabine, thomas, lena])

Define the rules. Note: rules are list of list of rules, e.g. [[e1, e2, [e3, e4]]].
This means that e1 and e2 and (e3 or e4) have to be fulfilled.

.. code-block:: python

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

Define a validator to apply the rules on the graph.

.. code-block:: python

   vl.Validator(rules).apply_rules(graph)

Print the final solution.

.. code-block:: python
   :emphasize-lines: 2

   final_path = gc.Graph.get_graph_paths(graph)
   print("\n" + str(final_path))
   [[Jolanda, Lena, Frank, Tina, Anna, Torsten, Sabine, Thomas, Jolanda]]

Note that the solution has to be read counterclockwise.
