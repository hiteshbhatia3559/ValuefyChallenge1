import requests
import time
import re
import random

def make_sleep():
    time.sleep(random.randint(0,2))  # So packets dont look suspicious

def get_data(url,visited_urls):
    response = requests.request("GET", url).text
    links = re.findall(r'"((https)s?://medium\.com/.*?)"', response)
    links = list(i[0] for i in links)
    links = set(links)
    visited_urls.append(url)
    return [links,visited_urls]