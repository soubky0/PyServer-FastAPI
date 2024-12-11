FROM python:3.9-slim

RUN useradd -m -d /home/restricted_user -s /usr/bin/python3 restricted_user

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

USER restricted_user

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
