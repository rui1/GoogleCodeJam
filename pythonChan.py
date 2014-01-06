#!/usr/bin/python

import string
import urllib.request
import re

original = """
g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."""

intab = string.ascii_lowercase
outab = intab[2:]+intab[:2]


print(original.translate(str.maketrans(intab,outab)))

b = "http://www.pythonchallenge.com/pc/def/map.html"
print(b.translate(str.maketrans(intab,outab)))


a = urllib.request.urlopen('http://www.pythonchallenge.com/pc/def/ocr.html')
html = a.read()

txt = re.compile('<!--((?:[^-]+|-[^-]|--[^>])*)-->', re.S).findall(html)[-1]
count = {}
for c in text : count[c]= count.get(c, 0)+1
count


