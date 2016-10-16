import os # imports the module for manipulating files

def create_project_dir(directory): # creates a folder for each new website
    if not os.path.exists(directory): # creates a folder only if it doesn't already exist
        print ('Creating project ' + directory)
        os.makedirs(directory)

def create_data_files(project_name, base_url):
    queue = os.path.join(project_name , 'queue.txt') # sets the path for the queue file
    crawled = os.path.join(project_name, 'crawled.txt') # sets the path for the crawled file
    if not os.path.isfile(queue): # checks whether the file already exist
        write_file(queue, base_url) # creates a file and inserts a homepage URL
    if not os.path.isfile(crawled):
        write_file(crawled, '') # creates an empty crawled file

def write_file (path, data):
    f = open(path, 'w') # creates a file for writing
    f.write(data) # writes data to file
    f.close() # closes the file


def append_to_file(path, data):
    with open(path, 'a') as file: # opens the file in the append mode.
        file.write(data + '\n') # adds data (links) to file and bumps the cursor on the new line.

def delete_file_contents(path):
    with open(path, 'w'): # opens data in write mode and overwrite it
        pass

def file_to_set(file_name): # the function that will read  a file and convert each line to set items
    results = set() # creates an empty set
    with open(file_name, 'rt') as f:
        for line in f: # loop through each line in a file
            results.add(line.replace('\n', '')) # add a line to a set and remove a newline character we've added earlier
    return results

# Iterate through a set, each item will be a line in a file
def set_to_file(links, file_name):
    with open(file_name,"w") as f:
        for l in sorted(links):
            f.write(l+"\n")
