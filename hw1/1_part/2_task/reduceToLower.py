#!/usr/bin/python
import sys

def main():
	prev_line = ""

	for line in sys.stdin:
        	line = line.strip()
	        if line != prev_line:
        	        print line
                	prev_line = line

if __name__=='__main__':
	main()
