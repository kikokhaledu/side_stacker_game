# notes and documentation of this app

the_game directory  is where the magic happens  

## Installation

covered in the readme.md file 


## function 

- lobby just choose to start the game 
- game setup you choose start type as player 1 or 2 
- game is created in the back ground every player is assigned a random id and the session id is set and cookies get saved 
- all the above are in normal Django HTML/CSS templates that are rendered no react here 
- after the game is created in the background you get redirected to the game which will invoke the React app /static/the_game/index-bundle.js'
- the react app will display the game info and manage the socket communication and display the updated accordingly 
- the game status is managed by numbers  as follows 
    - 0 = no winner the game keeps going  1 = player one wins  2 = player 2 wins  3 = a draw
- when the game ends no one can make a move 
- currently the only way to invite is to copy the URL after you create a game and then send it to someone else 
- the session will allow only 2 players to be connected 
- note that the Draw is implemented  but the case of a draw in a side stake is almost impossible since we have 7*7 board
- i have tested the draw logic but I had to disable the winning logic and fill the board so that only one piece left then add it to get a draw 
    check the pictures provided in this directory 
- a player can add peices to the sides  but only the first cell which will shift other chells accrodingly 


## storage

I have chosen Postgres because i am using a Json field

## notes 
- i used function based views  because it gives me more control and can show you my work better 
- read readme file carefully 
- check the TODO.md file 
- this app was done in a very short time so i didn't have the time to implement all the things i wanted 
- i initially used numpy but it make lots of problems with postgresql JSONField so i decided to ditch it 
- you will need a .env like the one called .env.example in this dir

## License
[by khaled yasser](kikokhaled.u@gmail.com)