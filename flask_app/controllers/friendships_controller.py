from flask_app import app
from flask import render_template, redirect, request, flash, session
from flask_app.models.user_model import User
from flask_app.models.friendship_model import Friendship

#view friendlist in dashboard
@app.route('/friendships/view')
def view_friendships():
    if 'user_id' not in session:
        return redirect ('/')
    friends = Friendship.get_all_friends({'id': session['user_id']})
    return render_template ('dashboard.html', friends = friends)

#view friends profile
@app.route('/friendships/view/<int:id>')
def view_friend_page(id):
    if 'user_id' not in session:
        return redirect ('/')
    logged_user = User.get_by_id({'id': session['user_id']})
    this_friend = Friendship.get_one_friend({'id': id })
    return render_template ('friend_view.html', this_friend = this_friend, logged_user=logged_user)

#view a user profile
@app.route('/users/view/<int:id>')
def view_userProfile (id):
    if 'user_id' not in session:
        return redirect ('/')
    logged_user = User.get_by_id({'id': session['user_id']})
    other_user= User.get_unfriended_user_by_name({'id': id })
    return render_template ('friend_view.html', other_user=other_user, logged_user=logged_user)
