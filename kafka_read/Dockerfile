FROM python:3.9-slim

RUN pip install --upgrade pip

WORKDIR /kafka_read
COPY requirements.txt .
RUN python3 -m pip install -r ./requirements.txt

COPY ./main.py .

ENTRYPOINT ["python", "-u", "main.py"]
