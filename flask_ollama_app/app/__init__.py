from flask import Flask
from flask_socketio import SocketIO

socketio = SocketIO()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your_secret_key'

    from .route1 import route1_bp
    from .route2 import route2_bp
    from .websocket1 import websocket1_bp
    from .websocket2 import websocket2_bp

    app.register_blueprint(route1_bp)
    app.register_blueprint(route2_bp)
    app.register_blueprint(websocket1_bp)
    app.register_blueprint(websocket2_bp)

    socketio.init_app(app)
    return app
