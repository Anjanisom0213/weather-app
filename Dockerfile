
FROM python:3.9-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

RUN pip install markupsafe==2.0.1

EXPOSE 5000

CMD ["python", "app.py"]

