import getopt
import sys
import requests
import csv
import urllib.request
from urllib.parse import urlparse, urljoin

def is_valid(url):
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)

def read_links_from_csv(base_url):
	parsed_base_url = urlparse(base_url)
	parsed_base_url_scheme = parsed_base_url.scheme
	parsed_base_url_netloc = parsed_base_url.netloc
	with open('URLList.csv') as csv_file:
		csv_reader = csv.reader(csv_file, delimiter='\n')
		for row in csv_reader:
			url = row[0]
			parsed_href = urlparse(url)
			new_url = parsed_base_url_scheme + "://" + parsed_base_url_netloc + parsed_href.path
			if parsed_href.query != "":
				new_url = new_url + "?" + parsed_href.query
			status = get_status(new_url)
			write_link_data_to_csv([new_url, status])


def get_status(url):
	r = requests.head(url)
	return r.status_code

def write_link_data_to_csv(data):
	with open('URLStatusList.csv', mode='a') as url_file:
		url_writer = csv.writer(url_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		url_writer.writerow(data)	


if __name__ == "__main__":
	argumentList = sys.argv[1:]
	options = "u:f:"
	try:
		arguments, values = getopt.getopt(argumentList, options)
		for currentArgument, currentValue in arguments:
			if currentArgument == '-u':
				if is_valid(currentValue):
					read_links_from_csv(currentValue)
				else:
					print("Please provide a valid base URL for the website.")
	except getopt.error as err:
		print (str(err))
