from flask import render_template, request, current_app
from app.models.message import Message
from . import web
from flask_socketio import emit, SocketIO
import sys
sys.path.append('../neo4j/')
from conversation import Graph4Match

socketio = SocketIO()


@web.route('/autochat', methods=['GET'])
def autochat():
    if request.method == 'GET':
        return render_template('chat/autochat.html')


@socketio.on('new message')
def new_message(message_body):
    message_body = message_body.split('\n')
    in_message = Message(author='user', body=message_body)
    emit('new message',
         {'message_html': render_template('chat/_message.html', message=in_message),
          'message_body': message_body},
         broadcast=False)

    graph = Graph4Match(current_app.config['NEO4J_IP'], current_app.config['NEO4J_USER'], current_app.config['NEO4J_PASSWORD'])
    out = graph.match_in_string(message_body[0]).split('\n')
    out_message = Message(author='ai', body=out)
    emit('new message',
         {'message_html': render_template('chat/_message.html', message=out_message),
          'message_body': out},
         broadcast=False)
