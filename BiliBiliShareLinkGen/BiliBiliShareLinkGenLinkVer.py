import requests
from selenium import webdriver
from hashlib import md5

from selenium.webdriver.chrome.options import Options


def get_aid(url):
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(executable_path=r"D:\Tools\ChromeDriver\chromedriver.exe",
                              options=chrome_options)
    driver.get(video_url)
    aid = driver.execute_script("return aid;")
    driver.quit()
    return aid


url_link = "https://api.bilibili.com/x/share/click"

data_json = {
    "build": 1,
    "buvid": "md5",
    "platform": "windows",
    "oid": "avid",
    "share_channel": "COPY",
    "share_id": "main.ugc-video-detail.0.0.pv",
    "share_mode": 1
}

video_url = input("Link: ")

avid = get_aid(video_url)
print("aid: {}".format(avid))

link_md5 = md5(avid.encode()).hexdigest()

data_json["buvid"] = link_md5
data_json["oid"] = avid

result_data = requests.post(url_link, json=data_json).json()

status_code = result_data["code"]

if status_code == 0 and result_data["data"] != {}:
    data = result_data["data"]
    link = data["content"]
    print("链接为: {}".format(link))
else:
    print("请求错误 返回:{}".format(result_data))
