from urllib.parse import urlparse # imports the module for URL parsing

def get_domain_name(url):
    try:
        results = get_sub_domain_name(url).split('.') # splits the URL so we can return only the last two elements (such as example.com)
        return results[-2] + '.' + results[-1] # returns only the last two elements in the list
    except:
        return ''

def get_sub_domain_name(url):
    try:
        return urlparse(url).netloc
    except:
        return '' # ensures that at least something is returned


