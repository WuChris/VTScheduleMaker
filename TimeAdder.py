class TimeAdder(object):

	def __init__(self):

		self.monday_times = []
		self.tuesday_times = []
		self.wednesday_times = []
		self.thursday_times = []
		self.friday_times = []
		self.class_list = []

	def add_class(self, course):
		
		# Checks first time slot
		if len(course[4]) == 3:
			self.check_days(course, 1, 2)

		# Checks first and additional time slot
		if len(course[4]) == 6:
			self.check_days(course, 1, 2)
			self.check_days(course, 4, 5)

		# Checks first and two additional time slots
		if len(course[4]) == 9:
			self.check_days(course, 1, 2)
			self.check_days(course, 4, 5)
			self.check_days(course, 7, 8)

	# Checks first for the days which the classes are to be scheduled
	# Checks that all necessary time slots are available
	def check_days(self, course, begin, end):

		if course[4][begin-1] == 'MWF':

			if (self.is_available_monday(course[4][begin], course[4][end]) and
					self.is_available_wednesday(course[4][begin], course[4][end]) and
					self.is_available_friday(course[4][begin], course[4][end])):

				self.add_to_monday(course[4][begin], course[4][end])
				self.add_to_wednesday(course[4][begin], course[4][end])
				self.add_to_friday(course[4][begin], course[4][end])
				self.add_to_class_list(course)

		elif course[4][begin-1] == 'MW':

			if (self.is_available_monday(course[4][begin], course[4][end]) and
					self.is_available_wednesday(course[4][begin], course[4][end])):

				self.add_to_monday(course[4][begin], course[4][end])
				self.add_to_wednesday(course[4][begin], course[4][end])
				self.add_to_class_list(course)

		elif course[4][begin-1] == 'MWR':

			if (self.is_available_monday(course[4][begin], course[4][end]) and
					self.is_available_wednesday(course[4][begin], course[4][end]) and
					self.is_available_thursday(course[4][begin], course[4][end])):

				self.add_to_monday(course[4][begin], course[4][end])
				self.add_to_wednesday(course[4][begin], course[4][end])
				self.add_to_thursday(course[4][begin], course[4][end])
				self.add_to_class_list(course)

		elif course[4][begin-1] == 'TR':

			if (self.is_available_tuesday(course[4][begin], course[4][end]) and
					self.is_available_thursday(course[4][begin], course[4][end])):

				self.add_to_tuesday(course[4][begin], course[4][end])
				self.add_to_thursday(course[4][begin], course[4][end])
				self.add_to_class_list(course)

		elif course[4][begin-1] == 'MTWRF':

			if (self.is_available_monday(course[4][begin], course[4][end]) and
					self.is_available_tuesday(course[4][begin], course[4][end]) and
					self.is_available_wednesday(course[4][begin], course[4][end]) and
					self.is_available_thursday(course[4][begin], course[4][end]) and
					self.is_available_friday(course[4][begin], course[4][end])):

				self.add_to_monday(course[4][begin], course[4][end])
				self.add_to_tuesday(course[4][begin], course[4][end])
				self.add_to_wednesday(course[4][begin], course[4][end])
				self.add_to_thursday(course[4][begin], course[4][end])
				self.add_to_friday(course[4][begin], course[4][end])
				self.add_to_class_list(course)

		elif course[4][begin-1] == 'M':
			
			if self.is_available_monday(course[4][begin], course[4][end]):
				self.add_to_monday(course[4][begin], course[4][end])
				self.add_to_class_list(course)

		elif course[4][begin-1] == 'T':
			
			if self.is_available_tuesday(course[4][begin], course[4][end]):
				self.add_to_tuesday(course[4][begin], course[4][end])
				self.add_to_class_list(course)

		elif course[4][begin-1] == 'W':

			if self.is_available_wednesday(course[4][begin], course[4][end]):
				self.add_to_wednesday(course[4][begin], course[4][end])
				self.add_to_class_list(course)

		elif course[4][begin-1] == 'R':

			if self.is_available_thursday(course[4][begin], course[4][end]):
				self.add_to_thursday(course[4][begin], course[4][end])
				self.add_to_class_list(course)

		elif course[4][begin-1] == 'F':

			if self.is_available_friday(course[4][begin], course[4][end]):
				self.add_to_friday(course[4][begin], course[4][end])
				self.add_to_class_list(course)

	# Add the minutes of a course so they cannot be duplicated
	def add_to_monday(self, begin, end):
		for minute in range(begin, end):
			self.monday_times.append(minute)
	
	# Adds filled in times for Tuesday
	def add_to_tuesday(self, begin, end):
		for minute in range(begin, end):
			self.tuesday_times.append(minute)

	# Adds filled in times for Wednesday
	def add_to_wednesday(self, begin, end):
		for minute in range(begin, end):
			self.wednesday_times.append(minute)

	# Adds filled in times for Thursday
	def add_to_thursday(self, begin, end):
		for minute in range(begin, end):
			self.thursday_times.append(minute)

	# Adds filled in times for Friday
	def add_to_friday(self, begin, end):
		for minute in range(begin, end):
			self.friday_times.append(minute)

	# Add the course to the list of courses
	def add_to_class_list(self, course):
		if self.class_list.count(course) == 0 and not self.is_course_listed(course):	
			self.class_list.append(course)

	# Checks if the time slot for Monday can hold a course 
	def is_available_monday(self, begin, end):
		minutes = range(begin, end)
		for time in minutes:
			if time in self.monday_times:
				return False
		return True

	# Checks if the time slot for Tuesday can hold a course 
	def is_available_tuesday(self, begin, end):
		minutes = range(begin, end)
		for time in minutes:
			if time in self.tuesday_times:
				return False
		return True

	# Checks if the time slot for Wednesdayday can hold a course 
	def is_available_wednesday(self, begin, end):
		minutes = range(begin, end)
		for time in minutes:
			if time in self.wednesday_times:
				return False
		return True

	# Checks if the time slot for Thursday can hold a course 
	def is_available_thursday(self, begin, end):
		minutes = range(begin, end)
		for time in minutes:
			if time in self.thursday_times:
				return False
		return True

	# Checks if the time slot for Friday can hold a course 
	def is_available_friday(self, begin, end):
		minutes = range(begin, end)
		for time in minutes:
			if time in self.friday_times:
				return False
		return True

	# Checks if class_list already contains the course being added
	def is_course_listed(self, course):
		for item in self.class_list:
			if item[2] == course[2] and item[3] == course[3]:
				return True
		return False

# schedule = TimeAdder()
# cs_time = ['MW 1115 1205 R 1530 1730']
# cs_time = ['MW', 1115, 1205, 'R', 1530, 1730]
# my_course = ['82120', 'CS', '1114', 'Intro to Software Design', cs_time]
# new_course = ['82122', 'CS', '1114', 'Intro to Software Design', ['R', 800, 1000, 'MW', 1115, 1205]]
# schedule.add_class(my_course)
# schedule.add_class(new_course)
# print schedule.class_list
# print len(schedule.class_list)