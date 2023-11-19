
#importing unittest to test def functions 
#to craete unit test import patch and magicMock which is class of the unittest.mock
#unittest is built in python, pach to decorater and context and MagicMock which allows to specify behavior for mocked objects
import unittest
from unittest.mock import patch, MagicMock
#importing CatchTheBallGame and GameQuitExceotion from Game
from game import CatchTheBallGame, GameQuitException
import pygame

class TestCatchTheBallGame(unittest.TestCase):#it define the test case class
   def setUp(self):
       pygame.init() # Initialize Pygame and craetes an instance of catchtheballgame
       self.game = CatchTheBallGame()

   def tearDown(self):#Clean up Pygame
       pygame.quit() 

   @patch('sys.exit')#3to replace sys.exit with mock and test if calling quit game raises
   def test_quit_game(self, mock_sys_exit):
       with self.assertRaises(GameQuitException):
           self.game.quit_game()
       mock_sys_exit.assert_not_called()

   @patch('pygame.display.set_mode', MagicMock(return_value=pygame.Surface((800, 600))))
   @patch('os.chdir')
   def test_init(self, mock_chdir):#checks the behavior of the start_menu
       game = CatchTheBallGame()
       mock_chdir.assert_called_once_with('/home/chungku/Desktop/game')
       self.assertIsInstance(game.screen, pygame.Surface)

   @patch('pygame.event.get', MagicMock(return_value=[pygame.event.Event(pygame.QUIT)]))
   @patch('pygame.display.flip')
   def test_start_menu_quit(self, mock_display_flip):#test start_menu_quit
       with self.assertRaises(GameQuitException):
           self.game.start_menu()
       mock_display_flip.assert_not_called()

   @patch('pygame.event.get', MagicMock(return_value=[pygame.event.Event(pygame.MOUSEBUTTONDOWN)]))
   @patch('pygame.display.flip')
   def test_start_menu_restart_game(self, mock_display_flip):#to test restart_game
       self.game.game_over = True
       self.game.restart_game()
       self.assertFalse(self.game.game_over)
       self.assertEqual(self.game.score, 0)
       mock_display_flip.assert_not_called()

if __name__ == '__main__':# check that the test are run 
   unittest.main()
