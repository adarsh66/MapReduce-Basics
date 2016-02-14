#!/usr/bin/python

def main():
	topTwentyWords=[]
	maxCount = 0
	for line in sys.stdin:
		line = line.strip()
		word_pair, count = line.split('\t')
		if count >maxCount:
		


if __name__=='__main__':
	main()
