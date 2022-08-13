#Dockerfile, Image, Container

FROM python:3.8

EXPOSE 5000

COPY . .

RUN pip install -U pip
RUN pip install -U nltk
RUN python -m nltk.downloader -q stopwords
RUN pip install -r requirements.txt


CMD python app.py