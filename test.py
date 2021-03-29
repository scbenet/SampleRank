import bs4
import urllib3
import re
import html
import sys


def get_samples_from_page(url):

    # Gets html from the specified page
    http = urllib3.PoolManager()
    r = http.request('GET', url)

    # Converts data to string and isolates relevant part of page
    htm = str(r.data)
    matc = []
    if "Contains samples" in htm:
        # htm = htm.split("Contains samples")[1]
        # htm = htm.split("Was sampled")[0]
        # htm = htm.split("Was covered")[0]

        # Gets list of samples in the song
        matches = re.findall('title=".*?"', htm)
        matc = matc + list(set(matches))

        matc = list(filter((lambda x: "\\'s" in x), matc))

        for n in range(len(matc)):
            matc[n] = matc[n].removeprefix("title=\"")
            matc[n].removesuffix("\"")
            re.sub(r'\W+', '', matc[n])
            matc[n] = html.unescape(matc[n])

        for mat in matc:
            print(mat)


if __name__ == "__main__":
    args = sys.argv

    artist = args[1]
    song_title = args[2]

    artist = artist.replace(" ", "-")
    song_title = song_title.replace(" ", "-")
    ws_url = f'https://www.whosampled.com/{artist}/{song_title}/samples'
    print(ws_url)
    get_samples_from_page(ws_url)

