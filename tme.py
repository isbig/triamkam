import re
def lobpunc(txt, txtnew, txtnewnew):
     with open(txt, "r", encoding='utf-8') as f:
          with open(txtnew, "w", encoding='utf-8') as f1:
               for line in f:
                    line = re.sub(r'^https?:\/\/.*[\r\n]*', '', line, flags=re.MULTILINE)
                    s = ["...", "\"", "<NE>", "</NE>", "?", "-", " ", ".", ":", "<AB>", "</AB>", "/", "(", ")"] 
                    for m in s:
                         line = line.replace(m, "")
                    for m in ["|", "\n", "  "]:
                         line = line.replace(m, " ")
                    while "  " in line:
                         line = line.replace("  ", " ")
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


import os
import glob
path = '/Users/bigmorning/Desktop/novel'
dir_path = os.path.dirname(os.path.realpath(__file__))
directory = dir_path+'/result/mod/'
directory1 = dir_path+'/result/mmod/'

if not os.path.exists(directory):
    os.makedirs(directory)

if not os.path.exists(directory1):
    os.makedirs(directory1)
    
for filename in glob.glob(os.path.join(path, '*.txt')):
     lobpunc(filename, directory+"mod"+str(filename)[-15:], directory1+"mmod"+str(filename)[-15:])

