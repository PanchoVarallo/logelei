# Logelei
[![Build Status](https://travis-ci.com/PanchoVarallo/Schafkopf-Application.svg?branch=master)](https://travis-ci.com/github/PanchoVarallo/Logelei)
[![codecov](https://codecov.io/gh/PanchoVarallo/logelei/branch/master/graph/badge.svg)](https://codecov.io/gh/PanchoVarallo/logelei)
[![Documentation Status](https://readthedocs.org/projects/logelei/badge/?version=latest)](https://logelei.readthedocs.io/en/latest/?badge=latest)

The package `logelei` contains algorithms to solve tasks from https://www.zeit.de/autoren/Z/Zweistein.

### Documentation and Usage
https://logelei.readthedocs.io/en/latest/. 

### For Developers
Feel free to add more solutions. 
Stick to the documentation styles and patterns.
Before creating a pull request, go to `docs/source` to create a fresh documentation by running:
```sh
# 1. Delete all rst-files except index.rst, solutions.rst, make.bat, Makefile
# 2. clean the current build folder with
make clean
# 3. Update the documentation by creating rst-files from docstrings
sphinx-apidoc -f -M -o . ../../logelei
# 4. If you want to create a local documentation
make html
```
