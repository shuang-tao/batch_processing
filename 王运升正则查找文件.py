import re
import os

def bianli1(mulu,mulu2):
   fr = open('G:\MapInfo.txt', 'r+')
   #print(fr.readlines())
   lines = fr.readlines()
   for line in lines:
      zhengze = line.strip()
      num=re.finditer(r"(?<=(\x7c))(.*?)(?=(\s))",zhengze)
      for i in num:
         #print(i.group())
         mingzi1=mulu + i.group()+".map"
         mingzi2=mulu2 + i.group()+".map"
         try:
            os.rename(mingzi1,mingzi2)
            print(mingzi1,mingzi2)
         except:
            print("找不到该文件",mingzi1)

def bianli2(mulu,mulu2):
   fr = open('G:\MapInfo.txt', 'r+')
   #print(fr.readlines())
   lines = fr.readlines()
   for line in lines:
      zhengze = line.strip()
      #((?!(\x7c)).)*
      num=re.finditer(r"(?<=(\x5b))(.*?)(?=(\s))",zhengze)
      for i in num:
         #print(i.group())
         mingzi1=mulu + i.group()+".map"
         mingzi2=mulu2 + i.group()+".map"
         try:
            os.rename(mingzi1,mingzi2)
            print(mingzi1,mingzi2)
         except:
            print("找不到该文件",mingzi1)


################################################################
  
mulu="G://map//"
mulu2="G://map2//"
bianli1(mulu,mulu2)
bianli2(mulu,mulu2)
