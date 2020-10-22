FROM python:3.8
MAINTAINER Heightline <teamheightline@mail.com>

# проверяем окружение python
RUN python3 --version
RUN pip3 --version

# задаем рабочую директорию для контейнера
RUN mkdir /app
WORKDIR  /app

#ADD . /app/
COPY . /app/

# устанавливаем зависимости python
COPY requirements.txt /app/
RUN pip install -r ./requirements.txt

RUN cd /app

#RUN python3 ./bot.py

# запускаем приложение Python
#CMD ["python", "bot.py"]

