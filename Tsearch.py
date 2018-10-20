import argparse
import time
import os
import random
from googlesearch import search


parser = argparse.ArgumentParser()
parser.add_argument("--target", help="Target", nargs='+')
args = parser.parse_args()
argspace = ' '.join(args.target)
keyword = str(argspace)

ganti = "%s" % keyword
hasil = ganti.replace(" ", "_")

os.mkdir("output/%s" % hasil)

for url in search("'%s' site:t.me" % str(keyword), stop=10):
    file = open("output/%s.txt" % str(keyword), 'a')
    file.write("%s\n" % url)
    file.close()


#WgetHtml
lis = [x.rstrip() for x in open('output/%s.txt' % str(keyword), 'r').readlines() if len(x.rstrip())]
for link in lis:
<<<<<<< HEAD
	rndm = random.random()
	os.system("wget -nH --cut-dirs=1 --output-document=output/%s/%s.html --convert-links %s" % (hasil, str(rndm), link))
	os.system("ls output/%s/ > output/%s.txt" % (hasil, hasil))

#Createiframe
=======
   rndm = random.random()
   os.system("wget -nH --cut-dirs=1 --output-document=output/%s/%s.html --convert-links %s" % (hasil, str(rndm), link))
   os.system("ls output/kali_linux/ > output/%s.txt" % hasil)

#CreateIframe
>>>>>>> 7ab2f4566050736752a7e3bb9ac180c433d546a2
lis = [x.rstrip() for x in open('output/%s.txt' % hasil, 'r').readlines() if len(x.rstrip())]
for frame in lis:
	fIframe = open('output/%s.html' % hasil, 'a')
	Iframe = """
	<iframe src="%s/%s" height="200" width="300" frameborder="3" gesture="media" allow="encrypted-media" allowfullscreen>></iframe>""" % (hasil, frame)
	fIframe.write(Iframe)
	fIframe.close()

<<<<<<< HEAD
os.remove('output/%s.txt' % hasil)
=======
os.remove('output/%s.txt' % hasil)
>>>>>>> 7ab2f4566050736752a7e3bb9ac180c433d546a2
