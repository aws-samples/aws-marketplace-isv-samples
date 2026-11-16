FROM python:3.14-alpine
ENV PYTHONUNBUFFERED=1

ARG PRODUCT_CODE
ARG PRODUCT_ID
ARG ISSUER_FOOTPRINT
ENV PROD_CODE=$PRODUCT_CODE
ENV PROD_ID=$PRODUCT_ID
ENV ISSUER_FT=$ISSUER_FOOTPRINT

COPY app /app
COPY requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
WORKDIR /app
EXPOSE 8000
CMD ["python","app.py"]