import json


def load_data(file):


	# Reads in the json file containing
	def read_json():

		class_data = json.loads(open(file).read())
		#class_data = json.loads(open("FallClasses.json").read())
		return class_data

	# Removes some values from the dictionaries
	def delete_values(list):

		for course in list:
			
			del course ['Type']
			del course ['Teacher']
			del course ['Location1']
			del course ['Location2']
			del course ['Location3']
			del course ['credits']
		
		return list 
		

	# Creates a list of all subjects
	def add_subjects(list):

		subject_list = []
		for course in list:
			if (not course['Course'] in subject_list):
				subject_list.append(course['Course'])
		return subject_list


	# Maps times to days
	def organize_times1(list):

		for course in list:

			if course['Days1'] == 'MW':
				course['MW Begin'] = course['timeBegin1']
				course['MW End'] = course['timeEnd1']
			elif course['Days1'] == 'MWF':
				course['MWF Begin'] = course['timeBegin1']
				course['MWF End'] = course['timeEnd1']
			elif course['Days1'] == 'MWR':
				course['MWR Begin'] = course['timeBegin1']
				course['MWR End'] = course['timeEnd1']
			elif course['Days1'] == 'TR':
				course['TR Begin'] = course['timeBegin1']
				course['TR End'] = course['timeEnd1']
			elif course['Days1'] == 'MTWRF':
				course['MTWRF Begin'] = course['timeBegin1']
				course['MTWRF End'] = course['timeEnd1']
			elif course['Days1'] == 'M':
				course['M Begin'] = course['timeBegin1']
				course['M End'] = course['timeEnd1']
			elif course['Days1'] == 'T':
				course['T Begin'] = course['timeBegin1']
				course['T End'] = course['timeEnd1']
			elif course['Days1'] == 'W':
				course['W Begin'] = course['timeBegin1']
				course['W End'] = course['timeEnd1']
			elif course['Days1'] == 'R':
				course['R Begin'] = course['timeBegin1']
				course['R End'] = course['timeEnd1']
			elif course['Days1'] == 'F':
				course['F Begin'] = course['timeBegin1']
				course['F End'] = course['timeEnd1']

		return list

	# Maps more times to days
	def organize_times2(list):

		for course in list:

			if course['Days2'] == 'MW':
				course['MW Begin'] = course['timeBegin2']
				course['MW End'] = course['timeEnd2']
			elif course['Days2'] == 'MWF':
				course['MWF Begin'] = course['timeBegin2']
				course['MWF End'] = course['timeEnd2']
			elif course['Days2'] == 'MWR':
				course['MWR Begin'] = course['timeBegin2']
				course['MWR End'] = course['timeEnd2']
			elif course['Days2'] == 'TR':
				course['TR Begin'] = course['timeBegin2']
				course['TR End'] = course['timeEnd2']
			elif course['Days2'] == 'MTWRF':
				course['MTWRF Begin'] = course['timeBegin2']
				course['MTWRF End'] = course['timeEnd2']
			elif course['Days2'] == 'M':
				course['M Begin'] = course['timeBegin2']
				course['M End'] = course['timeEnd2']
			elif course['Days2'] == 'T':
				course['T Begin'] = course['timeBegin2']
				course['T End'] = course['timeEnd2']
			elif course['Days2'] == 'W':
				course['W Begin'] = course['timeBegin2']
				course['W End'] = course['timeEnd2']
			elif course['Days2'] == 'R':
				course['R Begin'] = course['timeBegin2']
				course['R End'] = course['timeEnd2']
			elif course['Days2'] == 'F':
				course['F Begin'] = course['timeBegin2']
				course['F End'] = course['timeEnd2']

		return list

	# Maps more times to days
	def organize_times3(list):

		for course in list:

			if course['Days3'] == 'MW':
				course['MW Begin'] = course['timeBegin3']
				course['MW End'] = course['timeEnd3']
			elif course['Days3'] == 'MWF':
				course['MWF Begin'] = course['timeBegin3']
				course['MWF End'] = course['timeEnd3']
			elif course['Days3'] == 'MWR':
				course['MWR Begin'] = course['timeBegin3']
				course['MWR End'] = course['timeEnd3']
			elif course['Days3'] == 'TR':
				course['TR Begin'] = course['timeBegin3']
				course['TR End'] = course['timeEnd3']
			elif course['Days3'] == 'MTWRF':
				course['MTWRF Begin'] = course['timeBegin3']
				course['MTWRF End'] = course['timeEnd3']
			elif course['Days3'] == 'M':
				course['M Begin'] = course['timeBegin3']
				course['M End'] = course['timeEnd3']
			elif course['Days3'] == 'T':
				course['T Begin'] = course['timeBegin3']
				course['T End'] = course['timeEnd3']
			elif course['Days3'] == 'W':
				course['W Begin'] = course['timeBegin3']
				course['W End'] = course['timeEnd3']
			elif course['Days3'] == 'R':
				course['R Begin'] = course['timeBegin3']
				course['R End'] = course['timeEnd3']
			elif course['Days3'] == 'F':
				course['F Begin'] = course['timeBegin3']
				course['F End'] = course['timeEnd3']

		return list


	# Deletes more values in the dictionaries
	def delete_times(list):

		for course in list:
			# Deleting times and days
			del course ['timeBegin1']
			del course ['timeBegin2']
			del course ['timeBegin3']
			del course ['timeEnd1']
			del course ['timeEnd2']
			del course ['timeEnd3']
			del course ['Days1']
			del course ['Days2']
			del course ['Days3']
		
		return list 

	# Creates a single string listing all days and respective times of the courses
	def time_string(class_list, json_list):

		for i in range(len(json_list)):
			time = json_list[i]['Days1'] + " " + json_list[i]['timeBegin1'] + " " + json_list[i]['timeEnd1'] + " " + json_list[i]['Days2'] + " " + json_list[i]['timeBegin2'] + " " + json_list[i]['timeEnd2'] + " " + json_list[i]['Days3'] + " " + json_list[i]['timeBegin3'] + " " + json_list[i]['timeEnd3']
			class_list[i]['Time string'] = time
		return class_list

	# Empties strings which only contain zero
	def remove_zeros(list):

		for course in list:
			if course['timeBegin1'] == '0':
				course['timeBegin1'] = ''
			if course['timeBegin2'] == '0':
				course['timeBegin2'] = ''
			if course['timeBegin3'] == '0':
				course['timeBegin3'] = ''
			if course['timeEnd1'] == '0':
				course['timeEnd1'] = ''
			if course['timeEnd2'] == '0':
				course['timeEnd2'] = ''
			if course['timeEnd3'] == '0':
				course['timeEnd3'] = ''

		return list

	def list_classes(list):

		class_list = []

		for course in list:
			CRN = course['CRN']
			subject = course['Course']
			course_number = course['Num']
			course_name = course['Title']
			times = course['Time string']
			class_list.append([CRN, subject, course_number, course_name, times])

		return class_list


	# List of dictionaries for each course
	original_list = read_json()
	refined_list = read_json()

	subject_list = add_subjects(refined_list)

	original_list = remove_zeros(original_list)
	refined_list = delete_values(refined_list)

	# Maps times of courses to their days
	refined_list = organize_times1(refined_list)
	refined_list = organize_times2(refined_list)
	refined_list = organize_times3(refined_list)
	refined_list = delete_times(refined_list)
	refined_list = time_string(refined_list, original_list)
	class_list = list_classes(refined_list)

	#print subject_list
	#print original_list[99]
	#print refined_list[99]
	print class_list[100]
	#print refined_list[100]['Time string']
	#print (refined_list)[3700]

load_data("FallClasses.json")