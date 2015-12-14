# Closely based on a template for a Python scraper from morph.io (https://morph.io)
import scraperwiki
import lxml.html

# # Read in page data
html = scraperwiki.scrape("http://www.aec.gov.au/Elections/Australian_Electoral_History/Federal_State_and_Territory_elections_dates_1946_Present.htm")
#
# # Find something on the page using css selectors
root = lxml.html.fromstring(html)

for tr in root.cssselect("tbody>tr"):
  tds=tr.cssselect("td")
  year=tds[0].text_content()
  date=tds[1].text_content()
  electionType=tds[2].text_content()
  
#
# # Write out to the sqlite database using scraperwiki library
  scraperwiki.sqlite.save(unique_keys=['electionType','year'], data={"year": year, "date": date, "electionType": electionType})
#
# # An arbitrary query against the database
# scraperwiki.sql.select("* from data where 'name'='peter'")

# You don't have to do things with the ScraperWiki and lxml libraries.
# You can use whatever libraries you want: https://morph.io/documentation/python
# All that matters is that your final data is written to an SQLite database
# called "data.sqlite" in the current working directory which has at least a table
# called "data".
