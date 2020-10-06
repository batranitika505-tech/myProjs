import os
import sys
import urllib2
from bs4 import BeautifulSoup
import image_scraper
import datetime

# Specify URL(s) here
downloadURLsArray = ['',]
subtag = ['']
fileType = ['jpg']
hdr = {'User-Agent':'Mozilla/5.0'}
counts = 0
title = ''

def fetchTitleLinks(url, title=''):
	try:
		req = urllib2.Request(url,headers=hdr)
		page = urllib2.urlopen(req)
		soup = BeautifulSoup(page, "lxml")
		links = soup.find_all('a')
		#print links
		requiredLinks = []
		for tag in links:
			link = tag.get('href', None)
			if link is not None:
				if title in link:
					if '?' not in link.split('/')[-1] and '#' not in link.split('/')[-1] and ' ' not in link.split('/')[-1] and url != link:
						requiredLinks.append(link)
		
		return list(set(requiredLinks))
		
	except urllib2.HTTPError, e:
		print e.fp.read()
		return None

def fetchRequiredLinks(url):
	try:
		req = urllib2.Request(url,headers=hdr)
		page = urllib2.urlopen(req)
		soup = BeautifulSoup(page, "lxml")
		links = soup.find_all('a')
		# print links
		requiredLinks = []
		for tag in links:
			link = tag.get('href', None)
			if link is not None:
				for reqContent in subtag:
					if reqContent in link:
						requiredLinks.append(link)

				for reqFileType in fileType:
					if reqFileType in link:
						requiredLinks.append(link)
						
		img_tags = soup.find_all('img')
		urls = [img['src'] for img in img_tags]
		for url in urls:
			requiredLinks.append(url)
		# print requiredLinks
		return requiredLinks
		
	except urllib2.HTTPError, e:
		print e.fp.read()
		return None

def saveFile(url, fileType):
	#print 'saveFile : %', url
	global count
	try:
		fileName = url.split('/')[-1]
		'''
		else:
			countStr = str(count)
			while len(countStr) != 3:
				countStr = '0' + countStr
			#print countStr
			fileName = title + '_' + countStr + '.' + fileType 
		'''
		if not os.path.exists(fileName):
			f = open(fileName, 'wb')
		else:
			tStr = datetime.datetime.strftime(datetime.datetime.now(), "%H%M%S")
			fileName = tStr + '__' + fileName
			f = open(fileName, 'wb')
			
		req = urllib2.Request(url,headers=hdr)
		f.write(urllib2.urlopen(req).read())
		f.close()
	except Exception as e:
		print e
	count += 1
	
def fetchRequiredFile(url):
	for reqFileType in fileType:
		if reqFileType in url:
			saveFile(url, reqFileType)

def fetchRequiredContent(urlArray):
	for url in urlArray:
		fetchRequiredFile(url)
		
		links = list(set(fetchRequiredLinks(url)))
		# print links
		for link in links:
			fetchRequiredFile(link)
			print "Complete: ", count*100/len(urlArray)
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
	print dirName
	title = dirName
	dirPath = currWd + '\\' + dirName
	if not os.path.exists(dirPath):
		os.makedirs(dirPath)
	os.chdir(dirPath)

	urlArray = []
	urlArray = fetchRequiredLinks(url)
	titleLinks = fetchTitleLinks(url, dirName)
	titleLinks.sort()
	# print 'Title Links are ', titleLinks
	for link in titleLinks:
		respArray = fetchRequiredLinks(link)
		urlArray += respArray
		
	# for url in urlArray: print url
	fetchRequiredContent(urlArray)
	os.chdir(currWd)
	
def main():
	for url in downloadURLsArray:
		downloadURLContent(url)
	
main()
