from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.user_model import User
from flask_app.models.anime_model import Anime

@app.route('/anime/search')
def search():
    if 'user_id' not in session:
        return redirect ('/')
    logged_user = User.get_by_id({'id': session['user_id']})
    return render_template('create.html', logged_user=logged_user)

@app.route('/animes/add', methods=['POST'])
def add():
    if 'user_id' not in session:
        return redirect ('/')
    watched_anime = Anime.create({request.form})
    return redirect ('/dashboard', watched_anime=watched_anime)
    