# FinalProject
My final misy350 project
This project is suppose to create a list of actors and movies.

The design of the database is simple, there are two tables one regarding the Directors, and one with the Movies, 


Directors Database looks like:

Director Name	About	Movies
Director 1	About Director 1	Movies of Director 1
Director 2	About Director 2	Movies of Director 2

Movies Database looks like:

Movie Name	Director	Release Date
Movie 1	Director 1	Release Date of Movie 1
Movie 2	Director 2	Release Date of Movie 2

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
