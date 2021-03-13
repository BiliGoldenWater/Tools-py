from playsound import playsound

import requests
import time
import os


def get_room_info(roomid):
    result = requests.request("get",
                              "http://api.live.bilibili.com/room/v1/Room/room_init?id={}"
                              .format(roomid))
    return result.json()


i = 0
opened = False
rid = 953650
while True:
    print("\r\033[0;34m获取中\033[0m", end="")
    status = get_room_info(rid).json()["data"]["live_status"]

    if status == 0:
        print("\r\033[0;31m未开播\033[0m {}".format(i), end="")
        opened = False

    elif status == 1:
        print("\r\033[0;32m直播中\033[0m {}".format(i), end="")
        if not opened:
            # os.system(r'"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Edge.lnk" '
            #           r"https://live.bilibili.com/{}".format(rid))
            playsound("musics/startLive.mp3", block=True)
            opened = True

    elif status == 2:
        print("\r\033[0;33m轮播中\033[0m {}".format(i), end="")
        opened = False

    i += 1
    time.sleep(1)
