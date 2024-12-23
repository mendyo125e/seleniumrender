ARG PORT=433
FROM cypress/browsers:latest
RUN apt-get install python3 -y
RUN echo $(python3 -m site --user-base)
COPY requirments.txt .
ENV PATH /home/root/.local/bin:${PATH}
RUN apt-get update 
RUN apt-get install -y python3-pip
RUN pip3 install selenium==4.6.0
RUN pip3 install webdriver_manager==3.8.4
RUN pip3 install flask-restfull==0.3.9
RUN pip3 install fastapi[all]
RUN pip3 install uvicorn
RUN pip3 install aiofiles
COPY . .
CMD unicorn main:app --host 0.0.0.0 --port $PORT


