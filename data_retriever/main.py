import threading # since we will run multiple spiders simultaneously, we need to import the threading module
from queue import Queue
from .spider import Spider
from .domain import *
from .general import *


PROJECT_NAME = 'Dogs Database'
HOMEPAGE = 'claudiordgz.github.com/dogs_data'
DOMAIN_NAME = get_domain_name(HOMEPAGE) # the function will get the domain name from the HOMEPAGE variable
QUEUE_FILE = PROJECT_NAME + '/queue.txt' # the location of the queue file
CRAWLED_FILE = PROJECT_NAME + '/crawled.txt' # the location of the crawled file
NUMBER_OF_THREADS = 2 # this number depends on your operating system
queue = Queue() # represents the thread queue

Spider(PROJECT_NAME, HOMEPAGE, DOMAIN_NAME) # the first spider will create the project directory and the data files


def create_jobs(): # this function is called as long there are links that need to be crawled
    for link in file_to_set(QUEUE_FILE):
        queue.put(link) # stores the link in the thread queue
    queue.join()
    crawl() # calls the crawl() function to get the update version


def crawl(): # this function will check if there are items in the queue, and if there are, it will crawl them
    queued_links = file_to_set(QUEUE_FILE) # converts to set
    if len(queued_links) > 0: # checks if there are items that need to be crawled
        print(str(len(queued_links)) + ' links in the queue') # prints the info message
        create_jobs()

def create_workers(): # the function that will create worker threads
    for _ in range(NUMBER_OF_THREADS): # specifies how many threads will be created
        t = threading.Thread(target=work) # creates the worker and passes it the work function as its job
        t.daemon = True # ensures that the thread dies when the main program exits
        t.start() # starts the thread


# Do the next job in the queue
def work():
    while True:
        url = queue.get() # gets the next link in the queue
        Spider.crawl_page(threading.current_thread().name, url) # crawls the URL and displays the thread name
        queue.task_done() # specifies that the processing on the task is done


create_workers()
crawl()