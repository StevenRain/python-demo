import requests
import json
import sys

url = "http://192.168.1.25:8006/api/v1/reptile/su/ignoreMessage"

# 25
headers = {
    'Content-Type': 'application/json',
    'authorization': 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJjcHRlc3QiLCJpYXQiOjE1Mjk4OTYzNjgsInJvbGUiOiJBRE1JTiIsInVzZXJuYW1lIjoiY3B0ZXN0In0.Q4j2naT6zhUpuStXImqBZo6gknGjzseZAEBJrzycoGc'
}

gameUniqueIdList = {
    "HF_CQSSC","HF_XJSSC","HF_TJSSC","HF_AHD11","HF_GDD11","HF_JXD11","HF_SDD11","HF_SHD11","HF_AHK3","HF_GXK3","HF_JSK3",
    "HF_BJK3","HF_JLK3","HF_GDKL10F","HF_CQKL10F","HF_BJPK10","HF_XYFT","HF_BJ28","HF_SHSSL","MARK_SIX","PL3","X3D","QXC"
}


def clean_by_game_unique_id(gameUniqueId):
    # json_pattern = '{"gameUniqueId":"%s"}'
    # json_string = json_pattern % gameUniqueId
    # data = json.loads(json_string)
    #
    # response = requests.put(url, json=data, headers=headers)
    # print(data)
    # print(response.text)
    print(gameUniqueId)


try:
    gameUniqueId = sys.argv[1]
except:
    gameUniqueId = ''


if gameUniqueId:
    clean_by_game_unique_id(gameUniqueId)
else:
    for gameUniqueId in gameUniqueIdList:
        clean_by_game_unique_id(gameUniqueId)