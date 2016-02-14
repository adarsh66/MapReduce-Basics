#!/usr/bin/python

import sys

def main():
	for line in sys.stdin:
		line = line.strip()
		line = line.split()
		#making the student id col the key variable
		if line[0] == 'student':
			emit([line[1],line[0],line[2]])
		else:
			emit([line[2],line[0],line[1],line[3]])
		
def emit(items):
	stringOutput = ''
	for item in items:
		stringOutput += item + '\t'
	print stringOutput.strip()


if __name__ == '__main__':
	main()
