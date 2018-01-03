import requests

winnerURL = 'http://c6.wap.com/api/v1/orderdata/me/orders/findTopWinners?clientId=31'
response = requests.get(winnerURL)
jsonArray = response.json()


class Winner(object):
    username = ''
    winning_amount = 0

    def __init__(self, loads):
        self.__dict__ = loads
        self.username = loads['username']
        self.winning_amount = loads['winningAmount']


count = 0
for jsonData in jsonArray:
    winner = Winner(jsonData)
    if winner.winning_amount >= 500:
        count = count + 1
        print(str(count) + " : " + winner.username + " : " + str(winner.winning_amount))


print(count)
