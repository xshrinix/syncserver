from python:3.10-slim
#RUN apk add --no-cache py3-pip && pip3 install --upgrade pip
#pip install --upgrade pip
WORKDIR /app
COPY . /app

RUN pip install -r requirements.txt

EXPOSE 8000

ENTRYPOINT ["crossbar", "start", "--cbdir", "/app/.crossbar"]
# CMD ["helloworld.py"]
