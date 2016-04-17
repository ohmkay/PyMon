from datetime import datetime
import os.path

#Set file names
logs_to_check = [
"REGION1",
"REGION5"
]

#path to logs folder
file_path = '../logs/'

################################
#Add paths and date to filenames
################################
def format_log_paths(logs_to_check, file_path):
	logs_to_check = [file_path + log + "." + datetime.now().strftime("%m%d") for log in logs_to_check]
	return logs_to_check

logs_to_check = format_log_paths(logs_to_check, file_path)

#Read errors in log files
lines = []
for log in logs_to_check:
	if os.path.isfile(log):
		with open (log, 'r') as f:
			for line in f:
				if "error" in line:
					lines.append(line.rstrip('\n'))
	else:
		print('File ' + log + ' does not exist.')

#Testing
for line in lines:
	print(line)