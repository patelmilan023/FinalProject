import os
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)


basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
db = SQLAlchemy(app)


class Actor(db.Model):
    __tablename__ = 'actors'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    active = db.Column(db.Text)
    movies=db.relationship('Movie', backref='actor', cascade = 'delete')


class Movie(db.Model):
    __tablename__ = 'movies'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64))
    year = db.Column(db.Integer)
    actor_id =db.Column(db.Integer, db.ForeignKey('actors.id'))


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/actors')
def actors():
    return render_template('actors-all.html', actors=actors)


@app.route('/movies')
def movies():
    return render_template('movies-all.html', movies=movies)


@app.route('/about')
def about():
    return render_template('about.html')

    
if __name__ == '__main__':
    app.run()
