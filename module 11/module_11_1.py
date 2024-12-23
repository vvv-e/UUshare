# Домашнее задание по теме "Обзор сторонних библиотек Python"
import requests
import pandas as pd
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from itertools import chain

if __name__ == "__main__":
    """
    # requests
    print("-" * 50, "requests", "-" * 50)
    UU_URL = "https://urban-university.pro"
    res = requests.get(UU_URL)
    if str(res) == "<Response [200]>":
        print(res.content)
    else:
        print(f"что-то пошло не так, код={res}")

    # это из пройденного материала
    ACCESS_TOKEN = 'CXyFeSBw2lAdG41xkuU3LS6a_nwyxwwCz2dCkUohw-rw0C49x2HqP__6_4is5RPx'
    RANDOM_GENRE_API_URL = 'https://binaryjazz.us/wp-json/genrenator/v1/genre'
    GENIUS_API_URL = 'https://api.genius.com/search'
    GENIUS_URL = 'https://api.genius.com'
    for i in range(5):
        genre = requests.get(RANDOM_GENRE_API_URL).json()
        print(genre)
        for j in range(10):
            data = requests.get(GENIUS_API_URL, params={'access_token': ACCESS_TOKEN, 'q': genre})
            data = data.json()
            try:
                song_id = data['response']['hits'][0]['result']['api_path']
                s = f"{GENIUS_URL}{song_id}/apple_music_player"
                print(s)
                break
            except IndexError as e:
                pass
    
    # pandas
    print("-" * 50, "pandas", "-" * 50)
    flp = pd.read_csv("s3.csv", sep=";")
    print(flp)
    print(flp[["AVGDLJEM", "AVGDL16"]].describe())
    with pd.ExcelWriter("s3.xlsx") as writer:
        flp.to_excel(writer)
    flp = None
    
    # numpy
    print("-" * 50, "numpy", "-" * 50)
    narr =  np.array([[2, 6, 1], [4, 5, 3]])
    narr.sort()
    print(narr)
    narr = narr.T
    print(narr)
    np.savetxt('narr.csv', narr)
    np = None
    """

    # matplotlib + pandas
    print("-" * 50, "matplotlib", "-" * 50)
    flp = pd.read_csv("s3.csv", sep=";")
    flp["DELTA1"] = (flp["AVGDLJEM"] - flp["AVGDL16"])
    flp["DELTA2"] = (flp["GMDLJEM"] - flp["GMDL16"])
    array1 = flp[["DELTA1"]].to_numpy()
    array2 = flp[["DELTA2"]].to_numpy()
    flat_list1 = list(chain(*array1))
    flat_list2 = list(chain(*array2))
    plt.hist([flat_list1, flat_list2], bins=100, histtype='step')
    plt.semilogy()
    plt.show()
    flp = None
    plt = None

    # pillow
    print("-" * 50, "pillow", "-" * 50)
