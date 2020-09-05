from flask import Flask
from uuid import uuid4
from src.etc.settings import Settings
from src.controllers.loginController import LoginController
from src.controllers.registerController import RegisterController
from src.controllers.profileController import ProfileController
from src.controllers.chatController import ChatController
from src.controllers.friendshipController import FriendshipController
from src.controllers.notificationController import NotificationController


app = Flask(__name__)

app.secret_key = uuid4().hex


@app.route("/login", methods=["POST"])
def login():
    return LoginController().requestHandler()


@app.route("/register", methods=["POST"])
def register():
    return RegisterController().requestHandler()


@app.route("/profile", methods=["POST"])
def profile():
    return ProfileController().requestHandler()


@app.route("/chat", methods=["POST"])
def chat():
    return ChatController().requestHandler()


@app.route("/friendship", methods=["POST"])
def friendship():
    return FriendshipController().requestHandler()


@app.route("/notification", methods=["POST"])
def notification():
    return NotificationController().requestHandler()


if __name__ == "__main__":
    app.run(host=Settings.HOST, port=Settings.PORT)
