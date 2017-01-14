'''
This script extract all the products names from website consumer reports
link: http://www.consumerreports.org/cro/a-to-z-index/products/index.htm 
'''

from fake_useragent import UserAgent
import requests
from bs4 import BeautifulSoup
import collections

# fake user agent in this script chrome.
ua = UserAgent()

#url
url = "http://www.consumerreports.org/cro/a-to-z-index/products/index.htm"

#fetching url 
fhand = requests.get(url, headers={'user-agent': ua.chrome})

#getting data
data = fhand.content

#making soup
soup = BeautifulSoup(data, 'lxml')

#extracting all div which has attribute class: entry-letter
all_divs = soup.find_all('div',attrs={'class':'entry-letter'})

#listing names
name = [d.div.a.span.string for d in all_divs]

#listing corresponding url
url = [d.div.a.get('href') for d in all_divs]

#Initialize dictionary of name: url 
D = collections.defaultdict()

#update dictionary with name as key and url as value
D.update(zip(name, url))

#printing data
for key, value in D.items():
	print key + '  ---->  ' + value