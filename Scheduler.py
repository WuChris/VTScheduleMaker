from TimeManipulation import *
from TimeAdder import *
from Reader import load_data
import random

course_list = load_data('FallClasses.json')
selected_list = []

"""Choosing courses here"""

for course in course_list:
	if course[1] == 'COMM' and course[2] == '2004':
		selected_list.append(course)

for course in course_list:
	if course[1] == 'CS' and course[2] == '2505':
		selected_list.append(course)

for course in course_list:
	if course[1] == 'CS' and course[2] == '1944':
		selected_list.append(course)

for course in course_list:
	if course[1] == 'MATH' and course[2] == '2214':
		selected_list.append(course)

for course in course_list:
	if course[1] == 'MATH' and course[2] == '3134':
		selected_list.append(course)

for course in course_list:
	if course[1] == 'BIOL' and course[2] == '1005':
		selected_list.append(course)

for course in course_list:
	if course[1] == 'BIOL' and course[2] == '1015':
		selected_list.append(course)

random.shuffle(selected_list)
schedule = TimeAdder()

for course in selected_list:
	course[4] = fix_time_string(course[4])

# Schedule free times first
for course in course_list:
	if course[1] == 'REG':
		schedule.add_class(course)

# Attempt to add everything else
for course in selected_list:
	schedule.add_class(course)

print schedule.class_list