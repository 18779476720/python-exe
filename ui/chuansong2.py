import glob
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