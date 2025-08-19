FROM python3.12-slim
COPY ./app /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["python", "main.py"]