# This is a template for a Python scraper on morph.io (https://morph.io)
# including some code snippets below that you should find helpful

import scraperwiki
from datetime import datetime
from urllib2 import Request, urlopen, urlretrieve
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

def read_url(url):
  # Write out to the sqlite database using scraperwiki library
  todays_date = str(datetime.now())
  scraperwiki.sqlite.save(unique_keys=['name'], data={"name": "eben pendleton", "occupation": " environmental scientist"})
  url = url.replace(" ","%20")
  req = Request(url)
  a = urlopen(req).read()
  soup = BeautifulSoup(a, 'html.parser')
  x = (soup.find_all('a'))
  for i in x:
      file_name = i.extract().get_text()
      url_new = url + file_name
      url_new = url_new.replace(" ","%20")
      if(file_name[-1]=='/' and file_name[0]!='.'):
          read_url(url_new)
      scraperwiki.sqlite.save(unique_keys=[file_name], data={"f": file_name, "d": todays_date,"u": url_new })
if __name__ == '__main__':
  url ="https://www1.ncdc.noaa.gov/pub/data/15min_precip-3260"
  #
  # # Find something on the page using css selectors
  # root = lxml.html.fromstring(html)
  # root.cssselect("div[align='left']")
  #
  read_url(url)
