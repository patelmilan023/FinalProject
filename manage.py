from flask_script import Manager
from movie import app, db, Movie, Actor


manager = Manager(app)


@manager.command
def deploy():
    db.drop_all()
    db.create_all()
    actor1 = Actor(name='Coldplay', active='1999-present')
    actor2 = Actor(name='Maroon 5', active='2010-2017')
    movie1= Movie(title='Yellow', year=2000, actor=actor1)
    movie2 = Movie(title='Suger',year=2014, actor=actor2)
    db.session.add(actor1)
    db.session.add(actor2)
    db.session.add(movie1)
    db.session.add(movie2)
    db.session.commit()



if __name__ == '__main__':
    manager.run()
