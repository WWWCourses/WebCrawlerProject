# import lib
from lib.crawler import Crawler
from lib.scraper import Scraper
from lib.db import DB


# import lib.crawler as crw

if __name__ == '__main__':
	# crawler = Crawler('https://www.autokelly.bg/bg/products/43758570.html?ids=39849642;51224611')
	# crawler.run_crawler()
	# scraper = Scraper(crw_links=crawler.raw_links)
	# scraper.scrape_links_to_text()

	db = DB()
	tables = db.reflect('car_parts_gui')

