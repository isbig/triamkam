import re
import string
import os
import glob
import sys
import deepcut

s0 = [u'ก', u'ข', u'ฃ', u'ค', u'ฅ', u'ฆ', u'ง', u'จ', u'ฉ', u'ช',
    u'ซ', u'ฌ', u'ญ', u'ฎ', u'ฏ', u'ฐ', u'ฑ', u'ฒ', u'ณ', u'ด', u'ต', u'ถ', u'ท',
    u'ธ', u'น', u'บ', u'ป', u'ผ', u'ฝ', u'พ', u'ฟ', u'ภ', u'ม', u'ย', u'ร', u'ฤ',
    u'ล', u'ว', u'ศ', u'ษ', u'ส', u'ห', u'ฬ', u'อ', u'ฮ', u'ฯ', u'ะ', u'ั', u'า',
    u'ำ', u'ิ', u'ี', u'ึ', u'ื', u'ุ', u'ู', u'ฺฺ', u'เ', u'แ', u'โ', u'ใ', u'ไ',
    u'ๅ', u'ๆ', u'็', u'่', u'้', u'๊', u'๋', u'์', u'ํ', u'๐', u'๑', u'๒', u'๓',
    u'๔', u'๕', u'๖', u'๗', u'๘', u'๙']


def lobpunc(txt, txtnew):
     with open(txt, "r", encoding='utf-8') as f:
          with open(txtnew, "w", encoding='utf-8') as f1:
               for line in f:
                    for m in line:
                         if m not in s0:
                              line = line.replace(m, "")
                    f1.write(line)
               f1.close()
               f.close()

def token(txt, txtnew):
     with open(txt, "r", encoding='utf-8') as f:
          with open(txtnew, "a", encoding='utf-8') as f1:
               for line in f:
                    s = deepcut.tokenize(line)
                    m = ' '.join(s)
               f1.write(m)
          f1.close()
          f.close()
               
def romfile(txt, txtnew):
     with open(txt, "r", encoding='utf-8') as f:
          with open(txtnew, "a", encoding='utf-8') as f1:
               for line in f:
                    f1.write(line)
               f1.close()
               f.close()
                         
def triam(path):
     dir_path = os.path.dirname(os.path.realpath(__file__))
     directory = dir_path+'/result/twit_delpunc'
     directory1 = dir_path+'/result/twit_token'

     if not os.path.exists(directory):
         os.makedirs(directory)

     if not os.path.exists(directory1):
         os.makedirs(directory1)
         
     for filename in glob.glob(os.path.join(path, '*.txt')):
          lobpunc(filename, directory+"/delpunc_twit_"+filename.replace(path, ""))

     for filename in glob.glob(os.path.join(directory, '*.txt')):
          token(filename, directory1+"/token_twit_"+filename.replace(directory+"/", ""))

     for filename in glob.glob(os.path.join(directory1, '*.txt')):
          romfile(filename, dir_path+"/result/romfile_twit.txt")
                 
path_to_directory = '/Users/bigmorning/Documents/GitHub/Exthtweet/result/txtfile/'
triam(path_to_directory)
for m in glob.glob(os.path.join(path_to_directory, "*", "")):
     triam(m)
     print(str(m))
