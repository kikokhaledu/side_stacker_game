from django.db import models
import jsonfield
import numpy as np
from .game_utility import is_turn , check_winner

# PlayerKeyMaxLength = 50

class side_stack_game(models.Model):
    def initialize_board():
        #board is 7X7
        #the first index is col: 0 is left most row, 6 if right row
        #the second index is the row: 0 is the top row: 5 is the bottom row
        #TODO find a way to do it with numpy so i can make it dynamic (user provieds the number of rows and columns)
        return [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]


    game_state = models.JSONField(default =initialize_board)
    player_1 = models.CharField(max_length = 100, default='')
    player_2 = models.CharField(max_length = 100, default='')
    player_1_name = models.CharField(max_length = 256, default='')
    player_2_name = models.CharField(max_length = 256, default='')
    num_player_1_connection = models.IntegerField(default=0)
    num_player_2_connection = models.IntegerField(default=0)
    game_complete = models.BooleanField(default=False)
    against_bot = models.BooleanField(default=False)
    game_winner = models.CharField(max_length=1,null=True,blank=True)
    


    def try_move(self, player, row,side):
        if is_turn(self, player):
            row_value = self.game_state[row] #ex row 0 [0,0,0,0,0,0,0] has 7 0s which are cols
            if side == 'Right':
                index = -1
                for elem_number,col in reversed(list(enumerate(row_value))):
                    if col == 0 :
                        index += 1
                        break
                if index == -1:
                    #row full
                    return False       
                row_value.pop(elem_number)
                row_value.append (player)
                self.game_state[row] = row_value
                self.save()
                return True
            elif side == 'Left':
                index = -1
                for elem_number,col in list(enumerate(row_value)):
                    if col == 0 :
                        index += 1
                        break
                if index == -1:
                    #row is full
                    return False
                row_value.pop(elem_number)
                row_value.insert(0,player )
                self.game_state[row] = row_value
                self.save()
                return True
            return False
        else:
            pass



