ARG PORT=433
FROM umihico/aws-lambda-selenium-python:latest

RUN dnf install -y git && pip install setuptools && pip install git+https://www.github.com/filipopo/undetected-chromedriver@master

COPY . .
CMD unicorn main:app --host 0.0.0.0 --port $PORT


