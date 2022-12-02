from tkinter import *
import tkinter as tk
import tkinter . messagebox
import os
import shutil
a = [];
records = dict() # 初始化

def getFlist(file_dir,file_dir2):
    for root, dirs, files in os.walk(file_dir):
        #print('root_cs:', root);  #当前路径
        #print('sub_cs:', dirs);   #子文件夹
        #print('files:', files);    #文件名称，返回list类型
        print('title', len(root))
        if len(dirs) == 0:
            a.append(root)
            name = os.path.basename(root)
            print('name:',name)
            # 开始寻找对应文件移动到对应的路径中
            movefile(root,name,file_dir2);
    return files;

# 移动文件到对应的文件夹
def movefile(path,name,file_dir2):
    print('进入移动文件步骤')
    for files in os.walk(file_dir2):
        print('files',files[2])
        for file in files[2]:
            contain = name in file;
            print("contian:", contain)
            if contain==True:

                new_path = os.path.join(path, file);
                print('new_path',new_path)
                print('file', file);
                shutil.move(file_dir2+'\\'+file, new_path);

    return

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

labe1 = tk.Label(window,text="文件夹路径：")
labe2 = tk.Label(window,text="pdf路径：")
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