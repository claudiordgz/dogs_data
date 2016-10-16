from urllib.request import urlopen # a module that enables us to connect to webpages
from .link_finder import LinkFinder
from .domain import *
from .general import *

class Spider:

    project_name = '' # the name of the project
    base_url = '' # usually the homepage URL
    domain_name = '' # this variable will help us ensure that we are connecting to a valid domain name
    queue_file = '' # the location of the queue file
    crawled_file = '' # the location of the crawled file
    queue = set() # creates a set for the links in queue
    crawled = set() # creates a set for the crawled links

    def __init__(self, project_name, base_url, domain_name):
        Spider.project_name = project_name # sets the value for the class variable, so that all spiders have the same information
        Spider.base_url = base_url
        Spider.domain_name = domain_name
        Spider.queue_file = Spider.project_name + '/queue.txt' # defines the path for the queue file
        Spider.crawled_file = Spider.project_name + '/crawled.txt'
        self.boot() # the method that will create the project directory and the data files
        self.crawl_page('First spider', Spider.base_url) # the method that will start the page crawling and print the message to the user

    @staticmethod  # defines the method as static
    def boot():
        create_project_dir(Spider.project_name)  # creates the project folder using the name provided by the user
        create_data_files(Spider.project_name,
                          Spider.base_url)  # creates data files and add the homepage to the queue file
        Spider.queue = file_to_set(
            Spider.queue_file)  # converts the links from the queue file to a set for faster operation
        Spider.crawled = file_to_set(Spider.crawled_file)  # converts the links from the crawled file to a set

    @staticmethod
    def crawl_page(thread_name, page_url): # the method that will start the crawling
        if page_url not in Spider.crawled: # ensures that the page wasn't already crawled
            print(thread_name + ' now crawling ' + page_url) # displays the page that is being crawled
            print('Queue ' + str(len(Spider.queue)) + ' | Crawled  ' + str(len(Spider.crawled))) # prints how many links are in the waiting list and how many links have already been crawled
            Spider.add_links_to_queue(Spider.gather_links(page_url)) # adds the links to the waiting list
            Spider.queue.remove(page_url)  # removes the page that has been crawled from the queue set
            Spider.crawled.add(page_url) # adds the page that has been crawled to the crawled set
            Spider.update_files() # converts sets to files


    # Converts raw response data into readable information and checks for proper HTML formatting
    @staticmethod
    def gather_links(page_url): # the method that will crawl a page and return the set of links
        html_string = '' # the variable that will hold the HTML string
        try: # the try...except statement ensures that our program won't crash if there is an exception
            response = urlopen(page_url) # the variable that will hold the response (in byte data)
            if 'text/html' in response.getheader('Content-Type'): # checks if the crawled page contains an actual HTML data
                html_bytes = response.read() # reads the response (in byte data)
                html_string = html_bytes.decode("utf-8") # converts the raw data into an HTML string
            finder = LinkFinder(Spider.base_url, page_url) # creates the LinkFinder object
            finder.feed(html_string) # parses the HTML data
        except Exception as e:
            print(str(e)) # prints the error
            return set() # returns an empty set
        return finder.page_links() # returns links

    @staticmethod
    def add_links_to_queue(links):  # the function that will take a set of links and add them to the waiting list
        for url in links:  # loops through the set
            if (url in Spider.queue) or (
                url in Spider.crawled):  # checks if links are already in the waiting or the crawled list
                continue
            if Spider.domain_name != get_domain_name(
                    url):  # checks if the domain name is present in the URL. This ensures that the crawler will crawl only pages on the targeted website, and not the external links present on the website.
                continue
            Spider.queue.add(url)  # adds link to the waiting list

    @staticmethod
    def update_files():  # updates the files
        set_to_file(Spider.queue, Spider.queue_file)
        set_to_file(Spider.crawled, Spider.crawled_file)