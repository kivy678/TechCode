from flask import Flask, render_template
from flask_socketio import SocketIO, send
import time

app = Flask('TEST WEBPAGE',
            static_folder='static',
            template_folder='templates')

app.config['SECRET_KEY'] = 'BCODE_Flask'
socketio = SocketIO(app)


@app.route("/")
def main():
    return render_template('index.html')


def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!')


@socketio.on('my event')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    print('received my event: ' + str(json))
    for i in range(100):
        socketio.emit('my response', json, callback=messageReceived)
        time.sleep(1)


if __name__ == '__main__':
    socketio.run(app, host="127.0.0.1", port=7777)
