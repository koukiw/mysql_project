FROM python:3.9
ENV PYTHONUNBUFFERED 1
RUN mkdir /src
WORKDIR /src

RUN apt update
RUN apt install -y unoconv libreoffice vim
COPY init.sh /src/
COPY requirements.txt /src/
RUN pip install --upgrade pip && pip install -r requirements.txt
COPY . /code/
RUN apt install fonts-noto-cjk

# init.sh に実行権限を与える
# RUN chmod +x /src/init.sh
# # init.shを実行するコマンドを追加する
# CMD ["bin/bash", "/src/init.sh"]
