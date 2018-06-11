import re
import string
import os
import glob
import sys

def lobpunc(txt, txtnew, txtnewnew):
     #ลบเครื่องหมายต่าง ๆ ที่ไม่ต้องการ
     with open(txt, "r", encoding='utf-8') as f:
          with open(txtnew, "w", encoding='utf-8') as f1:
               for line in f:
                    line = re.sub(r'^https?:\/\/.*[\r\n]*', '', line, flags=re.MULTILINE)
                    s = ["...", "\"", "\'", "<NE>", "</NE>", "?", "-", "+", " ", ".", ":", ";", "<AB>", "</AB>", "/", "(", ")", ",", "[", "]", "*", "@", "POEM", "<", ">"] 
                    for m in s:
                         line = line.replace(m, "")
                    for m in ["|", "\n", "  "]:
                         line = line.replace(m, " ")
                    while "  " in line:
                         line = line.replace("  ", " ")
                    for m in string.printable:
                         if m != " ":
                              line = line.replace(m, "")
                    f1.write(line)
               f1.close()
               f.close()
     #ทำให้ multispace กลายเป็น 1 space
     with open(txtnew, "r", encoding='utf-8') as f1:                 
          with open(txtnewnew, "w", encoding='utf-8') as f2:
               for line in f1:
                    while "  " in line:
                         line = line.replace("  ", " ")
                    f2.write(line)
               f1.close()
               f2.close()

#รวมไฟล์ทั้งหมดเป็นไฟล์เดียว 
def romfile(txt, txtnew):
     with open(txt, "r", encoding='utf-8') as f:
          with open(txtnew, "a", encoding='utf-8') as f1:
               for line in f:
                    f1.write(line)
               f1.close()
               f.close()
                         

def triam(path):
     dir_path = os.path.dirname(os.path.realpath(__file__)) #ที่อยู่ปัจจุบันของไฟล์นี้ 
     directory = dir_path+'/result/first_mod'
     directory1 = dir_path+'/result/second_mod'

     if not os.path.exists(directory):
         os.makedirs(directory)

     if not os.path.exists(directory1):
         os.makedirs(directory1)

     #สร้างไฟล์ใหม่ที่เกิดจากการตัดเครื่องหมาย ชื่อไฟล์ว่า first_mod...
     #และสร้างไฟล์ที่นำไฟล์ first_mod มาตัด multiple space ให้เหลือ 1 space ชื่อไฟล์ว่า second_mod...
     #ไฟล์ first_mod อยู่ในโฟลเดอร์ first_mod ไฟล์ second_mod อยู่ในโฟลเดอร์ second_mod ทั้งสองโฟลเดอร์อยู่ในโฟลเดอร์ result 
     for filename in glob.glob(os.path.join(path, '*.txt')):
          lobpunc(filename, directory+"/first_mod_"+filename.replace(path, ""), directory1+"/second_mod_"+filename.replace(path, ""))

     #นำไฟล์ second_mod... ทั้งหมดมารวมกัน ได้ไฟล์เดียวชื่อ romfile อยู่ในโฟลเดอร์ result 
     for directory1 in glob.glob(os.path.join(directory1, '*.txt')):
          romfile(directory1, dir_path+"/result/third_romfile.txt")

#ใส่ตำแหน่งของโฟลเดอร์ที่รวมโฟลเดอร์ที่มีไฟล์ .txt ไว้ 
path_to_directory = '/Users/bigmorning/Desktop/sasomkam/' 
for m in glob.glob(os.path.join(path_to_directory, "*", "")):
     triam(m)
     print(str(m))
