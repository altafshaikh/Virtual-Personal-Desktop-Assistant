import os


def create_dir(path): 
    try:  
    	#create directory
        os.mkdir(path)
    except OSError:  
        print ("Creation of the directory %s failed" % path)
    else:  
        print ("Successfully created the directory %s " % path)

def remove_dir(path):
    try:  
        #remove directory
        os.rmdir(path)
        
    except OSError:  
        print ("Deletion of the directory %s failed" % path)
    else:  
        print ("Successfully Deleted the directory %s " % path)

def create_file(path):
    try:  
        #create files
        cmd = "touch"+path
        os.system(cmd)
    
    except OSError:  
        print ("Creation of the File %s failed" % path)
    else:  
        print ("Successfully Created the file %s " % path)


def remove_file(path):
    try:  
        #delete file 
        os.system("rm filename")
    
    except OSError:  
        print ("Deletion of the File %s failed" % path)
    else:  
        print ("Successfully Removed the file %s " % path)

def copy(path,filename):
    try:  
        #coping file
        os.system('cp text.py /root/Desktop/')
       
    except OSError:  
        print ("Coping of the File %s failed" % path)
    else:  
        print ("Successfully Copied the file %s " % path)

def move(path,filename):
    try:  
        #moving file
        os.system('mv text.py /root/Desktop/')

    except OSError:  
        print ("Moving of the File %s failed" % path)
    else:  
        print ("Successfully Moved the file %s " % path)



