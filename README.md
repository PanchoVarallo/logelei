# logelei

The package `logelei` contains algorithms to solve tasks from https://www.zeit.de/autoren/Z/Zweistein.

### Year 2019, Number 41
##### The task
Jolanda muss für ihre Feier anhand der Wünsche der Gäste die Sitzordnung an ihrem achteckigen Tisch festlegen.

Anna: "Frank hat so spitze Ellenbogen, der soll nicht neben mir sitzen."

Frank: "Wenn Tina und Torsten nebeneinandersitzen, dann lachen die zu laut."

Sabine: "Da ich schon lange Single bin, möchte ich neben zwei Männern sitzen."

Thomas: "Ich möchte mal wieder neben dir, Jolanda, sitzen."

Tina: "Ich möchte links von mir Frank sitzen haben, dann kann ich dessen Ohrring gebührend bewundern, oder rechts von mir Lena, die hat so ein tolles Tattoo auf ihrem linken Arm."

Torsten: "Ich möchte mit Tina reden können. Tina soll also neben mir sitzen, oder zumindest soll nur eine Person zwischen uns sitzen."

Lena: "Damit ich Annas Parfum nicht riechen muss, sollen mindestens zwei Personen zwischen uns sitzen."

##### The model
We build up a graph that encodes all possible combinations and discard wrong combinations.

##### The solution
See `test_Year2019number41.py`.

`========================== 1 passed in 1.21 seconds ===========================.`

`[[Jolanda, Lena, Frank, Tina, Anna, Torsten, Sabine, Thomas, Jolanda]]`
