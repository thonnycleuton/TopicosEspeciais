from requests import get
from bs4 import BeautifulSoup


class Movie:

    def __init__(self, title, cotacao):
        self.title = title
        self.cotacao = cotacao

    def __repr__(self):
        return repr((self.title, self.cotacao))


url = 'https://www.imdb.com/chart/boxoffice'
response = get(url)

html_soup = BeautifulSoup(response.text, 'html.parser')
movies = html_soup.find('table', {'class': 'chart full-width'}).find('tbody').find_all('tr')
movie_list = []
for movie in movies:
    title = movie.find('td', {'class': 'titleColumn'}).text.strip()
    cotacao = movie.find('td', {'class': 'ratingColumn'}).text.strip()
    movie_list.append(Movie(title=title, cotacao=cotacao))

sorted(movie_list, key=lambda movie: movie.cotacao)
print(movie_list)