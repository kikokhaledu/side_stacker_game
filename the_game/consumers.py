# chat/consumers.py
import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync

from the_game.game_utility import check_winner
from .models import Connect4Game

user_id_string = 'user_id'

class Connect4Consumer(WebsocketConsumer):

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


        game = Connect4Game.objects.get(pk = self.game_id)
        if game.player1 == self.scope['cookies'][user_id_string]:
            self.PlayerNum = 1 
            game.numPlayer1Connections += 1
        elif game.player2 == self.scope['cookies'][user_id_string]:
            self.PlayerNum = 2
            game.numPlayer2Connections += 1
        else:
            self.send({"close": True}) #closes the connection immediately
        game.save()   
        self.accept()
        self._makeEveryoneUpdate()

    def disconnect(self, close_code):
        """
        standard channels disconnect function
        """
        game = Connect4Game.objects.get(pk = self.game_id)
        if self.PlayerNum == 1:
            game.numPlayer1Connections -= 1
        elif self.PlayerNum == 2:
            game.numPlayer2Connections -= 1
        else:
            Exception("PlayerNum must be 1 or 2")
        game.save()
        self._makeEveryoneUpdate()
        async_to_sync(self.channel_layer.group_discard)(
            self.game_name,
            self.channel_name
        )

    
    def _makeEveryoneUpdate(self):
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
        game = Connect4Game.objects.get(pk = self.game_id) 
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
        #used 1 and 2 instead of == player cause you can win on your opponent's turn
        self._makeEveryoneUpdate() 

    def update_message(self, event):
        """
        channel calles it on update
        """
        self._sendToClient()

    def _sendToClient(self):
        """
        will get the game object and send to the React app
        """
        game = Connect4Game.objects.get(pk = self.game_id)
        gameToSend = {}
        gameToSend['board'] = game.game_state
        gameToSend['player'] = self.PlayerNum
        gameToSend['game_status'] = game.game_complete
        gameToSend['winner'] = game.game_winner
        opponentConnected = False
        if self.PlayerNum == 1:
            opponentConnected = game.numPlayer2Connections >= 1
        if self.PlayerNum == 2:
            opponentConnected = game.numPlayer1Connections >= 1
        gameToSend['opponentConnected'] = opponentConnected
        self.send(text_data=json.dumps(gameToSend))