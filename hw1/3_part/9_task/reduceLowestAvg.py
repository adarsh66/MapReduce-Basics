#!/usr/bin/python

import sys

def main():
	lowest_avg = 0
	lowest_avg_student_list = []
	for line in sys.stdin:
		line = line.strip()
		line = line.split('\t')
		student_name= line[0] #the key
		student_avg= line[1] #the value
		if not(lowest_avg) or (student_avg <lowest_avg):
			lowest_avg = student_avg
			lowest_avg_student_list = [] #reinitialize to empty
			lowest_avg_student_list.append(student_name)
		elif student_avg == lowest_avg: #handles 2 or more students with low avg
			lowest_avg_student_list.append(student_name)

	#ASSUMPTION: we run this only on a single reducer
	for lowest_avg_student in lowest_avg_student_list:
		print lowest_avg_student + ' with ' + lowest_avg

if __name__ == '__main__':
	main()
