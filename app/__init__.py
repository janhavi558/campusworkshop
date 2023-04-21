"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-ch13fcbh4hstbhh9l8og-a.oregon-postgres.render.com",
        database="todo_06bn",
        user="todo_06bn_user",
        password="sGONm1JhPZu6Ft4VOHEX4V9QNq3QBnVW")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
