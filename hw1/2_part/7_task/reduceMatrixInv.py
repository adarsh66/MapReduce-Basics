#!/usr/bin/python

import sys

def main():
	prev_col = ''
	firstLine = True #flag to check if this is the first row for this reducer
	for line in sys.stdin:
		line = line.strip()
		col_index, row_index, matrix_val = line.split('\t')
		if col_index == prev_col:
			#using stdout.write to ensure we dont hit buffer overflow 
			#we emit the values as soon as we hit them
			#stdout.write will continue append on the existing output
			sys.stdout.write(matrix_val + ' ')
			prev_col = col_index
		else:
			if not(firstLine):#only print the new line if this is not the first line
				sys.stdout.write('\n')#new column, new line
			sys.stdout.write(col_index +'\t'+ matrix_val + ' ')
			prev_col = col_index
			firstLine = False
	sys.stdout.write('\n')#new line after the last val has been printed

if __name__ == '__main__':
	main()

