FROM python:3.9
ENV PYTHONUNBUFFERED 1
RUN mkdir /src
WORKDIR /src

RUN apt-get update
RUN apt-get install -y unoconv libreoffice
RUN apt-get install python3-uno
RUN apt install -y vim
# RUN apt-get install libreoffice-pyuno
RUN apt-get install antiword
# execで入ってから以下のコマンド打てばインストールできる
# RUN apt-get install iputils-ping net-tools
# apt-get install lsof 
# python3コンテナ内でping localhosは反応ある
COPY requirements.txt /src/
RUN pip install --upgrade pip && pip install -r requirements.txt
COPY . /code/
