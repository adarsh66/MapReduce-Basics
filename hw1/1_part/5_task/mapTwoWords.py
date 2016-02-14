#!/usr/bin/python

import sys

def main():
	aggregatorKey='LongValueSum:'
	twoWordHashTable = {}
        for line in sys.stdin:
                line = line.strip()
		words = line.split()
                for i in range(len(words)-1):
			keyword = words[i] + ' ' + words[i+1]
			if keyword in twoWordHashTable:
				twoWordHashTable[keyword]+=1
			else:
				twoWordHashTable[keyword] =1
	#implementing the combiner.
	for key in twoWordHashTable.keys():
		print aggregatorKey + key + '\t' + str(twoWordHashTable[key])

if __name__ == '__main__':
        main()

