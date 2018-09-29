import argparse
import time
import os
import random
from googlesearch import search


parser = argparse.ArgumentParser()
parser.add_argument("--target", help="Target")
args = parser.parse_args()

keyword = str(args.target)

ganti = "%s" % keyword
hasil = ganti.replace(" ", "_")

os.mkdir("output/%s" % hasil)

for url in search("'%s' site:t.me" % str(keyword), stop=150):
    file = open("output/%s.txt" % str(keyword), 'a')
    file.write("%s\n" % url)
    file.close()


#createScreenshot
lis = [x.rstrip() for x in open('output/%s.txt' % str(keyword), 'r').readlines() if len(x.rstrip())]
for link in lis:
   rndm = random.random()
   os.system("/usr/local/bin/html2latex_webkit2png.py %s -o output/%s/%s.png" % (link,hasil, str(rndm)))