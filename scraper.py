import requests
import multiprocessing
import time
import re
import random
import scraperlib as sl

if __name__ == '__main__':
    length = 0
    visited_urls = []
    internal_url_list = []
    start = time.time()
    p = multiprocessing.Pool(5)

    def scrape(url):
        global length
        global visited_urls
        global internal_url_list
        global p
        if length is 0:
            internal_url_list.append(url)
        links = sl.get_data(url)
        for item in links:
            if length > 5:
                break
            if item not in visited_urls:
                sl.make_sleep()
                length += 1
                visited_urls.append(item)
                internal_url_list.append(item)
                with p:
                    scrape(item)




    top_url = "https://medium.com/"
    scrape(top_url)
    elapsed = time.time() - start
    # print(RenderTree(internal_url_tree[0], style=render.ContRoundStyle()))
    print('Time elapsed : '+str(elapsed)+' seconds')
    print(visited_urls)