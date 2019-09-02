FROM ubuntu:latest
RUN apt-get update -y
#RUN apt-get update -y && apt-get install -y python3
RUN apt-get install -y python3-pip python3-dev build-essential
RUN apt install -y libsm6 libxext6

RUN apt-get clean \
 && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt /app
RUN pip3 install -r requirements.txt

COPY now-deploy.pem /app
COPY GetKey.py /app
COPY img.py /app
COPY app.py /app
CMD python3 app.py 