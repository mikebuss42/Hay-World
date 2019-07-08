FROM python:3.6-slim-stretch
WORKDIR /app
COPY . /app
CMD ["python3", "HayWorld.py"]
