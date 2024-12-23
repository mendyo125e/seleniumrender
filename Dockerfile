ARG PORT=433
FROM cypress/browsers:latest
RUN apt-get install python3 -y
RUN echo $(python3 -m site --user-base)
COPY requirments.txt .
ENV PATH /home/root/.local/bin:${PATH}
RUN apt-get update 
RUN apt-get install -y python3-pip
RUN python3 -m pip install --upgrade pip -q
RUN python3 -m pip install selenium==4.6.0
RUN python3 -m pip install webdriver_manager==3.8.4
RUN python3 -m pip install flask-restfull==0.3.9
RUN python3 -m pip install fastapi[all]
RUN python3 -m pip install uvicorn
RUN python3 -m pip install aiofiles
COPY . .
CMD unicorn main:app --host 0.0.0.0 --port $PORT


