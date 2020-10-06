import os
import sys
import urllib3
from bs4 import BeautifulSoup
import datetime

# Specify URL(s) here
downloadURLsArray = ['',					 
					 ]
fileType = ['jpg']
hdr = {'User-Agent':'Mozilla/5.0'}
counts = 0
title = ''
http = urllib3.PoolManager()
    
def fetchRequiredLinks(url):
	try:
		req = http.request('GET', url, headers=hdr)
		soup = BeautifulSoup(req.data, 'html.parser')
		requiredLinks = []				
		img_tags = soup.find_all('img')
		urls = [img['src'] for img in img_tags]
		for url in urls:
			url = url.strip()
			result = url.find('?')
			if result != -1:
				url = url[:result]
			requiredLinks.append(url)
		# print (requiredLinks)
		return requiredLinks
		
	except urllib3.HTTPError as e:
		print (e.fp.read())
		return None

def saveFile(url, fileType):
	# print ('saveFile : %', url)
	global count
	try:
		fileName = url.split('/')[-1]
		'''
		else:
			countStr = str(count)
			while len(countStr) != 3:
				countStr = '0' + countStr
			# print (countStr)
			fileName = title + '_' + countStr + '.' + fileType 
		'''
		if not os.path.exists(fileName):
			f = open(fileName, 'wb')
		else:
			tStr = datetime.datetime.strftime(datetime.datetime.now(), "%H%M%S")
			fileName = tStr + '__' + fileName
			f = open(fileName, 'wb')
			
		req = http.request('GET', url, headers=hdr)
		f.write(req.data)
		f.close()
	except Exception as e:
		print (e)
	count += 1
	
def fetchRequiredFile(url):
	for reqFileType in fileType:
		if reqFileType in url:
			saveFile(url, reqFileType)

def fetchRequiredContent(urlArray):
	for url in urlArray:
		fetchRequiredFile(url)
		print ("Complete: ", count*100/len(urlArray))
		sys.stdout.write("\rCountdown: %d of %d" % (count, len(urlArray)))
		sys.stdout.flush()
			
def downloadURLContent(url):
	global count, title
	count = 0
	title = ''
	currWd = os.getcwd()
	dirName = url.split('/')[-1]
	if not dirName:
		dirName = url.split('/')[-2]
	print (dirName)
	title = dirName
	dirPath = currWd + '\\' + dirName
	if not os.path.exists(dirPath):
		os.makedirs(dirPath)
	os.chdir(dirPath)

	urlArray = []
	urlArray = fetchRequiredLinks(url)
	for url in urlArray: print (url)
	fetchRequiredContent(urlArray)
	os.chdir(currWd)
	
def main():
	for url in downloadURLsArray:
		downloadURLContent(url)
	
main()
