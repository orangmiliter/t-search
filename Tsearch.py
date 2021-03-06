import argparse
import time
import sys
import os
import random
from gsearch.googlesearch import search


parser = argparse.ArgumentParser()
parser.add_argument("--target", help="Target", nargs='+')
if len(sys.argv)==1:
    parser.print_help(sys.stderr)
    sys.exit(1)
args = parser.parse_args()
argspace = ' '.join(args.target)
keyword = str(argspace)

ganti = "%s" % keyword
hasil = ganti.replace(" ", "_")

os.mkdir("output/%s" % hasil)

for url in search('"%s" site:t.me' % str(keyword), num_results=50):
    file = open("output/%s.txt" % str(keyword), 'a')
    file.write("%s\n" % url[1])
    file.close()


#createScreenshot
lis = [x.rstrip() for x in open('output/%s.txt' % str(keyword), 'r').readlines() if len(x.rstrip())]
for link in lis:
	rndm = random.random()
	os.system("wget -nH --cut-dirs=1 --output-document=output/%s/%s.html --convert-links %s" % (hasil, str(rndm), link))
	os.system("ls output/%s/ > output/%s.txt" % (hasil, hasil))

#Createiframe
lis = [x.rstrip() for x in open('output/%s.txt' % hasil, 'r').readlines() if len(x.rstrip())]
for frame in lis:
	fIframe = open('output/%s.html' % hasil, 'a')
	Iframe = """
	<iframe src="%s/%s" height="200" width="300" frameborder="3" gesture="media" allow="encrypted-media" allowfullscreen>></iframe>""" % (hasil, frame)
	fIframe.write(Iframe)
	fIframe.close()

os.remove('output/%s.txt' % hasil)
