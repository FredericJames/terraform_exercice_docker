FROM python:3.12.0

WORKDIR /fastapi/

COPY main.py /fastapi/
COPY requirements.txt /fastapi/requirements.txt

RUN pip install --no-cache-dir --upgrade -r requirements.txt


CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]