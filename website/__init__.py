from flask import Flask

def create_app():
  app = Flask(__name__)
  app.config['SECRET_KEY'] = 'CaballoHomosexualDeLasMontañas'

  from .vistas import vistas

  app.register_blueprint(vistas, url_prefix='/')
  
  return app