import requests
import time

timestamp1 = int(round(time.time() * 1000))
# url = "http://c6.wap.com/api/v1/orderdata/me/orders/findTopWinners?clientId=31"
url = "https://106caipiao.com/api/v1/orderdata/me/orders/findTopWinners?clientId=7"
response = requests.get(url)
timestamp2 = int(round(time.time() * 1000))
print("请求用时 %d ms" % (timestamp2 - timestamp1))
content = response.text

# 解析json数组(两种方法)
# data = json.loads(content)
jsonArray = response.json()
print(jsonArray)
# 反序列化json


class Winner(object):
    username = ''
    winning_amount = 0
    game_name = ''
    game_issue_no = ''
    timestamp_in_milliseconds = 0

    def __init__(self, loads):
        self.__dict__ = loads
        self.winning_amount = loads['winningAmount']
        self.game_name = loads['gameNameInChinese']
        self.game_issue_no = loads['gameIssueNo']
        self.timestamp_in_milliseconds = loads['timestamp']


for jsonData in jsonArray:
    winner = Winner(jsonData)
    print("%s   %0.2f" % (winner.username, winner.winning_amount))
