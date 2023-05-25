from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash
from flask_app.models import user_model

class Anime:
    def __init__(self, data):
        self.id = data['id']
        self.anime_id = data['anime_id']
        self.links = data['links']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']

    @classmethod
    def create(cls, data):
        query = """INSERT INTO watched_animes (id, anime_id, links)
                VALUES ( %(id)s, %(anime_id)s, %(links)s );"""
        results = connectToMySQL(DATABASE).query_db(query, data)
        return results
    