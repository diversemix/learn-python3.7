FROM python:3.7-alpine

RUN mkdir /opt/app
WORKDIR /opt/app

# For now just copy everything
COPY ./ ./

RUN pip install --no-cache-dir -r requirements.txt
RUN mkdir -p /usr/src/app/log

CMD ["python3", "./app.py"]
