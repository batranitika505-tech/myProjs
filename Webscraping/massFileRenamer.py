import os

count = 61
ext = '.jpg'

pattern = 'some'

rootPath = '.'

for root, dirs, files in os.walk(rootPath):
	for filename in files:
		if pattern in filename:
			fname = str(count) + ext
			count += 1
			os.rename(filename, fname)