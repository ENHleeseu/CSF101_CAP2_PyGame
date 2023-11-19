# CSF101_CAP2_pygame
#test.py

#This document provides an overview of the test cases used to verify the functionality of the CatchTheBallGame class in the game module. 
#The test cases are written using Python's built-in unittest module and the unittest.mock module for creating mock objects and patching functions or methods.

#The Resources Used are 
#1.unittest: A built-in Python module for creating unit tests. 
#It provides a rich set of tools for constructing and running tests, and includes features for test automation, sharing of setup and shutdown code for tests, aggregation of tests into collections, 
#And independence of the tests from the reporting framework.
#2. unittest.mock: A module for creating mock objects and patching functions or methods.

#Justification :
#The unittest and unittest.mock modules were chosen for their simplicity, ease of use, and the fact that they are built into Python.
#They provide a powerful and flexible framework for creating unit tests, and the unittest.mock module is particularly useful for isolating the class under test from its dependencies.
#The test cases are organized into a TestCatchTheBallGame class, which inherits from unittest.TestCase. Each method in this class represents a test case. 
#The setUp and tearDown methods are used to set up and clean up the test environment before and after each test case.

#The test cases cover:
#test_quit_game: Tests that the quit_game method of CatchTheBallGame raises a GameQuitException and does not call sys.exit.
#test_init: Tests that the initialization of CatchTheBallGame correctly sets up the game environment and does not call pygame.display.set_mode or os.chdir.
#test_start_menu_quit: Tests that the start_menu method of CatchTheBallGame raises a GameQuitException when a quit event is received and does not call pygame.display.flip.
#test_start_menu_restart_game: Tests that the restart_game method of CatchTheBallGame correctly restarts the game when a mouse button down event is received and does not call pygame.display.flip.
#Each test case uses the assertRaises method to check that the correct exceptions are raised.
#The assertIsInstance method is used to check that the screen attribute of CatchTheBallGame is an instance of pygame.Surface.



