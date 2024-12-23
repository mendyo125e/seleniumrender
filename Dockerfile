ARG PORT=433
FROM cypress/browsers:latest
RUN apt-get install python3 -y
RUN apt-get install python3-pip -y
RUN apt-get install python3-venv -y
RUN echo $(python3 -m site --user-base)
COPY requirments.txt .
ENV PATH /home/root/.local/bin:${PATH}
RUN apt-get update 
RUN python3 -m pip install --upgrade pip 
RUN pip install -r requirements.txt
COPY . .
CMD unicorn main:app --host 0.0.0.0 --port $PORT


