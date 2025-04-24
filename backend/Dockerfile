FROM python:3.10

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

# RUN pip install git+https://github.com/shiau109/QCAT


COPY . .
COPY ./app /app/app
COPY ./libs /app/libs

ENV PYTHONPATH="/app/libs:${PYTHONPATH}"

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
