from django.test import TestCase
from .game_utility import check_winner, is_turn


class test_is_winner(TestCase):
    """
    to test the check _ winner conditions 
    this will try different combinations to check if it works correctly
    """
    def test_board_is_empty_no_winner(self):
        board = [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]
        self.assertEqual(check_winner(board), 0)
    
    def test_horizontal_win_right(self):
        board = [[0,0,0,0,0,0,0],[0,0,0,1,1,1,1],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]
        self.assertEqual(check_winner(board), 1)
        
    def test_horizontal_win_left(self):
        board = [[0,0,0,0,0,2,0],[0,0,0,1,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[2,2,2,2,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]
        self.assertEqual(check_winner(board), 2)
        
    def test_vertical_win(self):
        board = [[0,0,0,0,0,2,0],[0,0,0,1,0,0,0],[0,0,0,0,0,0,0],[2,0,0,0,0,0,0],[2,2,2,0,0,0,0],[2,0,0,0,0,0,0],[2,0,0,0,0,0,0]]
        self.assertEqual(check_winner(board), 2)

    def test_diagonal_win(self):
        board = [[1,0,0,0,0,2,0],[2,1,0,1,0,0,0],[2,2,1,0,0,0,0],[1,1,2,1,0,0,0],[2,2,2,0,0,0,0],[1,0,0,0,0,0,0],[2,0,0,0,0,0,0]]
        self.assertEqual(check_winner(board), 1)

    def test_other_diagonal_win(self):
        board = [[0,0,0,0,0,2,1],[0,0,0,0,0,1,2],[0,0,0,0,1,0,0],[1,0,0,1,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]
        self.assertEqual(check_winner(board), 1)
    
    # TODO its almost imposible to have a tie so how i tested this is that i bypassed the other winning conditions
    # and only leftout the tie condition
    # maunally added a board thta looks like this 
    # [[1, 2, 1, 2, 1, 2, 1], [1, 2, 1, 2, 1, 2, 1], [1, 2, 1, 2, 1, 2, 1],
    # [1, 2, 1, 2, 1, 2, 1], [1, 2, 1, 2, 1, 2, 1], [1, 2, 1, 2, 1, 2, 1],
    # [1, 2, 1, 2, 1, 2, 0]]
    # then tested the final move in the last row last col  and it worked fine.
