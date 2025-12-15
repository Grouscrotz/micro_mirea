# Dockerfile
FROM python:3.11-slim

# Создаем рабочую директорию
WORKDIR /app

# Копируем requirements и устанавливаем
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем ВСЮ папку app в /app
COPY app/ .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]