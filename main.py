import sys
import os
import requests
from urllib.parse import urlparse
import pprint
from dotenv import load_dotenv


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
    bitly_api_url = f"https://api-ssl.bitly.com/v4/bitlinks/{url}"
    headers = {"Authorization": "Bearer {token}".format(token=token),
               "unit": "day", "units": "-1"}
    clicks_count_url = f"{bitly_api_url}/clicks/summary"
    clicks_count = requests.get(clicks_count_url, headers=headers)
    clicks_count.raise_for_status()
    return clicks_count.json()


def exist_bitly(token, link):
    parsed = urlparse(link)
    url = parsed.netloc + parsed.path
    bitly_api_url = f"https://api-ssl.bitly.com/v4/bitlinks/{url}"
    headers = {"Authorization": "Bearer {token}".format(token=token)}
    response = requests.get(bitly_api_url, headers=headers)
    try:
        response.raise_for_status()
        return True
    except Exception:
        return False


def main():

    load_dotenv()

    token = os.getenv("TOKEN")

    # sys.argv is a list of command line arguments
    if exist_bitly(sys.argv[1]):
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
