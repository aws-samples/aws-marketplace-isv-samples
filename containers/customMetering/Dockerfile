FROM python:3.8-alpine
ENV PYTHONUNBUFFERED=1

ARG PRODUCT_CODE
ENV PROD_CODE=$PRODUCT_CODE

COPY app /app
COPY requirements.txt /requirements.txt
RUN pip install -r requirements.txt
WORKDIR /app
EXPOSE 8000

ENTRYPOINT ["python","app.py"]