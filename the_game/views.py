from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404
import random
from django.urls import reverse
from .models import side_stack_game
import random
from datetime import datetime

#Globals
user_id_string = 'user_id'

# Create your views here.
def home(request):
    """simply simplton home page that renders the start page may improve later """
    return render(request, 'connect4/index.html')

def setup(request):
    """
    this will just render the setup page where you will start the game 
    with the choose start player  1 or 2  
    """
    return render(request, 'connect4/setup.html')

def create_game(request):
    """
    this is were the game is created comes after the setup
    if you start first or not then the game and sets the session
    """
    user_id = get_session_id(request)
    if request.method == 'POST':
        player_num = request.POST['player'] #this is a string; either '1' or '2'
        if player_num not in ['1','2']:
            raise Http404("Page not available")      
        game = side_stack_game()
        if player_num == '1':
            game.player_1 = user_id
        if player_num == '2':
            game.player_2 = user_id
        player_name = request.POST["name"]
        game.player_1_name = player_name
        game.save()
        response = redirect('game', game_id = game.id)
        set_session_id(response, user_id)
        return response  
    else:
        raise Http404("Page not available")
    

def game(request, game_id):
    '''
    Check if session Id matches a player
    if it does return game
    if it does not and a player is still null -> assign player to session ID and return
    else 404
    '''
    user_id = get_session_id(request)
    game = get_object_or_404(side_stack_game, pk=game_id)   
    if user_id in [game.player_1, game.player_2]:
        pass #just return the game number
    elif game.player_1 == '':       
        game.player_1 = user_id
    elif game.player_2 == '':
        game.player_2 = user_id
    else:
        #game is already full
        #TODO: allow spectators?
        raise Http404("Page not available")
    game.save()
    response = render(request, "connect4/game.html", 
    {
        'absoluteLink': request.build_absolute_uri(),
        'game_id': game_id
    })
    set_session_id(response, user_id)
    return response

def set_session_id(response, value):
    """will set the current session id"""
    response.set_cookie(user_id_string,value)

def get_session_id(request):
    """
    will get session id if there is no user id 
    it will assign a random  value
    """
    value = request.COOKIES.get(user_id_string)
    if value is None:
        return str(random.randint(0, 2147483647))
    return value


def join_game(request):
    """
    Joining a Game
    """
    if request.method == 'POST':
        name = request.POST['name']
        game_id = request.POST['id']    
        game = side_stack_game.objects.get(id=game_id)
        if not game:
          raise Http404("Page not available")
        game.player_2_name = name
        game.save()
        return redirect('game', game_id = game.id)
    else:
        raise Http404("Page not available")
    
    
def create_single_game(request):
    """
    this is were the game is created comes after the setup
    if you start first or not then the game and sets the session
    """
    user_id = get_session_id(request)
    # if request.method == 'POST':
    player_num = 1  
    game = side_stack_game()
    game.player_1 = user_id
    game.player_2 = user_id+"bot"
    # player_name = request.POST["name"]
    game.player_1_name = "Human Player"
    game.player_2_name = "Bot"
    game.against_bot = True
    game.num_player_1_connection = 1 
    game.num_player_2_connection = 1
    game.save()
    response = redirect('game', game_id = game.id)
    set_session_id(response, user_id)
    return response  
