import os 

# This is to get the directory that the program 
# is currently running in. 
def search(name):
	dir_path = os.path.dirname(os.path.realpath(__file__)) 
	file_name = name+".mp3"
	for root, dirs, files in os.walk(dir_path):
		for file in files: 
			if file.endswith(file_name): 
				path = root+'/'+str(file)
				return True
