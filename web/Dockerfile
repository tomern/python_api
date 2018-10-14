FROM python:latest
COPY web /app
WORKDIR app
RUN pip install -r requirements.txt
CMD ['python', 'app.py']