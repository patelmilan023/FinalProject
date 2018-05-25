import os
from flask import Flask, render_template, request, flash, redirect, url_for, jsonify
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
    title = db.Column(db.String(256))
    year = db.Column(db.Integer)
    actor_id =db.Column(db.Integer, db.ForeignKey('actors.id'))


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/actors')
def show_all_actors():
    actors = Actor.query.all()
    return render_template('actors-all.html', actors=actors)

@app.route('/actor/add', methods=['GET', 'POST'])
def add_actor():
    if request.method == 'GET':
        return render_template('actor-add.html')
    elif request.method == 'POST':

        name = request.form['name']
        about = request.form['about']

        actor = Actor(name=name, about=about)
        db.session.add(actor)
        db.session.commit()
        return redirect(url_for('show_all_actors'))

@app.route('/api/actor/add', methods=['POST'])
def add_ajax_actors():

    name = request.form['name']
    about = request.form['about']


    actor = Actor(name=name, about=about)
    db.session.add(actor)
    db.session.commit()

    flash('Actor Inserted', 'success')
    return jsonify({"id": str(actor.id), "name": actor.name})

@app.route('/actor/edit/<int:id>', methods=['GET', 'POST'])
def edit_actor(id):
    actor = Actor.query.filter_by(id=id).first()
    if request.method == 'GET':
        return render_template('actor-edit.html', actor=actor)
    elif request.method == 'POST':

        actor.name = request.form['name']
        actor.about = request.form['about']

        db.session.commit()
        return redirect(url_for('show_all_actors'))

@app.route('/actor/delete/<int:id>', methods=['GET', 'POST'])
def delete_actor(id):
    actor = Actor.query.filter_by(id=id).first()
    if request.method == 'GET':
        return render_template('actor-delete.html', actor=actor)
    elif request.method == 'POST':

        db.session.delete(actor)
        db.session.commit()
        return redirect(url_for('show_all_actors'))

@app.route('/api/actor/<int:id>', methods=['DELETE'])
def delete_ajax_actor(id):
    actor = Actor.query.get_or_404(id)
    db.session.delete(actor)
    db.session.commit()
    return jsonify({"id": str(actor.id), "name": actor.name})


@app.route('/movies')
def show_all_movies():
    movies = Movie.query.all();
    return render_template('movie-all.html', movies=movies)

@app.route('/movie/add', methods=['GET', 'POST'])
def add_movies():
    if request.method == 'GET':
        actors = Actor.query.all()
        return render_template('movie-add.html', actors=actors)
    elif request.method == 'POST':

        name = request.form['name']
        year = request.form['year']
        ratings = request.form['ratings']
        actor_name = request.form['actor']
        actor = actor.query.filter_by(name=actor_name).first()
        movie = Movie(name=name, year=year, ratings=ratings, actor=actor)


        db.session.add(movie)
        db.session.commit()
        return redirect(url_for('show_all_movies'))

@app.route('/movie/edit/<int:id>', methods=['GET', 'POST'])
def edit_movie(id):
    movie = Movie.query.filter_by(id=id).first()
    actors = Actor.query.all()
    if request.method == 'GET':
        return render_template('movie-edit.html', movie=movie, actors=actors)
    elif request.method == 'POST':

        movie.name = request.form['name']
        movie.year = request.form['year']
        movie.ratings = request.form['ratings']
        actor_name = request.form['actor']
        actor = Actor.query.filter_by(name=actor_name).first()
        movie.actor = actor

        db.session.commit()
        return redirect(url_for('show_all_movies'))

@app.route('/movie/delete/<int:id>', methods=['GET', 'POST'])
def delete_movie(id):
    movie = Movie.query.filter_by(id=id).first()
    actors = Actor.query.all()
    if request.method == 'GET':
        return render_template('movie-delete.html', movie=movie, actors=actors)
    elif request.method == 'POST':


        db.session.delete(movie)
        db.session.commit()
        return redirect(url_for('show_all_movies'))

@app.route('/api/movie/<int:id>', methods=['DELETE'])
def delete_ajax_movie(id):
    movie = Movie.query.get_or_404(id)
    db.session.delete(movie)
    db.session.commit()
    return jsonify({"id": str(movie.id), "name": movie.name})

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/users')
def show_all_users():
    return render_template('user-all.html')
@app.route('/form-demo', methods=['GET', 'POST'])
def form_demo():

    if request.method == 'GET':
        first_name = request.args.get('first_name')
        if first_name:
            return render_template('form-demo.html', first_name=first_name)
        else:
            return render_template('form-demo.html', first_name=session.get('first_name'))
    if request.method == 'POST':
        session['first_name'] = request.form['first_name']

        return redirect(url_for('form_demo'))

@app.route('/user/<string:name>/')
def get_user_name(name):

    return render_template('user.html', name=name)


@app.route('/movie/<int:id>/')
def get_movie_id(id):

    return "Hi, this is %s and the movie's id is %d" % ('administrator', id)


if __name__ == '__main__':
    app.run()
