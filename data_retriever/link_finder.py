from html.parser import HTMLParser
from urllib import parse # defines a standard interface to break URL strings up in components

class LinkFinder(HTMLParser): # creates a new class that will inherit from HTMLParser

    def __init__(self, base_url, page_url):
        super().__init__()
        self.base_url = base_url
        self.page_url = page_url
        self.links = set()

    def handle_starttag(self, tag, attrs):
        if tag == 'a':  # checks if the tag is a link
            for (attribute, value) in attrs:
                if attribute == 'href':  # checks if the link attribute is href, which represents a link
                    url = parse.urljoin(self.base_url,value)  # if a link is a relative link, adds the domain name to it.
                    self.links.add(url)  # adds the URL to the set

    def page_links(self):
        return self.links

    def error(self, message):
        pass