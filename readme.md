###Solution Runner

####Structure
The tests (located in `_solution.py`) have access to the files in `/in` and a data object that's loaded in to the BaseSolution Class (located in `utils.py`)


####Setup & Running it 
To see how it works, run `python3 _solution.py` which creates an instance of the TestSolution class called mainTest. MainTest tests against the python module main (loaded from `in/main.py`) and has a few functions immediately availiable to it. 

####Output
For now, the report() method in TestSolution just returns an array of strings, though this could easily be changed to a json object (or some other thing). 