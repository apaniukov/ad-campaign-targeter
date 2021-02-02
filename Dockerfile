FROM python:3.9

WORKDIR /project

COPY . .

RUN pip install --upgrade pip && pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "main.py"]
