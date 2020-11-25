import getopt
import sys
import requests
import csv
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup

internal_urls = set()

def is_valid(url):
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)

def get_all_website_links(url):
    urls = set()
    domain_name = urlparse(url).netloc
    soup = BeautifulSoup(requests.get(url).content, "html.parser")
    for a_tag in soup.findAll("a"):
        href = a_tag.attrs.get("href")
        if href == "" or href is None:
            continue    
        href = urljoin(url, href)
        parsed_href = urlparse(href)
        href = parsed_href.scheme + "://" + parsed_href.netloc + parsed_href.path
        if parsed_href.query != "":
        	href = href + "?" + parsed_href.query
        if not is_valid(href):
            continue
        if href in internal_urls:
            continue
        if domain_name not in href:
            continue
        urls.add(href)
        internal_urls.add(href)
        write_to_csv(href)
    return urls

total_urls_visited = 0

def crawl(url):
    links = get_all_website_links(url)
    for link in links:
        crawl(link)

def write_to_csv(href):
	with open('URLList.csv', mode='a') as url_file:
		url_writer = csv.writer(url_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		url_writer.writerow([href])

if __name__ == "__main__":
	argumentList = sys.argv[1:]
	options = "u:"
	try:
		arguments, values = getopt.getopt(argumentList, options)
		for currentArgument, currentValue in arguments:
			if currentArgument == '-u':
				if is_valid(currentValue):
					crawl(currentValue)
				else:
					print("Please provide a valid base URL for the website.")
	except getopt.error as err:
		print (str(err))
    
