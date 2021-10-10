import requests
import os
import re
from bs4 import BeautifulSoup

def get_filename(url):
	rx = re.compile(r"^https?://(.+?)(?:/|$)")
	m = rx.search(url)
	if m:
		filename = m.group(1)
		return filename


def	save_to_file(content, filename):
	with open(SCRIPT_FOLDER+'/data/'+filename,"w") as f:
		f.write(content)


class Crawler:
	def __init__(self,seed):
		self.urls_to_visit = []
		self.urls_visited = []

		for url in seed:
			self.urls_to_visit.append(url)

	def extract_links(self, content):
		pass

	def get_page_content(url):
		r = requests.get(url, verify=False)
		r.encoding="utf-8"

		content = r.text








seed = ['https://www.autokelly.bg']
crawler = Crawler(seed)