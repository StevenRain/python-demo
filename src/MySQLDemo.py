import mysql.connector as connector
from tkinter import *

HOST = "www.codecenter.store"
PORT = 3306
USER = "root"
PASSWORD = "StevenMichael88"
DB = "video"

root = Tk()
root.title("Python Learning")
root.geometry('520x320+650+400')


def exec_sql(sql):
    try:
        connection = connector.connect(host=HOST, user=USER, password=PASSWORD, db=DB)
        cursor = connection.cursor()
        cursor.execute(sql)
        values = cursor.fetchall()
        cursor.close()
        connection.close()
        return values
    except Exception as e:
        return e


def build_button_pressed():
    username = userText.get()
    password = passwordText.get()
    pattern = "select * from user where username='%s' and password='%s'"
    sql = pattern % (username, password)
    sqlText.delete(0, END)
    sqlText.insert(0, sql)


def exec_button_pressed():
    sql = sqlText.get()
    result = exec_sql(sql)
    consoleText.delete('1.0', END)
    consoleText.insert(END, result)


# 用户名
usernameLabel = Label(root, text="用户名")
usernameLabel.place(x=10, y=30, width=50, height=20)
userText = Entry(root)
userText.place(x=60, y=30, width=400, height=20)
userText.focus()

# 密码
usernameLabel = Label(root, text="密码")
usernameLabel.place(x=10, y=60, width=50, height=20)
passwordText = Entry(root)
passwordText.place(x=60, y=60, width=400, height=20)

# sql 输出
sqlLabel = Label(root, text="sql")
sqlLabel.place(x=10, y=90, width=50, height=20)
sqlText = Entry(root)
sqlText.place(x=60, y=90, width=400, height=20)

# print
consoleText = Text(root, background="black", foreground="green")
consoleText.place(x=60, y=120, width=400, height=150)
consoleText.insert(END, "Console Window")

# 生成sql
submitButton = Button(root, text="生成sql", command=build_button_pressed)
submitButton.place(x=60, y=280, width=100, height=30)

# 执行sql
submitButton = Button(root, text="执行sql", command=exec_button_pressed)
submitButton.place(x=240, y=280, width=100, height=30)

root.mainloop()