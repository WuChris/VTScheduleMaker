from TimeManipulation import *
from TimeAdder import *
from Reader import load_data
import random

# classes_to_add - number of classes to add
# subjects - list of subjects
# numbers - list of course numbers
def course_scheduler(classes_to_add, subjects, numbers):
	course_list = load_data('FallClasses.json')
	selected_list = []

	for i in range(0, classes_to_add):
		for course in course_list:
			if course[1] == subjects[i] and course[2] == numbers[i]:
				selected_list.append(course)

	schedule = []

	for course in selected_list:
		course[4] = fix_time_string(course[4])

	# Creates 5 schedules
	for i in range(0, 5):
		random.shuffle(selected_list)
		schedule.append(TimeAdder())

		# Schedule free times first
		for course in selected_list:
			if course == 'REG':
				schedule[i].add_class(course)

		# Attempt to add everything else
		for course in selected_list:
			schedule[i].add_class(course)

	return schedule #call schedule[index].class_list to retrieve that schedule

# """ Test run, just delete """
# schedule_list = []
# subjects = ['CS', 'CS', 'CS', 'MATH', 'MATH', 'BIOL', 'BIOL']
# numbers = ['1944', '2104', '2114', '2224', '2534', '1005', '1015']
# schedule_list = course_scheduler(7, subjects, numbers)
# print schedule_list[2].class_list
# for schedule in schedule_list:
# 	print schedule.class_list