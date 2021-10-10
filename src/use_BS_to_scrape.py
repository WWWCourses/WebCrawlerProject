from bs4 import BeautifulSoup


def read_file():
	with open("./test.html","r") as f:
		content = f.read()
		return content


html = read_file()
soup = BeautifulSoup(html, 'html.parser')

# get elements by string content
extraced = soup.find_all(string="Main Title")

for e in extraced:
	print(e)


# find first element by tag name:
el = soup.find("li")
# # print(el.findChildren())
print(el.contents)