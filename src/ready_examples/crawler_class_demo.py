import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import logging

logging.basicConfig(format='%(asctime)s - %(message)s', datefmt="%H:%M:%S", level=logging.INFO)

class Crawler:
	def __init__(self, seed=[]):
		self.urls_to_visit = seed
		self.urls_visited = []

	def get_HTML(self, url, *args):
		r = requests.get(url, *args)
		return r.text

	def get_JSON(self, url, *args):
		r = requests.get(url, *args)
		return r.json()

	def extract_links_to_visit(self,url):
		html = self.get_HTML(url)

		# parse:
		soup = BeautifulSoup(html, 'html.parser')
		for link in soup.find_all('a'):
			href = link.get('href')
			if href and href.startswith('/'):
				self.urls_to_visit.append(urljoin(url, href))

	def crawl(self, url, level=1):
		logging.info(f"Crawling: {url}")
		self.extract_links_to_visit(url)
		self.urls_visited.append(url)

	def log_visited_urls(self, filename):
		with open(filename, 'w') as f:
			f.writelines('\n'.join(self.urls_visited))

	def run(self):
		url = self.urls_to_visit.pop(0)
		while self.urls_to_visit:
			url = self.urls_to_visit.pop()
			if url not in self.urls_visited:
				self.urls_visited.append(url)
				self.crawl(url)


if __name__ == '__main__':
	crawler = Crawler(seed=['https://webscraper.io/test-sites/e-commerce/static/computers/laptops'])
	crawler.run()
	crawler.log_visited_urls('urls.txt')

