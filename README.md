# fx_api-http_status_codes
A python 3 webserver that serves up https status codes on RESTful endpoints. The API is driven by a Swagger definition that uses connexion to handle the mapping.

## Python version
Developed and run with Python3.7

## Setup
To setup the environment you need to setup a virtual env using the following;

```
# create your virtual env with a name
python -m venv {what you want to call it}

# activate the virtual env
source {name of env}/Scripts/activate

# now install requirements using PIP
pip install -r requirements.txt
```

## Running the server
In order to run the server the following parameters can be accepted or omitted
```
# --debug-mode      ;; default = false     ;; will enable debugging of Flask, SQLAlchemy and SQLite
# --port=<int>      ;; default = 5000      ;; take in the integer to run the application using that port
# --host="<string>" ;; default = "0.0.0.0" ;; string to use as the host

python --debug-mode --port=<int> --host="<string>" server.py
```

