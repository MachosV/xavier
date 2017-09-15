#!/usr/bin/env python
# -*- coding: utf-8 -*-

import marshal

def printer(): #sample function.
	print msg
	
def stringifyCode():
	code_string = marshal.dumps(printer.func_code) #make the string -> upload to file
	return map(ord,code_string)
	#code = marshal.loads(code_string) # receiver downloads the string, runs this to get code object
	#exec(code,{'msg':'KALIMERA'}) #exec the code with arguments ;)

def main(args):
	f = open ("content1","w+")
	f.write("<content>")
	f.write("<code>")
	code = stringifyCode()
	for num in code:
		f.write(str(num)+" ")
	f.write("</code>")
	f.write('''<args>
		<arg>
			<key>msg</key>
			<value>H3ll0 w0rld</value>
		</arg>
	</args>''')
	f.write("</content>")
	f.close()
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
