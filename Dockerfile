FROM python:3
ENV PYTHONUNBUFFERED=1
RUN mkdir /QuizApp
WORKDIR /QuizApp
ADD requirements.txt /QuizApp/
COPY requirements.txt /home/kali/Desktop/QuizApp
RUN pip install Django
COPY . /QuizApp/