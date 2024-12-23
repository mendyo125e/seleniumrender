from typing import Optional
from fastapi import FastAPI
import aiofiles,json
from fastapi.responses import HTMLResponse, JSONResponse
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import urllib3,urllib.parse
import random,time
import os
import random
app = FastAPI()
def random_color_by_name(testcolor):
    if testcolor=="test":
        color_names = [
            "blue", "green", "orange","red", "lightblue","grey","black","white" ,"yellow" ,"purple" ,"pink" ,"brown" ,"cyan","magenta","lime","gold","teal","navy","olive","maroon"       
        ]
    else:
        color_names = [
            "blue", "green", "orange","red", "lightblue","grey","black" 
        ]
    # Chọn ngẫu nhiên một  màu
    return random.choice(color_names)
def updatestatus(user,url,cookie):
    # Khởi tạo PoolManager
    http = urllib3.PoolManager()
    # URL API cần gửi yêu cầu
    data = {'namefolder': f'{user}',"cookie": cookie,}
    encoded_data = json.dumps(data).encode('utf-8')
    response = http.request( 'POST',   url,  body=encoded_data,   headers={'Content-Type': 'application/json'})
    return {"status_code": response.status,"response": response.data.decode('utf-8')}
def send_alertzy_notification(account_key, title, message,priority, group, buttons=None):
    url = "https://alertzy.app/send"
    data = {"accountKey": account_key,"title": title,"message": message,"group": group,}
    data["priority"]=priority
    if buttons:
        data["buttons"] = json.dumps(buttons)
    http = urllib3.PoolManager()
    response = http.request('POST',url,fields=data)
    return {"status_code": response.status,"response": response.data.decode('utf-8')}
def guisms(account_key,user,message,chotot):
    http = urllib3.PoolManager()
    data = {"token": account_key,"user": user,"message": message,"sound": chotot,}
    encoded_data = urllib.parse.urlencode(data).encode("utf-8")  # Phải encode thành bytes
    response = http.request(
        "POST",
        "https://api.pushover.net/1/messages.json",
        body=encoded_data,
        headers={"Content-Type": "application/x-www-form-urlencoded"},
    )
    return {"status_code": response.status,"response": response.data.decode('utf-8')}
def guismssystem(title,message,nologin,random_color):
    # Khởi tạo PoolManager
    http = urllib3.PoolManager()
    # URL API cần gửi yêu cầu
    url = 'https://hieuphp.name.vn/api/undetected/message.php?all=1'
    data = {'title': f'{title}','message': f'{message}','nologin': f'{nologin}','random_color': f'{random_color}'}
    encoded_data = json.dumps(data).encode('utf-8')
    response = http.request( 'POST',   url,  body=encoded_data,   headers={'Content-Type': 'application/json'})
    return {"status_code": response.status,"response": response.data.decode('utf-8')}
def convert_boolean_values(cookie):
    # Kiểm tra nếu cookie là kiểu dict
    if isinstance(cookie, dict):
        for key, value in cookie.items():
            if isinstance(value, bool):
                cookie[key] = value  # Đảm bảo giá trị boolean đúng (True/False)
    return cookie
def fetch_data_from_api(url):
    http = urllib3.PoolManager()
    response = http.request('GET', url)
    if response.status == 200:
        try:
            data = json.loads(response.data.decode('utf-8'))
            return data
        except json.JSONDecodeError:
            print("Lỗi khi giải mã dữ liệu JSON.")
            return None
    else:
        print(f"Lỗi khi gửi yêu cầu GET, mã trạng thái: {response.status}")
        return None
def lambda_handler():
    # Cấu hình trình duyệt
    chrome_options = Options()
    #chrome_options.add_argument("--headless")  # Chạy chế độ không giao diện
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_argument("--disable-notifications")
    message_value = 0 
    i=0
    vonglap=True
    url = "https://hieuphp.name.vn/api/undetected/systemapi.php?all=1"  
    data = fetch_data_from_api(url)
    namesms = data.get("name", None)
    tokensms = data.get("token", None)
    usersms = data.get("user", None)
    random_color = random_color_by_name(namesms)
    # Khởi tạo WebDriver 
    try:
        url = "https://hieuphp.name.vn/api/undetected/getdata.php"  
        data = fetch_data_from_api(url)
        try:
            message_value = data.get("message", None)
        except Exception as e:
            message_value=0
            
        if message_value!=1:
            # In dữ liệu trả về (có thể tùy chỉnh để chỉ lấy các trường cụ thể)
           
            for record in data:
               
                #print(f"Email: {record.get('email', 'Không có email')}")
                cookie_data=record.get('cookie', 'Không có cookie')
                cookies = json.loads(cookie_data)
                 #cookies = cookie_dict.get("cookies", [])
                #print(f"Cookie: {cookies}") 
                namefolder=record.get('namefolder', 'Không có namefolder')
                #print(f"Name Folder: {namefolder}")
                nameapp=record.get('nameapp', 'Không có nameapp')
                #print(f"Name App: {nameapp}")
                cookieactive=record.get('cookieactive', 'Không có cookieactive')
                #print(f"Cookie Active: {cookieactive}")
                testversion=record.get('testversion', 'Không có testversion')
                #print(f"Test Version: {testversion}")
                testbodyelement=record.get('testbodyelement', 'Không có testbodyelement')
                print(f"Test Body Element: {testbodyelement}")
                viewtmp=record.get('viewtmp', 'Không có xem tmp')
                print(f"Xem tmp: {viewtmp}")
                nhansms=record.get('nhansms', 'Không có nhansms')
                print(f"nhansms: {nhansms}")
                noidungtin=record.get('noidungtin', 'Không có noidungtin')
                print(f"noidungtin: {noidungtin}")
                status=record.get('status', 'Không có status')
                print(f"Status: {status}") 
                                   
        else:
            print("Đã kiểm tra hết các trang")
            url = "https://hieuphp.name.vn/api/undetected/updatestatus.php?all=1"  
            fetch_data_from_api(url)
            vonglap=False
        chrome_options = Options()

        #chrome_options.browser_version = "130"
       #chrome_options.platform_name = "Windows 10"
        #lt_options = {};
        #lt_options["username"] = "alexschmidt63ng";
        #lt_options["accessKey"] = "evq0nRPGqRSZOQtu2hcYW2xy18CgxDjUotY1vYFD491PfVxPcd";
        #lt_options["smartUI.project"] = "alexschmidt63ng";
        #lt_options["resolution"] = "1024x768";
        #lt_options["recordVideo"] = "true";
        #lt_options["browserName"] = "Chrome";
        #lt_options["w3c"] = True;
        #lt_options["selenium_version"] = "4.0.0";
        #lt_options["plugin"] = "python-python";
        #chrome_options.set_capability('LT:Options', lt_options);

         #driver = webdriver.Remote(command_executor="http://hub.lambdatest.com:80/wd/hub",options=chrome_options)
        driver = webdriver.Remote(command_executor="http://10.210.44.94:4444/wd/hub",options=chrome_options)


        print("abc") 
        cookieactive=0
    
        #driver = uc.Chrome(options, driver_executable_path=driver_path, browser_executable_path=browser_path,version_main=108 )
        url="https://www.chotot.com/my-ads"
        driver.get(url)    
        nologin=2        
        time.sleep(1)
        dathemcookie=0
        cookieactive=1   
        if int(cookieactive) == 1:
            for cookie in cookies:
                cookie = convert_boolean_values(cookie)
                loaibo=cookie.get('domain')
                if  loaibo == "www.chotot.com" or loaibo == ".www.chotot.com":
                    print(f"Loại bỏ cookie có domain 'www.chotot.com'")
                    continue 
                # Chuyển đổi expiry từ mili-giây sang giây (nếu có)
                if 'expiry' in cookie and isinstance(cookie['expiry'], (int, float)):
                    if cookie['expiry'] > 1e10:  # Giả sử giá trị lớn hơn 1e10 là mili-giây
                        cookie['expiry'] = int(cookie['expiry'] / 1000)

                if "expirationDate" in cookie:
                    cookie["expiry"] = int(cookie["expirationDate"])  # Chuyển đổi thành 'expiry' 
                    #print(f"cookie thường {cookie}")
                    expirationDate=cookie["expirationDate"]
                    #print(f"cookie thường {expirationDate}")
                    del cookie["expirationDate"]  # Xóa trường không được hỗ trợ
                    

                invalid_fields = ['sameSite', 'storeId', 'session', 'hostOnly']

                for field in invalid_fields:
                    cookie.pop(field, None)  # Loại bỏ các trường không hợp lệ
                
                try:
                    driver.add_cookie(cookie)  # Thêm cookie
                    dathemcookie=1
                except Exception as e:
                    loithemcookie+=1

            #print(f"Số lỗi khi thêm cookie : {loithemcookie} ")
            if dathemcookie==1:
                print("Đã thêm cookie") 
                #driver.refresh() 
                driver.get(url)
                time.sleep(1)
                getcookie=json.dumps(driver.get_cookies())
                url = "https://hieuphp.name.vn/api/undetected/undetected.php?all=1"
                updatestatus1=updatestatus(namefolder,url,getcookie)
                print(f"update sesion theo namefolder: {updatestatus1}")
        time.sleep(0) 
        #fetch_data_from_api(url)      
        if int(testbodyelement) ==1:
            body_element = driver.find_element("tag name", "body").text
            print("Nội dung văn bản của 1 <body>:", body_element)
    
        if int(nhansms) ==1:
            timeout = 3       
            end_time = time.time() + timeout
            while True:
                try:
                # Tìm phần tử chứa chữ "Đăng nhập"

                    unread_count = driver.find_element(By.ID, "chat-unread-count").text
                    
                    if int(unread_count) > 0:
                        priority=2 #priority [0 = Normal (default), 1 = High, 2 = Critical]
                        group = "chotot"
                        buttons = [{"text": f"{nameapp}", "link": "https://chotot.com/", "color":f"{random_color}"}]
                        
                        if int(noidungtin)==0:
                            title = f"{nameapp}: Có {unread_count} tin nhắn"
                            message = f"{nameapp}: bạn {namefolder} có {unread_count} tin nhắn"
                        else:    
                            last_message = driver.find_element(By.CSS_SELECTOR, ".styles_LastMessage__BY5e2.styles_NewMessage__pHpaN").text
                            userchotot = driver.find_element(By.CSS_SELECTOR, ".styles_UserNameTime__B3N7j.text-1-line").text
                            title = f"{nameapp}: Có {unread_count} tin nhắn "
                            message = f"{nameapp}: bạn {namefolder} có khách {userchotot} hỏi {last_message}"    
                        
                        if namesms=="pushover":   
                            result = guisms(tokensms, usersms, message,nameapp)
                        elif namesms=="alertzy":     
                            result = send_alertzy_notification(tokensms, title, message,priority,group, buttons)
                        else:  
                            print(f"nội dung {message}")    
                            result =guismssystem(title,message,nologin,random_color)   
                        print(f"Kết quả đã gửi sms cho {namefolder} {nameapp} {result}")
                        break
                        # Gửi thông báo 

                    
                except Exception as e:
                    time.sleep(1)
                    #print("Đợi tin nhắn")

                if time.time() > end_time:
                    print("Hết giờ không gửi được tin nhắn") 
                    unread_count = driver.find_element(By.ID, "chat-unread-count").text
                    print(f"bcde {unread_count}")
                    time.sleep(0)
                    break
    #time.sleep(1)
        i+=1
        print(f"hết vòng lập sms {i}")
        if int(testversion) ==1:
            driver.get("chrome://version/")
            body_element = driver.find_element("tag name", "body").text
            print("Nội dung văn bản của 1 <body>:", body_element)
        driver.quit()
        url = 'http://hieuphp.name.vn/api/undetected/updatestatus.php'
        updatestatus(namefolder,url,"")     
                             
        time.sleep(1)
        driver.quit()
        return f"Title of the page is"
    except Exception as e:
        return f"Error abc "

@app.get("/", response_class=HTMLResponse)
async def read_index():
    try:
        async with aiofiles.open("index.html", mode="r") as f:
            html_content = await f.read()
        return HTMLResponse(content=html_content, status_code=200)
    except FileNotFoundError:
        return {"error": "index.html not found"}
        
@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    if item_id == 123:
        result = lambda_handler()
        return JSONResponse(content={"item_id": item_id, "result": result})
    return {"item_id": item_id, "q": q}
    

        


