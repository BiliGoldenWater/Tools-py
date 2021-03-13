import requests
import time


def get_fans_num(uid):
    result = requests.request("get", "https://api.bilibili.com/x/relation/stat?vmid={}".format(uid))
    return result.json()["data"]["follower"]


while True:
    print("现:{}".format(get_fans_num(297786973)))
    print("旧:{}".format(get_fans_num(319341196)))
    time.sleep(0.5)
