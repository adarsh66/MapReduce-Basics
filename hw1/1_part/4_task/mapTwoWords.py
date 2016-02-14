#!/usr/bin/python

import sys

def main():
	#we are going to use the inbuilt aggregate package in hadoop streaming.
	#LongValueSum is the keyword associated with suming up the results associated with that keyword.
	aggregatorKey='LongValueSum:'
        for line in sys.stdin:
                line = line.strip()
		words = line.split()
                for i in range(len(words)-1):
			print aggregatorKey+words[i]+' '+words[i+1]+'\t'+'1'

if __name__ == '__main__':
        main()

