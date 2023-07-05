FROM python:3.11-slim

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . /apps/build_system
WORKDIR /apps/build_system

EXPOSE 8111

CMD ["uvicorn", "src.app:app", "--workers", "1", "--host", "0.0.0.0", "--port", "8111"]
