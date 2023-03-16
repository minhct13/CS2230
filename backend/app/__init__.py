from flask import Flask
from config import config
from flask_cors import CORS

from app.controllers.classify import classify_bp
from app.services import model 
def create_app():
    app = Flask(__name__)

    app.config.from_object(config)

    api_prefix = app.config["APP_API_PREFIX"]
    
    model.init_model(app)
    
    CORS(
          app, resources={
            rf"{api_prefix}/*": {
              "origins": [
                "*"
              ],
              "supports_credentials": True,
            }
          }
        )
    # Import a module / component using its blueprint handler variable
    app.register_blueprint(classify_bp, url_prefix=api_prefix)
    
    return app
