import os, sys
import connexion
import requests
from sqlalchemy import create_engine
from sqlalchemy.pool import SingletonThreadPool
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from flask_marshmallow import Marshmallow
from flask import render_template

debug_through_app = False
host_ip = "0.0.0.0"
port = 5000
api_version = "v1"

# analytic base info
ga_version = "1"
ga_id = ""

if len(sys.argv) > 1 and sys.argv[1] == "--help":
    print("Usage: --debug-mode --port=<int> --host=\"<string>\" --ga-version=<int> --ga-id=\"<string>\"")
    sys.exit(1)

for arg in sys.argv:
    if arg.startswith("--debug-mode"):
        debug_through_app = True
    elif arg.startswith("--port"):
        port = arg.split("=")[1]
    elif arg.startswith("--host"):
        host_ip = arg.split("=")[1]
    elif arg.startswith("--ga-version"):
        ga_version = arg.split("=")[1]
    elif arg.startswith("--ga-id"):
        ga_id = arg.split("=")[1]

# setup variables for locations
base_dir = os.path.abspath(os.path.dirname(__file__))
sqlite_url = "sqlite:///" + base_dir + "/database/status-codes.db"
sqlalchemy_engine_echo = debug_through_app

# setup the application, create the db connection and marshmallow
app = connexion.App(__name__, specification_dir = base_dir)
engine = create_engine(sqlite_url, echo = debug_through_app, connect_args={ "check_same_thread" : False })
Session = sessionmaker(bind = engine)
Base = declarative_base(engine)
marsh = Marshmallow(app.app)

# function is used to create new session for each access of the db
def generate_new_session_connector():
    return Session()

# this is used to post analytics off to google (driven by parameters)
def post_to_analytics(endpoint):
    base_url = "https://www.google-analytics.com/collect?"
    base_url += "v=" + ga_version
    base_url += "&tid=" + ga_id
    base_url += "&cid=1" # hardcoded as it comes from this server not client
    base_url += "&t=pageview" # set option to be pageview, easier collection in analytics
    base_url += "&dp=%2fapi%2fhttp-status%2f" + api_version + endpoint.replace("/", "%2f")
    
    requests.post(base_url)

# main route for the home page
@app.route("/api/http-status/info")
def info():
    return render_template("info.html", ga_id = ga_id, swagger_url = api_version + "/ui")

# start up of the server app instance
if __name__ == "__main__":
    app.add_api(base_dir + "/swagger.yml")
    app.static_folder = "static"
    app.run(debug = debug_through_app, host = host_ip, port = port)