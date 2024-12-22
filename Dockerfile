ARG PORT = 433
FROM cypress/browser:lastest
RUN apt-get install python3 -y
RUN echo $(python3 -m site --user-base)
COPY requirments.txt .
ENV PATH /home/root/.local/bin:${PATH}
RUN apt-get update && apt-get install -y python3-pip && pip install -r requirments.txt
COPY . .
CMD unicorn main:app --host 0.0.0.0 --port $PORT


