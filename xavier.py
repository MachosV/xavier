#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests,marshal,types
from xml.etree import ElementTree


def buildArgs(r): #response object
	tree = ElementTree.fromstring(r.content)
	d = {}
	for arg in tree.iter('arg'):
		d[arg[0].text] = arg[1].text
	return d

def buildCode(r):
	tree = ElementTree.fromstring(r.content)
	code = tree[0].text.split()
	code = map(int,code)
	code = map(chr,code)
	code = marshal.loads("".join(code))
	return code

def main(args):
	r = requests.get("http://localhost:8000/content1") #content1 is the xml file containing the code object
	print "Message received, building:"
	code_object = buildCode(r)
	args = buildArgs(r)
	exec(code_object,args)
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
