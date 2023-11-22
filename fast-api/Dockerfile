FROM --platform=linux/amd64 python:3.11.0

WORKDIR /fastapi/

COPY requirements.txt /fastapi/requirements.txt

RUN pip install --upgrade pip
RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY app/ /fastapi/

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]