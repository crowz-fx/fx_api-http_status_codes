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

RUN pip3 install -r requirements.txt

CMD ["python3", "server.py", "--port=5001", "--ga-id='UA-81180399-1'"]