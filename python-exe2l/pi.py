from tkinter import *
import tkinter as tk
import tkinter . messagebox
import os
import shutil

from docx2pdf import convert

a = [];
records = dict() # 初始化

def getFlist(file_path,out_path):
    for dirpath, dirnames, filenames in os.walk(file_path):
        for file in filenames:
            fullpath = os.path.join(dirpath, file)
            print('fullpath:"' + fullpath)
            # convert("input.docx", "output.pdf")
            convert(fullpath, f"{fullpath}.pdf")  # 转换成pdf文件，但文件名是.docx.pdf，需要重新修改文件名
            shutil.move(dirpath + '\\' + file, out_path + '\\' + file);  # 转换后将word版本与PDF分离
    for dirpath, dirnames, filenames in os.walk(file_path):
        for fullpath in filenames:
            # print(fullpath)
            if '.pdf' in fullpath:
                fullpath_after = os.path.splitext(fullpath)[0]
                fullpath_after = os.path.splitext(fullpath_after)[0]
                fullpath_after = fullpath_after + '.pdf'
                fullpath_after = os.path.join(dirpath + '\\' + fullpath_after)
                # print('fullpath_after:' + fullpath_after)
                fullpath = os.path.join(dirpath, fullpath)
                # print('fullpath:'+fullpath)
                os.rename(fullpath, fullpath_after)

# 移动文件到对应的文件夹


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

    getFlist(file_dir,file_dir2)



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

labe1 = tk.Label(window,text="word文件夹路径：")
labe2 = tk.Label(window,text="pdf文件夹路径：")
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