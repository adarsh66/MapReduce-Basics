#!/usr/bin/python

import sys

def main():
	for line in sys.stdin:
		line = line.strip()
		col_index = 0
		#first value in the line is the row_index
		row_index, line =line.split('\t') 
		for c in line.split():
			print str(col_index) + '\t' + row_index + '\t' + c
			col_index +=1

if __name__ == '__main__':
	main()
