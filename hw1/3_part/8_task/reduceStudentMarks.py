#!/usr/bin/python

import sys

def main():
	prev_student_id = ''
	course_list = []
	for line in sys.stdin:
		line = line.strip()
		line = line.split('\t')
		student_id= line[0] #the key
		if student_id == prev_student_id:
			if line[1] == 'student':
				student_name = line[2]
			else:
				course_list.append((line[2],line[3]))
		else:
			if prev_student_id:
				printStudentDetails(student_name,course_list)
			prev_student_id = student_id
			course_list = []
			if line[1] == 'student':
				student_name = line[2]
			else:
				course_list.append((line[2],line[3]))
	
	#for the last row
	printStudentDetails(student_name, course_list)

def printStudentDetails(student_name, course_list):
	stringOutput = student_name + ' -->'
	for (course_name, course_marks) in course_list:
		stringOutput += ' ('+course_name+','+course_marks+')'
	print stringOutput

if __name__ == '__main__':
	main()
