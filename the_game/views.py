from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404
import random
from django.urls import reverse
from .models import Connect4Game
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

def creategame(request):
    """
    this is were the game is created comes after the setup
    if you start first or not then the game and sets the session
    """
    userId = GetSessionid(request)
    if request.method == 'POST':
        playerNum = request.POST['player'] #this is a string; either '1' or '2'
        if playerNum not in ['1','2']:
            raise Http404("Page not available")      
        game = Connect4Game()
        if playerNum == '1':
            game.player1 = userId
        if playerNum == '2':
            game.player2 = userId
        game.save()
        response = redirect('game', game_id = game.id)
        SetSessionid(response, userId)
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
    userId = GetSessionid(request)
    game = get_object_or_404(Connect4Game, pk=game_id)   
    if userId in [game.player1, game.player2]:
        pass #just return the game number
    elif game.player1 == '':       
        game.player1 = userId
    elif game.player2 == '':
        game.player2 = userId
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
    SetSessionid(response, userId)
    return response

def SetSessionid(response, value):
    """will set the current session id"""
    response.set_cookie(user_id_string,value)

def GetSessionid(request):
    """
    will get session id if there is no user id 
    it will assign a random  value
    """
    value = request.COOKIES.get(user_id_string)
    if value is None:
        return str(random.randint(0, 2147483647))
    return value