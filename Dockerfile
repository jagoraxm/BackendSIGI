# Use the official Python image from Docker Hub
FROM python:3.8-slim

# Set work directory in the container
WORKDIR /app

# Copy project files into the docker image
COPY . .

# Instalar dependencias del sistema necesarias para algunas librerías de Python
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    libxml2-dev \
    libxslt1-dev \
    python3-dev \
    && apt-get clean

# Actualizar pip a la última versión
RUN pip install --upgrade pip

RUN pip cache purge
# Install project dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Default port to use if one isn't available in the environment
ENV PORT=5000

RUN python --version

# Set flask to run in production or development based on availability of PORT in environment
ENV FLASK_ENV=${FLASK_ENV:-development}
ENV FLASK_APP=app.py

# Expose the chosen port
EXPOSE $PORT

# The command to run your application
# CMD if [ "$FLASK_ENV" = "production" ] ; then gunicorn -b :$PORT app:app ; else flask run --host=0.0.0.0 --port=$PORT ; fi
CMD if [ "$FLASK_ENV" = "production" ] ; then hypercorn app:asgi_app --host 0.0.0.0 --port $PORT ; else flask run --host=0.0.0.0 --port=$PORT ; fi