import requests
import time
import json
import os
import random


class BiliBiliDanMuLottery:
    def __init__(self, roomid, lottery_key):
        self.url = 'https://api.live.bilibili.com/xlive/web-room/v1/dM/gethistory'
        self.headers = {
            'Host': 'api.live.bilibili.com',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0',
        }
        self.data = {
            'roomid': str(roomid),
            'csrf_token': '',
            'csrf': '',
            'visit_id': '',
        }

        self.danMu_data = []
        self.joinSuccess = []
        self.winning = []

        self.lotteryKey = lottery_key

    def get_danmu(self):
        # 获取直播间弹幕
        html = requests.post(url=self.url, headers=self.headers, data=self.data).json()
        # 解析弹幕列表
        for content in html['data']['room']:
            # 获取昵称
            uid = content['uid']
            nickname = content["nickname"]
            # 获取发言
            text = content['text']
            # 获取发言时间
            timeline = content['timeline']
            # 记录发言
            data = [uid, text, nickname, timeline]
            # 判断对应消息是否存在于日志，如果和最后一条相同则打印并保存
            if data not in self.danMu_data:
                if text == self.lotteryKey:
                    if [uid, nickname] not in self.joinSuccess:
                        self.joinSuccess.append([uid, nickname])
                        print("昵称:{} 参与成功! 当前{}人".format(nickname, len(self.joinSuccess)))
                    else:
                        print("昵称:{} 重复发送! 已过滤!".format(nickname))
                print(data)
                self.danMu_data.append(data)

    def save(self):
        with open("danMu.json", mode="w", encoding="utf-8") as f:
            f.write(json.dumps(self.danMu_data))
        with open("danMuJoinSuccess.json", mode="w", encoding="utf-8") as f:
            f.write(json.dumps(self.joinSuccess))
        with open("winning.json", mode="w", encoding="utf-8") as f:
            f.write(json.dumps(self.winning))
        print("保存成功")

    def close(self):
        self.save()
        print("已关闭")

    def lottery(self):
        if self.joinSuccess:
            winning = random.choice(self.joinSuccess)
            self.winning.append(winning)
            print("恭喜: " + winning[1] + "中奖!")


danMu = BiliBiliDanMuLottery(953650, "a")
isContinue = True
isRecording = True
while isContinue:
    time.sleep(0.1)
    # 获取弹幕
    if isRecording:
        danMu.get_danmu()
    if os.path.exists("start.txt"):  # 开始
        isRecording = True
        os.remove("start.txt")
    elif os.path.exists("pause.txt"):  # 暂停
        isRecording = False
        os.remove("pause.txt")
    elif os.path.exists("save.txt"):  # 保存
        danMu.save()
        os.remove("save.txt")
    elif os.path.exists("close.txt"):  # 关闭
        danMu.close()
        isContinue = False
        os.remove("close.txt")
    elif os.path.exists("lottery.txt"):  # 抽奖
        danMu.lottery()
        os.remove("lottery.txt")
