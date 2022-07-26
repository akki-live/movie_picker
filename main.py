from asyncio.log import logger
import random
import logging
import logging.handlers
import requests
from bs4 import BeautifulSoup
import mail

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger_file_handler = logging.handlers.RotatingFileHandler(
    "movie_picker.log",
    maxBytes=1024 * 1024,
    backupCount= 2,
    encoding="utf8",
)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger_file_handler.setFormatter(formatter)
logger.addHandler(logger_file_handler)


URL = 'http://www.imdb.com/chart/top'

def main():
    response = requests.get(URL)

    soup = BeautifulSoup(response.text, 'html.parser')
    movie_name = soup.select('td.titleColumn')
    movie_title = soup.select('td.titleColumn a')
    rate_movie = soup.select('td.ratingColumn strong')


    #print(movie_name)

    #movie_actors = movie_name['title a']

    total = len(movie_name)
    
    idx = random.randrange(0, total)

    year = (movie_name[idx].text).split()[-1]

    actors = movie_title[idx]['title']

    movie = movie_title[idx].text

    rating = rate_movie[idx]['title']


    movie_choice = f"Movie name is \"{movie.upper()}\" was released in \"{year}\" and has rating \"{rating}\", Crue and Casts are \"{actors}\""
    mail.send_mails(movie_choice)
    logger.info(f'Suggested movie name is : {movie.upper()}')
    




if __name__ == "__main__":
    main()
    