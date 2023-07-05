import requests
from bs4 import BeautifulSoup

response = requests.get(url="https://www.empireonline.com/movies/features/best-movies-2/")
top_movies_webpage = response.text

soup = BeautifulSoup(top_movies_webpage, "html.parser")

content_tag = soup.find_all(name="div", class_ = "jsx-1913936986 listicle-item-content" )
review_text = [content.find_all("p")[-1].getText() for content in content_tag]
# for content in content_tag:
#     print(content.find_all("p")[-1].getText())

movie_name = [text.split("review of ")[-1] for text in review_text][::-1]
# for text in review_text:
#     movie = text.split("review of ")[-1]
#     movie_name.append(movie)


with open("top_100_movies.txt", "a") as file:
    index = 1
    for movie in movie_name:
        file.write(f"{index}. {movie}\n")
        index+=1


