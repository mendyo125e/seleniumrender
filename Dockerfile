ARG PORT=433
FROM cypress/browsers:latest
# Cập nhật hệ thống
RUN apt-get install python3 -y
# Nâng cấp pip

RUN python3 -m pip install -r selenium==4.6.0
RUN python3 -m pip install --upgrade pip

# Kiểm tra thư mục cài đặt gói Python
RUN echo $(python3 -m site --user-base)

# Đặt PATH chính xác
ENV PATH $(python3 -m site --user-base)/bin:${PATH}

# Sao chép file yêu cầu (nếu có)
COPY requirments.txt .

# Cài đặt các gói Python
RUN python3 -m pip install selenium==4.6.0
RUN python3 -m pip install webdriver_manager==3.8.4
RUN python3 -m pip install flask-restfull==0.3.9
RUN python3 -m pip install fastapi[all]
RUN python3 -m pip install uvicorn
RUN python3 -m pip install aiofiles

COPY . .
CMD unicorn main:app --host 0.0.0.0 --port $PORT


