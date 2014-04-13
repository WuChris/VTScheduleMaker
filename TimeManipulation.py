import shlex


# Splits times string from database into a list
def split_time(time_string):

	# times in list format: [days1, timeBegin1, timeEnd1, days2, timeBegin2, etc.]
	listed_times = shlex.split(time_string) 
	return listed_times


# Cast the time strings to integers
def cast_to_ints(time_list):

	for i in range(0, len(time_list), 3):
		time_list[i+1] = int(time_list[i+1])
		time_list[i+2] = int(time_list[i+2])
	return time_list

# Splits the string into a list and convert numerical strings to ints
def fix_time_string(time_string):

	time_list = split_time(time_string)
	time_list = cast_to_ints(time_list)

	return time_list