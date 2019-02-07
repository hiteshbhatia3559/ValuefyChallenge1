import re
import requests
from anytree import Node, RenderTree, search, render
import threading
import time
import random
import json

length = 0
visited_urls = []
internal_url_tree = []
start = time.time()


def run(url):
    global length
    global visited_urls
    global internal_url_tree
    if length is 0:
        internal_url_tree.append(Node(url))
    response = requests.request("GET", url).text
    links = re.findall(r'"((https)s?://medium\.com/.*?)"', response)
    links = list(i[0] for i in links)
    links = set(links)
    try:
        links.remove(url)
    except:
        print('')
    visited_urls.append(url)
    print(url)
    #Recursion here
    for item in links:

        if length > 5:
            break
        if item not in visited_urls:
            # print(item+' is child of '+url)
            time.sleep(random.randint(1, 3)) #So packets dont look suspicious
            length += 1

            visited_urls.append(item)
            internal_url_tree.append(Node(item, parent=search.findall_by_attr(internal_url_tree[0],url)[0]))
            run(item)
            print(length)




top_url = "https://medium.com/"

run(top_url)
elapsed = time.time() - start
print(RenderTree(internal_url_tree[0], style=render.ContRoundStyle()))
print('Time elapsed : '+str(elapsed)+' seconds')


# roadmap
# 1. implement tree recursion with repetition checking (could use a dict as a tree data structure? checking possible with that) #DONE
# 2. implement a way to show the tree (pdf? picture? research better method) #CAN BE DONE
# 3. write readme (deliverable) #DOING
# 4. check for pip-8 compliance (deliverable) #PENDING
# 5. implement multithreading (deliverable) #PENDING
