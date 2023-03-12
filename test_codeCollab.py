from codeCollab import Tetris
import unittest
from io import StringIO

from unittest.mock import patch

class Test_tetris(unittest.TestCase):
    @patch("codeCollab.Tetris.left", return_value= "left and row down")
    @patch('builtins.input', return_value='a')
    def test_left(self, mock_input, mock_left):
        self.assertEqual(Tetris().move(), 'left and row down')

    @patch("codeCollab.Tetris.right", return_value= "right and row down")
    @patch('builtins.input', return_value='d')
    def test_right(self, mock_input, mock_right):
        self.assertEqual(Tetris().move(), 'right and row down')
    
    @patch("codeCollab.Tetris.clock_rotate", return_value= "clockwise and move one row down")    
    @patch('builtins.input', return_value='s')
    def test_clock_rotate(self, mock_input, mock_clock):
        self.assertEqual(Tetris().move(), 'clockwise and move one row down')

    @patch("codeCollab.Tetris.anticlock_rotate", return_value= "counter clockwise and move one row down")
    @patch('builtins.input', return_value='w')
    def test_anticlock_rotate(self, mock_input, mock_anticlock):
        self.assertEqual(Tetris().move(), 'counter clockwise and move one row down')

    @patch("codeCollab.Tetris.do_nothing", return_value= "no action but move one row down")
    @patch('builtins.input', return_value=' ')
    def test_do_nothing(self, mock_input, mock_donothing):
        self.assertEqual(Tetris().move(), 'no action but move one row down')

    @unittest.mock.patch('builtins.print')
    @patch('builtins.input', side_effect=['1','yn','yes','s'])
    def test_incoorect_input(self, mock_input, mock_print):
        self.assertEqual(Tetris().move(), "rotate piece clockwise and move one row down")
        self.assertEqual(mock_input.call_count, 4)
        mock_print.assert_called_with('Invalid Move Please Enter make a valid Move')

if __name__ == '__main__':
    unittest.main()
