FROM python:3.9
ENV PYTHONUNBUFFERED 1
RUN mkdir /src
WORKDIR /src

RUN apt update
RUN apt install -y unoconv libreoffice vim
COPY requirements.txt /src/
RUN pip install --upgrade pip && pip install -r requirements.txt
COPY . /code/
RUN apt install fonts-noto-cjk