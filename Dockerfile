ARG FROM_IMAGE
FROM ${FROM_IMAGE}

WORKDIR /opt/applications/executables/http-status-api

RUN mkdir -p database && mkdir -p templates

ADD server.py .
ADD requirements.txt .
ADD handler.py .
ADD database/* database/
ADD templates/ templates/
ADD swagger.yml .

RUN apt-get update -y && apt-get install --no-install-recommends -y \
  python3.7 \
  && rm -rf /var/lib/apt/lists/*

RUN python3.7 -m pip install pip

RUN pip install -U pip setuptools wheel

RUN python3.7 -m pip install -r requirements.txt

CMD ["python3", "server.py", "--port=5001", "--ga-id='G-D1FW7EL3ZM'"]