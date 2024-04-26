FROM python:3.12 

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

COPY . . 

EXPOSE 8000

RUN chmod a+x ./django.sh

ENTRYPOINT [ "django.sh" ]