From python:3
WORKDIR /usr/src/app
COPY requirments.txt .
RUN pip install --no-cache-dir -r requirments.txt
COPY . .
CMD ["python","API_Resource.py"]
