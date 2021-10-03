FROM python:3.9

WORKDIR /app

# Install app dependencies
COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY heimdall /app

EXPOSE 8080
EXPOSE 271017

CMD [ "app/heimdall" ]
