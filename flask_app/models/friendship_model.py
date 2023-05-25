from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask_app.models import user_model

class Friendship:
    def __init__(self, data):
        self.user_id = data['user_id']
        self.friend_id = data['friend_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create(cls, data):
        query = """INSERT INTO friendships (user_id, friend_id)
                VALUES ( %(user_id)s, %(friend_id)s);"""
        results = connectToMySQL(DATABASE).query_db(query, data)
        return results

    @classmethod
    def get_all_friends(cls, data):
        query = """ SELECT users2.username AS friend_name, users2.id AS friend_id FROM users JOIN friendships ON users.id = friendships.user_id LEFT JOIN users AS users2 
                    ON users2.id = friendships.friend_id WHERE users.id = %(id)s """
        results = connectToMySQL(DATABASE).query_db(query, data)
        return results

    @classmethod
    def get_one_friend(cls, data):
        query = """
            SELECT * FROM friendships JOIN users ON friendships.friend_id = users.id WHERE user_id = %(id)s;
        """
        results = connectToMySQL(DATABASE).query_db(query, data)
        return results