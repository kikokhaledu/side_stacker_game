# side stacker game

This is essentially connect-four, but the pieces stack on either side of the board instead of bottom-up.
Two players see a board, which is a grid of 7 rows and 7 columns. They take turn adding pieces to a row, on one of the sides. The pieces stack on top of each other, and the game ends when there are no spaces left available, or when a player has four consecutive pieces on a diagonal, column, or row.


## Installation

#### set environment variables
if you decided to user docker then you must set your .env to have the 

DB_HOST=db

if you don't want to use docker 
you can set it to any host you want 

please refer  to the .env.example file

#### docker installation 

to install we have to options normal pip installation and docker installation:

with docker its easy just navigate to the root dir of the project and run the following:

```bash
docker-compose run web
```
then 

```bash
docker-compose up
```
#### local installation 

for normal installation a venv is preferred so all you need to do is to make sure you have python 3.10 installed

clone this repository and run the following in the base dir

```bash
python -m venv <venv_name>
```

activate your venv

#### windows

```bash
cd venv/Scripts/
```

```bash
Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process -Force
```
```bash
./activate
```


#### mac or linux

```bash
source venv/bin/activate
```

finally run the following to install the requirements make sure you are in the project base dir

```bash
pip install -r requirments.txt
```

```bash
python manage.py runserver
```

## usage and testing
for testing run the following command 

```bash
python manage.py test
```

result should look like 

```bash
......
----------------------------------------------------------------------
Ran 6 tests in 0.008s

OK
```

## load testing 

navigate to the root dir of the project and run the following:

```bash
locust -f locust.py --host http://127.0.0.1:8000 --users 100 --spawn-rate 50
```

then in your browser simply visit 

http://localhost:8089/

load testing was done using locust.py the reports are in the root directory of this project under the names 

### "side_stacker_load_testing.HTML" 
and 
### "side_stacker_load_testing.csv"


## storage

this project uses PostgreSQL for its DB because its utilizing JSONField
so make sure you have a running PostgreSQL server with 

create a DB 

add your DB information to the .env file
along with your secret please check example .env file

#### for more information please check the DOC.MD file 
## License
[by khaled yasser](kikokhaled.u@gmail.com)
