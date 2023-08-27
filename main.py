from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

#função de enviar mensagem
@socketio.on("message")
def gerenciar_mensagem(mensagem):
    send(mensagem, broadcast=True)

#criar rota 1ª página
@app.route("/")
def homepage():
    return render_template("index.html")

#rodar codigo
socketio.run(app, host="Seu IP")

#websocket

