FROM python:3.7

EXPOSE 80
WORKDIR /usr/src/app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

CMD [ "flask", "run", "--host=0.0.0.0", "--port=80"]
