import os
import csv
import sys

excelDataFilesDir = "D:\Aditya\Projects\PythonProgs\ExcelParser\excelData"
proprietaryHeaderLineNumber = 4

def findExcelFiles():
	fileList = []
	for file in os.listdir(excelDataFilesDir):
		if file.endswith(".csv") or file.endswith(".xls") or file.endswith(".xlsx"):
			fileList.append(file)
	return fileList

def findExcelFilesWithFullPath():
	fileListWithPath = []
	for root,dirs,files in os.walk(excelDataFilesDir):
		for file in files:
			if file.endswith(".csv") or file.endswith(".xls") or file.endswith(".xlsx"):
				fullpath = os.path.join(root, file)
				fileListWithPath.append(fullpath)
	return fileListWithPath

def storeExcelFormattedDataWithCorrespondingHeading(dataReader):
	data = []
	rownum = 0
	for row in dataReader:
		# Save header row.
		if rownum < proprietaryHeaderLineNumber:
			rownum += 1
			continue
		elif rownum == proprietaryHeaderLineNumber:
			header = row
		else:
			colnum = 0
			for col in row:
				data.append('%-8s: %s' % (header[colnum], col))
				colnum += 1
		rownum += 1
	return data

def storeExcelFormattedDataAsList(dataReader):
	data = list(dataReader)
	return data[proprietaryHeaderLineNumber:]

def readExcelFileData(file):
	fd = open(file)
	#data = fd.read()
	dataReader = csv.reader(fd)
	#data = storeExcelFormattedDataWithCorrespondingHeading(dataReader)
	data = storeExcelFormattedDataAsList(dataReader)
	fd.close()
	return data

def calculateTotalAmount(csvData):
	total = 0.0
	for line in csvData[1:]:
		#print line[3]
		total += float(line[3].replace(',', ''))
	return total
	
def main():
	fileListWithPath = findExcelFilesWithFullPath()
	for file in fileListWithPath:
		print file
		csvData = readExcelFileData(file)
		i = 1
		for line in csvData:
			print line
			i = i + 1
			if i == 5:
				break

		print calculateTotalAmount(csvData)
	
main()