ARG PORT=433
FROM cypress/browsers:latest
RUN echo $(python3 -m site --user-base)
COPY requirments.txt .
ENV PATH /home/root/.local/bin:${PATH}
RUN apt-get update && \
    apt-get install -y python3 python3-pip python3-venv && \
    python3 -m pip install --upgrade pip && \
    pip install --break-system-packages -r requirements.txt
COPY . .
CMD unicorn main:app --host 0.0.0.0 --port $PORT


