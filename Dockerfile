FROM python:3.10

COPY requirement.txt .

RUN pip3 install --upgrade pip
RUN pip3 install --no-cache-dir -r requirement.txt

WORKDIR /src

COPY /src /src
EXPOSE 8080

# APIキーを設定してください
ENV OPENAI_API_KEY=

