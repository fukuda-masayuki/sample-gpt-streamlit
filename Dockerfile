FROM python:3.10

COPY src/requirements.txt .

RUN pip3 install --upgrade pip
RUN pip3 install --no-cache-dir -r requirements.txt

WORKDIR /src

COPY /src /src
EXPOSE 8080


