import re
import string
def lobpunc(txt, txtnew, txtnewnew):
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
                    #filter(lambda x: x == " " or x not in string.printable, line)
                    for m in string.printable:
                         if m != " ":
                              line = line.replace(m, "")
                    f1.write(line)
               f1.close()
               f.close()
     with open(txtnew, "r", encoding='utf-8') as f1:                 
          with open(txtnewnew, "w", encoding='utf-8') as f2:
               for line in f1:
                    while "  " in line:
                         line = line.replace("  ", " ")
                    f2.write(line)
               f1.close()
               f2.close()

def romfile(txt, txtnew):
     with open(txt, "r", encoding='utf-8') as f:
          with open(txtnew, "a", encoding='utf-8') as f1:
               for line in f:
                    f1.write(line)
               f1.close()
               f.close()
                         

import os
import glob
import sys 
def triam(path):
     dir_path = os.path.dirname(os.path.realpath(__file__))
     directory = dir_path+'/result/mod'
     directory1 = dir_path+'/result/mmod'

     if not os.path.exists(directory):
         os.makedirs(directory)

     if not os.path.exists(directory1):
         os.makedirs(directory1)
         
     for filename in glob.glob(os.path.join(path, '*.txt')):
          lobpunc(filename, directory+"/mod"+filename.replace(path, ""), directory1+"/mmod"+filename.replace(path, ""))
     for directory1 in glob.glob(os.path.join(directory1, '*.txt')):
          romfile(directory1, dir_path+"/result/romnovel.txt")
                 
path_to_directory = '/Users/bigmorning/Desktop/sasomkam/'
for m in glob.glob(os.path.join(path_to_directory, "*", "")):
     triam(m)
     print(str(m))
