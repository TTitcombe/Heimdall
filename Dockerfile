FROM python:3.9

WORKDIR /app

# Install app dependencies
COPY requirements.txt ./

RUN pip install -r requirements.txt

# Bundle app source
COPY heimdall /app

EXPOSE 8080
CMD [ "python" ]
