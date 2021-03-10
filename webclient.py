#!/usr/bin/env python3

from urllib.request import urlopen
from urllib.parse import urljoin
import bs4


class WebClient(object):
	# print results

	def __init__(self):
		pass

	# get web page
	def get_web_page(self):
		webpage = urlopen("http://bid.udl.cat/ca/")
		html = webpage.read()
		return html

	def parse_web_page(self, html):
		titles = []
		links = []
		dates = []
		soup = bs4.BeautifulSoup(html, features="lxml")
		news = soup.find_all("li", "box")  # Tot el element de llista
		for new in news:
			title_tag = new.find("a")  # Tot el tag de l'enllaç a la notícia
			titles.append(title_tag['title'])  # Solament el text del títol

			link = urljoin("http://bid.udl.cat/ca/", title_tag['href'])
			links.append(link)  # Text del link

			time_tag = new.find("time")
			dates.append(time_tag.text.strip())
		return titles, links, dates

	def get_information(self):
		html = self.get_web_page()
		# read information from web page
		info = self.parse_web_page(html)
		return info


if __name__ in "__main__":
	client = WebClient()
	information = client.get_information()
	for i in range(len(information[0])):
		print(information[0][i])
		print(information[1][i])
		print(information[2][i])
		print()
