from tkinter import *

root = Tk()
root.title("Python Learning")
root.geometry('500x350+650+400')

# 1.空窗体
# root.mainloop()

# 2.列表
# languageList = ['C', 'Java', 'Python']
# listA = Listbox(root)
#
# for item in languageList:
#     listA.insert(0, item)
#
# listA.pack()
# root.mainloop()

# 3.按钮
"""
注意，调用place时不能调用pack, 否则place不起作用
"""
def callback():
    print("Button pressed!")


# Button(root, text='TestButton', command=callback).pack(ipadx=10, pady=20, ipady=20)
# Button(root, text='TestButton', command=callback).pack(ipadx=20, pady=20, ipady=20)
button3 = Button(root, text='button3', command=callback)
button3.place(x=40, y=40, width=80, height=40)
root.mainloop()


# import random
# root = Tk()
# # width x height + x_offset + y_offset:
# root.geometry("500x200+30+30")
#
# languages = ['Python', 'Perl', 'C++', 'Java', 'Tcl/Tk']
# labels = range(5)
# for i in range(5):
#     ct = [random.randrange(256) for x in range(3)]
#     brightness = int(round(0.299 * ct[0] + 0.587 * ct[1] + 0.114 * ct[2]))
#     ct_hex = "%02x%02x%02x" % tuple(ct)
#     bg_colour = '#' + "".join(ct_hex)
#     l = Label(root,
#                  text=languages[i],
#                  fg='White' if brightness < 120 else 'Black',
#                  bg=bg_colour)
#     l.place(x=20, y=30 + i * 30, width=120, height=25)
#
#     button = Button(root, text=languages[i], bg=bg_colour)
#     button.place(x=300, y=30 + i * 30, width=120, height=25)
#
# root.mainloop()