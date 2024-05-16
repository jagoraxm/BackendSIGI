FROM python:3.10-slim-buster
COPY . /app
WORKDIR /app
ADD . /app
RUN pip install -r requirements.txt
# Bind to all network interfaces so that it can be mapped to the host OS
CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0", "--port=5000"]
