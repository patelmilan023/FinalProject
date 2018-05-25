from flask_script import Manager
from movie import app, db, Movie, Actor


manager = Manager(app)


@manager.command
def deploy():
    db.drop_all()
    db.create_all()
    actor1 = Actor(name='Ryan Reynolds', active='1976-present')
    actor2 = Actor(name='Chris Pratt', active='2010-2017')
    actor3 = Actor(name='Robert Downey, Jr.', active='2000-present')
    movie1= Movie(title='Deadpool', year=2015, actor=actor1, rating="8.2")
    movie2 = Movie(title='Jurassic World',year=2016, actor=actor2, rating="8.5")
    movie3= Movie(title='Iron Man', year=2017, actor=actor3, rating="7.6")
    db.session.add(actor1)
    db.session.add(actor2)
    db.session.add(actor3)
    db.session.add(movie1)
    db.session.add(movie2)
    db.session.add(movie3)
    db.session.commit()



if __name__ == '__main__':
    manager.run()
