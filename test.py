from datetime import datetime
import os.path

#Set file names
logs_to_check = [
	{'path':'./logs/', 'filename':'REGION1'},
	{'path':'./logs/', 'filename':'REGION5'}
]

#errors to ignore
whitelist = [
	"not an error",
	"definitely...not an error"
]

################################
#Add paths and date to filenames
################################
def add_date_to_log(logs_to_check):
	for log in logs_to_check:
		for key, value in log.items():
			if key == 'filename':
				log[key] = value + "." + datetime.now().strftime("%m%d")
	return logs_to_check

def create_full_path(logs_to_check):
	for log in logs_to_check:
		for key, value in log.items():
			if key == 'path':
				path = value
			elif key == 'filename':
				filename = value
		log['full_path'] = path + filename
	return logs_to_check

def check_against_whitelist(line):
	for ignorable in whitelist:
		if ignorable in line:
			return True
		else:
			return False

logs_to_check = add_date_to_log(logs_to_check)
logs_to_check = create_full_path(logs_to_check)

# test_string = 'this shouldnt be an error but you never know.  also, it\'s not ann error'
# print(check_against_whitelist(test_string))

#iterates through logs looking for errors and writes them to a file
lines = []
for log in logs_to_check:
	for key, value in log.items():
		if key == 'full_path':
			if os.path.isfile(value):  #checks if log file exists
				with open(value, 'r') as f:
					for line in f:
						if 'error' in line:
							if not check_against_whitelist(line):  #calls function to test error against whitelist
								lines.append(line.rstrip('\n'))  #adds line and removes newline
			else:
				print('File ' + value + ' does not exist.')	

	#write data to output log file
	for line in lines:
		with open('./PyMonLog/test.txt', 'a') as f:
			f.write(line+'\n')
	lines = []