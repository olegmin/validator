# Базовый образ
FROM python:3.7.3


# Переменная окружения
ENV PYTHONUNBUFFERED 1


# Устанавка зависимостей проекта
ADD requirements.txt .
RUN pip3 install --upgrade pip && \
    pip3 install --trusted-host pypi.python.org -r requirements.txt && \
    rm -f requirements.txt


# Deploy проекта (размещение исходного кода в контейнере)
ADD ./code /appcode


# Рабочая директория проекта
WORKDIR /appcode
