from tkinter import *
import requests
import time

root = Tk()
root.title("Python Learning")
root.geometry('300x150+650+400')

# 创建一个输入文本框
tokenText = Entry(root)
tokenText.place(x=50, y=30, width=200, height=20)
tokenText.focus()


def get_balance(token):
    headers = {
        'Content-Type': 'application/json',
        'device_token': '6b1afd2c9a54907d1c6ccd8e9b3bc99c',
        'authorization': 'bearer ' + token,
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1'
    }
    balance_url = 'http://c6.wap.com/api/v1/balance/me'
    time1 = round(time.time() * 1000)
    response = requests.get(balance_url, headers=headers)
    time2 = round(time.time() * 1000)
    print("请求用时 %d ms" % (time2 - time1))
    if(response.text.__contains__("balance")):
        return response.json()["balance"]
    else:
        print(response.content)
        return 0.0


# 创建一个按钮
def update_balance():
    token = tokenText.get()
    balance = get_balance(token)
    balanceLabel["text"] = balance


balanceButton = Button(root, text="UpdateBalance", command=update_balance)
balanceButton.place(x=50, y=60, width=100, height=30)

# 创建一个标签控件
balanceLabel = Label(root, text="0.0")
balanceLabel.place(x=170, y=60, width=80, height=30)

root.mainloop()
