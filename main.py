import sys
import os
import requests
from urllib.parse import urlparse
import pprint
from dotenv import load_dotenv

load_dotenv()

BITLY_TOKEN = os.getenv("TOKEN")


def shorten_link(token, url):
    api_url = "https://api-ssl.bitly.com/v4/shorten"
    headers = {"Authorization": "Bearer {token}".format(token=token)}
    payload = {"long_url": url}
    response = requests.post(api_url, headers=headers, json=payload)
    response.raise_for_status()
    return response.json()['link']


def count_clicks(token, link):
    parsed = urlparse(link)
    url = parsed.netloc + parsed.path
    headers = {"Authorization": "Bearer {token}".format(token=token),
               "unit": "day", "units": "-1"}
    clicks_count_url = "https://api-ssl.bitly.com/v4/bitlinks/" \
        + "{url}/clicks/summary".format(url=url)
    clicks_count = requests.get(clicks_count_url, headers=headers)
    clicks_count.raise_for_status()
    return clicks_count.json()


def main():
    if not sys.argv[1].startswith("https://bit.ly"):
        bitlink = None
        try:
            bitlink = shorten_link(token, sys.argv[1])
            print("Битлинк {link}".format(link=bitlink))
        except requests.exceptions.HTTPError as error:
            print("Ошибка: {error}".format(error=error))
    else:
        try:
            clicks_count = count_clicks(token, sys.argv[1])
            pprint.pprint(clicks_count)
        except requests.exceptions.HTTPError as error:
            print("Ошибка: {error}".format(error=error))


if __name__ == '__main__':
    main()
