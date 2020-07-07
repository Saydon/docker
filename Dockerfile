FROM python:3

WORKDIR /usr/src/app
COPY requirements.txt requirements.txt
COPY bitcoin.py bitcoin.py
RUN pip install -r requirements.txt
EXPOSE 80
ENTRYPOINT ["python", "bitcoin.py"]