FROM --platform=linux/amd64 python:3.11.0-alpine

WORKDIR /fastapi/

COPY app/ /fastapi/
COPY requirements.txt /fastapi/requirements.txt

RUN pip install --no-cache-dir --upgrade -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]