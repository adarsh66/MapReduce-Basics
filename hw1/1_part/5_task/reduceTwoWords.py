#!/usr/bin/python
'''
Logic for this code is taken almost exactly from the Lab 1 slides
and is identical to task 4 count
'''
import sys

def main():
	prev_word = ''
	value_total = 0
	word = ''

	for line in sys.stdin:          
		line = line.strip()         
		word, value = line.split('\t', 1)
		value = int(value)

		if prev_word == word:
			value_total += value
		else:
			if prev_word:  # write result to stdout
				print prev_word+'\t'+str(value_total)

			value_total = value
			prev_word = word

	#print the last line
	if prev_word == word:
    		print prev_word+'\t'+str(value_total)

if __name__=='__main__':
	main()

