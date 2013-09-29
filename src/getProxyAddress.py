#!/usr/bin/env python
#python25 on windows7
#####################################
# GPL v2
# Author: Arjun Sreedharan
# Email: arjun024@gmail.com
#####################################

import urllib2
import re
import os
import time
import random

def main():
	request = urllib2.Request("http://www.ip-adress.com/proxy_list/")
	# request.add_header("User-Agent", "Mozilla/5.0 (Windows; U; Windows NT 5.1; es-ES; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5")
	#Without Referer header ip-adress.com gives 403 Forbidden
	request.add_header("Referer","https://www.google.co.in/")
	f = urllib2.urlopen(request)

	#outfile = open('outfile.htm','w')
	str1 = f.read()
	#outfile.write(str1)

	# normally DOT matches anycharacter EXCEPT newline. re.DOTALL makes dot include newline
	pattern = re.compile('.*<td>(.*)</td>.*<td>Elite</td>.*', re.DOTALL)
	matched = re.search(pattern,str1)
	print(matched.group(1))
	"""
	ip = matched.group(1)
	os.system('echo "http_proxy=http://'+ip+'" > ~/.wgetrc')
	if random.randint(1,2)==1:
		os.system('wget --proxy=on -t 1 --timeout=14 --header="User-Agent: Mozilla/5.0 (Windows; U; Windows NT 5.1; es-ES; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5" http://funnytweets.in -O /dev/null')
	else:
		os.system('wget --proxy=on -t 1 --timeout=14 --header="User-Agent: Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.29 Safari/525.13" http://funnytweets.in -O /dev/null')
	"""
if __name__ == '__main__':
	while True:
		main()
		time.sleep(2)