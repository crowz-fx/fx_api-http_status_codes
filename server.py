import os, sys
import connexion
from sqlalchemy import create_engine
from sqlalchemy.pool import SingletonThreadPool
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from flask_marshmallow import Marshmallow
from flask import render_template

debug_through_app = False
host_ip = '0.0.0.0'
port = 5000

if len(sys.argv) > 1 and sys.argv[1] == "--help":
    print("Usage: --debug-mode --port=<int> --hoste=\"<string>\"")
    sys.exit(1)

for arg in sys.argv:
    if arg.startswith("--debug-mode"):
        debug_through_app = True
    elif arg.startswith("--port"):
        port = arg.split("=")[1]
    elif arg.startswith("--host"):
        host_ip = arg.split("=")[1]

# setup variables for locations
base_dir = os.getcwd()
sqlite_url = "sqlite:///database/status-codes.db"
sqlalchemy_engine_echo = debug_through_app

# setup the application, create the db connection and marshmallow
app = connexion.App(__name__, specification_dir = base_dir)
engine = create_engine(sqlite_url, echo = debug_through_app, connect_args={ 'check_same_thread' : False})
Session = sessionmaker(bind = engine)
Base = declarative_base(engine)
marsh = Marshmallow(app.app)

# function is used to create new session for each access of the db
def generate_new_session_connector():
    return Session()

# main route for the home page
@app.route('/api/http-status/info')
def info():
    return render_template('info.html')

# start up of the server app instance
if __name__ == '__main__':
    app.add_api(base_dir + 'swagger.yml')
    app.run(debug = debug_through_app, host = host_ip, port = port)