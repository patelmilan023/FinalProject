# FinalProject
My final misy350 project
This project is suppose to create a list of actors and movies.

The design of the database is simple, there are two tables one regarding the Directors, and one with the Movies, 


Movie Database:

|   Movie Name    |  About        |  Release           |
| --------------- | ------------- | ------------------ |
|  Movie1 Name    | About Movie1  |  Release of Movie1 |
|  Movie2 Name    | About Movie2  |  Release of Movie2 |

Actor Database:

|  Actor Name     |  About        | Movies            |
| --------------- | ------------- | ----------------- |
|  Actor1 Name    | About Actor1  |  Movies acted in  |
|  Actor2 Name    | About Actor2  |  Movies acted in  |


In orer to run this project the following must be executed:

1. Install virtualenv venv
2. Activate the virtual environment via (in Windows powershell):
venv/scripts/activate
3. Next by installing
pip install -r requirements.txt
4. than creating the database

python manage.py deploy
Finally running the server with debugger. 
python manage.py runserver -d
