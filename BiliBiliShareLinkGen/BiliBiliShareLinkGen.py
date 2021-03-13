import requests
from hashlib import md5

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

avid = input("AVID: ").replace("av", "").replace("AV", "")

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
