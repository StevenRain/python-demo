import requests
import time
import json

# python http post请求练习
bettingHeaders = {
    'Content-Type': 'application/json',
    'device_token': '6b1afd2c9a54907d1c6ccd8e9b3bc99c',
    'authorization': 'bearer de2b5766-adae-44b5-aca8-d5b57c5a1836',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1'
}

bettingObject = {
  "betEntries": [
    {
      "amount": 2,
      "betString": "01 03",
      "gameplayMethod": "R2",
      "numberOfUnits": 1,
      "pricePerUnit": 2,
      "returnMoneyRatio": 0
    }
  ],
  "drawIdentifier": {
    "gameUniqueId": "HF_SHD11",
    "issueNum": "20171227058"
  },
  "numberOfUnits": 1,
  "purchaseInfo": {"purchaseType": "METHOD_UNDEFINED"},
  "totalAmount": 2.0,
  "userSubmitTimestampMillis": 0
}

time1 = round(time.time() * 1000)
gameIssueNoURL = "http://c6.wap.com/api/v1/result/service/mobile/results/currentTwo/HF_SHD11"
response = requests.get(gameIssueNoURL)
currentGameIssueNo = response.json()['current']['uniqueIssueNumber']
currentTimestamp = round(time.time() * 1000)
bettingObject['drawIdentifier']['issueNum'] = currentGameIssueNo
bettingObject['userSubmitTimestampMillis'] = currentTimestamp

bettingURL = "http://c6.wap.com/api/v1/ordercap/me"
response = requests.post(bettingURL, json=bettingObject, headers=bettingHeaders)

if response.text.__contains__('transactionId'):
    print("投注成功，订单号 : %s" % json.loads(response.text)['transactionId'])
else:
    print("投注失败，返回消息 : %s" % json.loads(response.text)['message'])

time2 = round(time.time() * 1000)
print("用时 %d ms" % (time2 - time1))

