# chat/consumers.py
import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync

from the_game.game_utility import check_winner,bot_move
from .models import side_stack_game

user_id_string = 'user_id'

class side_stack_consumer(WebsocketConsumer):

    def connect(self):
        """
        standard django channels connect nothing special here 
        just connects to the game. checks the number of players 
        and if 2 players are connected  no one else can connect 
        has to match the user in the cookies 
        """
        self.game_id = self.scope['url_route']['kwargs']['game_id']
        self.game_name = 'game_%s' % self.game_id #just string formatting

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.game_name,
            self.channel_name
        )


        game = side_stack_game.objects.get(pk = self.game_id)
        if game.player_1 == self.scope['cookies'][user_id_string]:
            self.player_num = 1 
            game.num_player_1_connection += 1
        elif game.player_2 == self.scope['cookies'][user_id_string]:
            self.player_num = 2
            game.num_player_2_connection += 1
        else:
            self.send({"close": True}) #closes the connection immediately
        game.save()   
        self.accept()
        self.make_everyone_update()

    def disconnect(self, close_code):
        """
        standard channels disconnect function
        """
        game = side_stack_game.objects.get(pk = self.game_id)
        if self.player_num == 1:
            game.num_player_1_connection -= 1
        elif self.player_num == 2:
            game.num_player_2_connection -= 1
        else:
            Exception("player_num must be 1 or 2")
        game.save()
        self.make_everyone_update()
        async_to_sync(self.channel_layer.group_discard)(
            self.game_name,
            self.channel_name
        )

    
    def make_everyone_update(self):
        "channels group  makes sure that everybody has the same messages and updates etc."
        async_to_sync(self.channel_layer.group_send)(
            self.game_name,
            {
                'type': 'update_message'
            }
        )

    #recieve message from websocket
    def receive(self, text_data):
        """
        this is where we recieve the message from the websocet we then
        have to try the move it is valid then we will check for a winner 
        to see if the current player's move resulted in a win for any player 
        NOTE a play can win on his/her turn or the other player's turn 
        """
        text_data_json = json.loads(text_data)
        row  = text_data_json['row']
        side = text_data_json['side']
        player = text_data_json['player'] 
        game = side_stack_game.objects.get(pk = self.game_id)
        if not game.try_move(player,row,side):
            pass
        result = check_winner (game.game_state)
        if result != 0  and result !=3 :
            game.game_complete = True
            game.game_winner = result
            game.save()
        elif result == 3:
            game.game_complete = True
            game.game_winner = result
            game.save()
            #tie
        else:
            pass
        if game.against_bot:
            if player == 1:
                bot_move(game,2)
            else:
                bot_move (game,1)
            result = check_winner (game.game_state)
            if result != 0  and result !=3 :
                game.game_complete = True
                game.game_winner = result
                game.save()
            elif result == 3:
                game.game_complete = True
                game.game_winner = result
                game.save()
                #tie
            else:
                pass
        #used 1 and 2 instead of == player cause you can win on your opponent's turn
        self.make_everyone_update() 

    def update_message(self, event):
        """
        channel calles it on update
        """
        self.send_to_client()

    def send_to_client(self):
        """
        will get the game object and send to the React app
        """
        game = side_stack_game.objects.get(pk = self.game_id)
        game_to_send = {}
        game_to_send['board'] = game.game_state
        game_to_send['player'] = self.player_num
        game_to_send['game_status'] = game.game_complete
        game_to_send['winner'] = game.game_winner
        game_to_send['player_1_name'] = game.player_1_name
        game_to_send['player_2_name'] = game.player_2_name
        opponent_connected = False
        if self.player_num == 1:
            opponent_connected = game.num_player_2_connection >= 1
        if self.player_num == 2:
            opponent_connected = game.num_player_1_connection >= 1
        game_to_send['opponent_connected'] = opponent_connected
        self.send(text_data=json.dumps(game_to_send))