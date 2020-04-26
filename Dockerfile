FROM python:3.6.1-alpine
COPY ./requirements.txt .
RUN pip install -q -r requirements.txt
CMD ["python","app.py"]
COPY app.py /app.py