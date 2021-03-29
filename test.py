import bs4
import urllib3
import re
import html
import sys


def get_samples_from_page(url):

    # Gets html from the specified page, if no sample page return empty list
    http = urllib3.PoolManager()
    try:
        r = http.request('GET', url)
    except:
        return []

    # Converts data to string (make it searchable with regex)
    htm = str(r.data)

    # Gets list of samples in the song
    matches = re.findall('title=".*?"', htm)
    matc = list(set(matches))

    matc = list(filter((lambda x: "\\'s" in x), matc))

    # Format list
    for n in range(len(matc)):
        matc[n] = matc[n].removeprefix("title=\"")
        matc[n] = html.unescape(matc[n])
        matc[n] = matc[n].removesuffix('\"')
    # Print list to console
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

