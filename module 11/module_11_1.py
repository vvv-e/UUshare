# Домашнее задание по теме "Обзор сторонних библиотек Python"
import requests


if __name__ == "__main__":
    ACCESS_TOKEN = 'CXyFeSBw2lAdG41xkuU3LS6a_nwyxwwCz2dCkUohw-rw0C49x2HqP__6_4is5RPx'
    RANDOM_GENRE_API_URL = 'https://binaryjazz.us/wp-json/genrenator/v1/genre'
    GENIUS_API_URL = 'https://api.genius.com/search'
    GENIUS_URL = 'https://api.genius.com'
    genre = requests.get(RANDOM_GENRE_API_URL).json()
    print(genre)

