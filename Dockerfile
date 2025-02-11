# Use the official Python image from Docker Hub
FROM python:3.8-slim

# Set work directory in the container
WORKDIR /app

# Copy project files into the docker image
COPY . .

# Install project dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Default port to use if one isn't available in the environment
ENV PORT=5000

# Set flask to run in production or development based on availability of PORT in environment
ENV FLASK_ENV=${FLASK_ENV:-development}
ENV FLASK_APP=app.py

# Expose the chosen port
EXPOSE $PORT

# The command to run your application
# CMD if [ "$FLASK_ENV" = "production" ] ; then gunicorn -b :$PORT app:app ; else flask run --host=0.0.0.0 --port=$PORT ; fi
CMD if [ "$FLASK_ENV" = "production" ] ; then hypercorn app:asgi_app --host 0.0.0.0 --port $PORT ; else flask run --host=0.0.0.0 --port=$PORT ; fi