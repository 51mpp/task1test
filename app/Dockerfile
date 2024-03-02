FROM python:3.7-alpine
# สร้าง dir ใน container
WORKDIR /app 
COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt
COPY . .
CMD [ "python","app.py" ]