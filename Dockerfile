FROM python:3.6

WORKDIR /flaskapp
ADD . /flaskapp
RUN pip install -r requirements.txt

EXPOSE 5000
CMD ["python", "flaskapp/app.py"]
