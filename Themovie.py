#Basic movie archive with API
import requests

class TheMovieDb():
    def __init__(self):
        self.api_url = "https://api.themoviedb.org/3"
        self.api_key = "<api_key>"
    
    def getPopular(self):
        response = requests.get(f"{self.api_url}/movie/popular?api_key={self.api_key}&language=en-US&page=1")
        return response.json()

    def searchMovies(self,key):
        response = requests.get(f"{self.api_url}/search/keyword?api_key={self.api_key}&query={key}&page=1")
        return response.json()

theMovie = TheMovieDb()

while True:
    secim = input('1- Popular Movie\n2- Search Movies\n3- Exit')

    if secim == '3':
        print('Logged Out..')
        break
    else:
        if secim == '1':
            movies = theMovie.getPopular()
            for movie in movies['results']:
                print(movie['title'])
        elif secim == '2':
            keyword = input('keywords:')
            movies = theMovie.searchMovies(keyword)
            for movie in movies['results']:
                print(movie['name'])