# Use an official Python runtime as a parent image
FROM python:3.6

WORKDIR /client
COPY . /client
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Run app.py when the container launches
ENTRYPOINT ["python", "client.py"]
