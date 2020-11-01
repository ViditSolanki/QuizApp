FROM python:3
ENV PYTHONUNBUFFERED=1
RUN mkdir /QuizApp
WORKDIR /QuizApp
RUN pip install Django
RUN pip install django-crispy-forms
RUN pip install psycopg2-binary
COPY . /QuizApp/
