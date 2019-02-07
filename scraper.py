import re
import requests
import anytree
import threading

url = "https://medium.com/"

response = requests.request("GET",url).text
medium_link = re.findall(r'"((https)s?://medium\.com/.*?)"',response)

response = requests.request("GET", url).text
links = re.findall(r'"((https)s?://medium\.com/.*?)"', response)
links = list(i[0] for i in links)

links = set(links)
print(len(links))
links.remove(url)
print(len(links))
# roadmap
# 1. implement tree recursion with repetition checking (could use a dict as a tree data structure? checking possible with that)
# 2. implement a way to show the tree (pdf? picture? research better method)
# 3. write readme (deliverable)
# 4. check for pip-8 compliance (deliverable)
# 5. implement multithreading (deliverable)
