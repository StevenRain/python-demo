import requests
import redis
import json

winnerURL = 'http://c6.wap.com/api/v1/orderdata/me/orders/findTopWinners?clientId=31'
response = requests.get(winnerURL)
jsonArray = response.json()

HOST = "192.168.1.57"
PORT = 6379
DB = 0
conn = redis.Redis(host=HOST, port=PORT, db=DB)


class Winner(object):
    username = ''
    winning_amount = 0

    def __init__(self, loads):
        self.__dict__ = loads
        self.username = loads['username']
        self.winning_amount = loads['winningAmount']


total = 0
countForWinnersWhenWinAmountGreaterThan500 = 0
for jsonData in jsonArray:
    winner = Winner(jsonData)
    total = total + 1
    # print(str(total) + " : " + winner.username + " : " + str(winner.winning_amount))
    if winner.winning_amount >= 500:
        countForWinnersWhenWinAmountGreaterThan500 = countForWinnersWhenWinAmountGreaterThan500 + 1


keyForTopWinners = "order:topwinners:topwinnersByclient:31"
keyForFinalWinners = "order:topwinners:finalWinnersByclient:31"
data = conn.get(keyForFinalWinners)
jsonArray = json.loads(data)

countForFinalWinners = 0
for jsonData in jsonArray:
    countForFinalWinners = countForFinalWinners + 1


data = conn.get(keyForTopWinners)
jsonArray = json.loads(data)
countForTopWinners = 0
for jsonData in jsonArray:
    countForTopWinners = countForTopWinners + 1


if countForTopWinners == 20:
    print("TopWinners共 %d 个，测试通过" % countForTopWinners)
else:
    raise Exception("TopWinners共 %d 个，测试失败" % countForTopWinners)

if countForFinalWinners >= 39:
    print("榜单共 %d 个，测试通过" % countForFinalWinners)
else:
    raise Exception("榜单共 %d 个，测试失败" % countForFinalWinners)

if countForWinnersWhenWinAmountGreaterThan500 >= 20:
    print("中奖超过500的用户共有 %d 个，测试通过" % countForWinnersWhenWinAmountGreaterThan500)
else:
    raise Exception("测试失败，中奖超过500的用户数量为 %d" % countForWinnersWhenWinAmountGreaterThan500)

