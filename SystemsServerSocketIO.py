from asyncio.windows_events import NULL
from socket import socket
from flask import Flask, render_template, redirect, request, session
from flask.globals import request
from flask_socketio import SocketIO, emit, rooms,send
from flask_socketio import join_room, leave_room
from flask import g
import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.FATAL)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)
socketio.init_app(app, cors_allowed_origins="*")


@socketio.on('connect')
def test_connect():
    print('Client connected')

@socketio.on('client: Calculate price')
def OCR_request(data):
    id = request.sid
    print('here')
    Apple_price = 20*data[Apples]
    Banana_price = 30*data[Bananas]
    orange_price = 10*data[Oranges]
    response = Apple_price + Banana_price + orange_price
    print(response)   
    socketio.emit('Server: Response', response , room = id ) 
    
if __name__ == '__main__':
    socketio.run(app,host='0.0.0.0',debug=True, port=5000)
    






