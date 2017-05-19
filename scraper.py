# This is a template for a Python scraper on morph.io (https://morph.io)
# including some code snippets below that you should find helpful

import scraperwiki
from datetime import datetime
import requests
from bs4 import BeautifulSoup
# import lxml.html
#
# # An arbitrary query against the database
# scraperwiki.sql.select("* from data where 'name'='peter'")

# You don't have to do things with the ScraperWiki and lxml libraries.
# You can use whatever libraries you want: https://morph.io/documentation/python
# All that matters is that your final data is written to an SQLite database
# called "data.sqlite" in the current working directory which has at least a table
# called "data".

def listFD(url, ext=''):
    page = requests.get(url).text
    soup = BeautifulSoup(page, 'html.parser')
    return [url + '/' + node.get('href') for node in soup.find_all('a') if node.get('href').endswith(ext)]




def read_url(url):
  # Write out to the sqlite database using scraperwiki library
  todays_date = str(datetime.now())
  scraperwiki.sqlite.save(unique_keys=['name'], data={"name": "eben pendleton", "occupation": " environmental scientist"})
  for file_name in listFD(url):
      print(file_name,todays_date)
      #scraperwiki.sqlite.save(unique_keys=[file_name], data={"f": file_name, "d": todays_date })
if __name__ == '__main__':
  url ="https://www1.ncdc.noaa.gov/pub/data/15min_precip-3260"
  #
  # # Find something on the page using css selectors
  # root = lxml.html.fromstring(html)
  # root.cssselect("div[align='left']")
  #
  read_url(url)
