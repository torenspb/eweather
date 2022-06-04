FROM python:3.8-alpine
RUN pip install --no-cache-dir flask==2.1.2 feedparser==6.0.10
WORKDIR /opt/eweather/
COPY app.py .
COPY templates/ templates/
COPY static/ static/
EXPOSE 80/tcp
ENTRYPOINT ["python"]
CMD ["-m", "flask", "run", "--host=0.0.0.0", "--port=80"]