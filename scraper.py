import requests
from queue import Queue
import threading
import time
import re
import random


length = 0
visited_urls = []
internal_url_list = []
start = time.time()
thread_list = []
globalid = ''

def make_sleep():
    time.sleep(random.randint(1, 3))  # So packets dont look suspicious

def get_data(url):
    global visited_urls
    response = requests.request("GET", url).text
    links = re.findall(r'"((https)s?://medium\.com/.*?)"', response)
    links = list(i[0] for i in links)
    links = set(links)
    visited_urls.append(url)
    return links

def scrape(url):
    global length
    global visited_urls
    global internal_url_list
    if length is 0:
        internal_url_list.append(url)
    links = get_data(url)
    for item in links:

        if length > 5:
            break
        if item not in visited_urls:
            make_sleep()
            length += 1
            visited_urls.append(item)
            internal_url_list.append(item)
            scrape(item)

top_url = "https://medium.com/"
scrape(top_url)
elapsed = time.time() - start
# print(RenderTree(internal_url_tree[0], style=render.ContRoundStyle()))
print('Time elapsed : '+str(elapsed)+' seconds')
print(visited_urls)