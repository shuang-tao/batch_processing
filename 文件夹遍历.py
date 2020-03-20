import os
import os,shutil


def getfilelist(filepath,newfilepath):
    try:
        filelist =  os.listdir(filepath)
        #遍历父目录文件路径
        for i in range(len(filelist)):
            zhu = os.path.join(filepath, filelist[i])      
            if os.path.isdir(zhu) == True:
                ci=os.listdir(zhu)
                #遍历子目录中路径
                for j in range(len(ci)):
                    ci2 = os.path.join(zhu,ci[j])
                    mulu = os.path.isdir(ci2)
                    #判断子目录内是否包含文件夹
                    if mulu == True:
                        #print('是目录',ci2 ,filelist[i],ci[j],zhu)
                        gai=newfilepath + filelist[i] + '-'+ ci[j]
                        os.rename(ci2,gai)
                        print('子目录移动成功：',gai)
                    else:
                        try:
                            gai2= newfilepath + filelist[i]
                            os.rename(zhu,gai2)
                        except:
                            print('文件所在目录已移动')
                        print('目录移动成功：',gai2)
            else:
                print('跳过该路径：（该路径不为目录）',zhu)
    except Exception as ex:
        print(ex)
        input("按回车键退出。。。")
        
                                
def delfilelist(filepath):
    
    filelist =  os.listdir(filepath)
    for i in range(len(filelist)):
        zhu = os.path.join(filepath, filelist[i])
        os.rmdir(zhu)
        print("删除空文件夹：",filelist[i],"  成功")


def y_or_n():
    y_n=input("是否开始处理y/n:")
    if y_n == 'y':
        print('=====================开始处理=====================')
        getfilelist(filepath,newfilepath)
        print('====================删除空目录====================')
        delfilelist(filepath)
        print("=============该目录下所有档案处理完毕=============")
        input("按回车键退出。。。")
    else:
        if y_n =='n':
            print("程序已结束运行")
            input("按回车键退出。。。")
        else:
            print("输入不合规（请输入y或n）")
            y_or_n()



#########################################################################

#遍历文件根指向
filepath = input("请输入需处理文件夹路径：")
#处理后文件流向
newfilepath=input("请输入处理后文件夹存放路径：") 
#处理文件夹
print("需处理文件夹路径为:",filepath)
print("处理后文件夹存放路径:",newfilepath)
#获取用户输入数据
y_or_n()






            
