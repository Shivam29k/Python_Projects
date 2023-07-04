import requests
from bs4 import BeautifulSoup

response = requests.get(url="https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

titles = [title_tag.getText() for title_tag in soup.find_all(name="span", class_="titleline")]
links = [title_tag.find("a").get("href") for title_tag in soup.find_all(name="span", class_="titleline")]

upvotes = [int(point.text.split(" ")[0]) for point in soup.find_all(name="span", class_="score")]
sorted_upvotes = sorted(upvotes, reverse=True)


index_list = [upvotes.index(score) for score in sorted_upvotes]

sorted_titles = [titles[index] for index in index_list]
sorted_links = [links[index] for index in index_list]

# most upvoted article and its link
print(sorted_titles[0])
print(sorted_links[0])

