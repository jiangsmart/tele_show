"""
注册所有相关蓝图,初始化数据库等
"""

from flask import Flask
from app.web import web
from app.web.autochat import socketio

def create_app():
    app = Flask(__name__)
    app.register_blueprint(web)
    socketio.init_app(app)
    return app
