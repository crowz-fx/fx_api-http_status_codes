# fx_api-http_status_codes   
A Python webserver that serves up HTTP status codes on RESTful endpoints. The API is driven by a Swagger definition that uses connexion to handle the Swagger endpoint to the application endpoint.

Link to hosted...
- Information/entrypoint page --> [HERE][1]
- Swagger definition --> [HERE][2]

## Python version
Developed and run with Python3.7.

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
In order to run the server the following parameters can be accepted or omitted in any combination;
```
# --debug-mode       ;; default = false     ;; enable debugging of Flask, SQLAlchemy and SQLite
# --port=<int>       ;; default = 5000      ;; integer to run the application using that port
# --host="<string>"  ;; default = "0.0.0.0" ;; string to use as the host
# --ga-version=<int> ;; default = 1         ;; version of the google analytics API to use
# --ga-id="<string>"  ;; default = ""        ;; tracking ID used in google analytics API

python --debug-mode --port=<int> --host="<string>" --ga-version=<int> --ga-id="<string>" server.py
```
 
[1]: https://crowzfx.co.uk/api/http-status/info
[2]: https://crowzfx.co.uk/api/http-status/v1/ui/
