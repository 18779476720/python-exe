from tkinter import *
import tkinter as tk
import tkinter . messagebox
import os
import shutil
import os
import time
from win32com import client
from docx2pdf import convert
from wx.lib.agw.shapedbutton import folder

a = [];
records = dict() # 初始化


# 移动文件到对应的文件夹
def doc_to_docx(list_dir, save_file):
    word = client.Dispatch("Word.Application")  # 打开word应用程序
    filename_list = [i for i in list_dir if i.split(".")[-1] == "doc"]
    # filename_list=[os.path.join(folder,j) for j in li ]
    # print(filename_list)
    # time.sleep(10)
    try:
        for file in filename_list:
            print("开始转换:", file)
            # print(file)
            # 将doc的文件名换成后缀为docx的文件
            name = os.path.splitext(file)[0] + '.docx'
            # 将我们的docx与文件保存位置拼接起来，获得绝对路径
            out_name = os.path.join(save_file, name)  #
            print("测试后:", name)
            print("转换后：", out_name)
            # out_file.append(out_name)
            file_path = os.path.join(folder, file)
            doc = word.Documents.Open(file_path)  # 打开word文件
            # doc.SaveAs("{}".format(out_name), 12)  # 另存为后缀为".docx"的文件，其中参数12或16指docx文件
            doc.SaveAs("{}".format(out_name), 12, False, "", True, "", False,
                       False, False,
                       False)  # 转换后的文件,12代表转换后为docx文件
            doc.Close()  # 关闭原来word文件
    except Exception as e:
        print(e)
    word.Quit()


def run(folder,out_dir):
    list_dir = os.listdir(folder)
    # print(list_dir)
    doc_to_docx(list_dir, out_dir)

#开始执行函数

# file_name = getFlist(file_dir,file_dir2)
# print('a:',a)
# print(len(a))

window = Tk()
window.winfo_screenwidth()
window.winfo_screenheight()
window.minsize(350,150)
#root.config(background="#6fb765")
window.title('投行小工具')

def callback():
    file_dir=entryStr1.get()
    file_dir2=entryStr2.get()
    print(entryStr1.get())
    print(entryStr2.get())

    run(file_dir,file_dir2)



def menuCommand() :
    tkinter.messagebox.showinfo("主菜单栏","你正在使用主菜单栏")

frame = Frame(window);
entryStr1=tk.StringVar()
entryStr2=tk.StringVar()
# b = tk.Button(window, text="开始执行", command=callback,).pack()
# entry1 = tk.Entry(window, textvariable=entryStr1, font=("微软雅黑",20)).pack(padx=10, pady=5)
# entry2 = tk.Entry(window, textvariable=entryStr2, font=("微软雅黑",20)).pack(padx=10, pady=5)

b = tk.Button(window, text="开始执行", command=callback)
entry1 = tk.Entry(window, textvariable=entryStr1, font=("微软雅黑",15),)
entry2 = tk.Entry(window, textvariable=entryStr2, font=("微软雅黑",15))

labe1 = tk.Label(window,text="pdf文件夹路径：")
labe2 = tk.Label(window,text="word文件夹路径：")
# main_menu = Menu (window)
# main_menu.add_command (label="文件",command=menuCommand)
# main_menu.add_command (label="编辑",command=menuCommand)
# main_menu.add_command (label="格式",command=menuCommand)
# main_menu.add_command (label="查看",command=menuCommand)
# main_menu.add_command (label="帮助",command=menuCommand)
# #显示菜单
# window.config (menu=main_menu)
labe1.grid(row=0,column=0)
labe2.grid(row=1,column=0)

entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)
b.grid(row=2)

window.mainloop()