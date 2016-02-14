#!/usr/bin/python

import sys

def main():
	lowest_avg = 0
	lowest_avg_student_list = []
	for line in sys.stdin:
		line = line.strip()
		line = line.split()
		totalMarks = 0
		numCourses = 0
		if len(line) > (2+4):
		#first two items are name and --> symbol. after that the marks
			for item in line:
				if '(' in item: #hacky way of finding the marks
					item = removeBrackets(item)
					course_name, course_mark = item.split(',')
					totalMarks += float(course_mark.strip())
					numCourses += 1
			avg = totalMarks/numCourses
			if (not(lowest_avg)) or (avg < lowest_avg):#if lowest avg is not initialized or avg is lesser than lowest avg
				lowest_avg = avg
				lowest_avg_student_list = [] #reinitialize to empty
				lowest_avg_student_list.append(line[0])
			elif avg == lowest_avg: # we need to append student name to the list
				lowest_avg_student_list.append(line[0])
	#this should work for more than one student with the lowest avg
	for lowest_avg_student in lowest_avg_student_list:
		emit([lowest_avg_student, lowest_avg])
		
def emit(items):
	stringOutput = ''
	for item in items:
		stringOutput += str(item) + '\t'
	print stringOutput.strip()

def removeBrackets(item):
	return item.replace('(','').replace(')','')

if __name__ == '__main__':
	main()
