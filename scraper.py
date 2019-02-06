import re
import requests

url = "https://medium.com/"

response = requests.request("GET",url).text
medium_link = re.findall(r'"((https)s?://medium\.com/.*?)"',response)

new_list = [] #has all the urls
for item in medium_link:
    (x,y) = item
    if x != 'https://medium.com/':
        new_list.append(x)

print(len(new_list))

# roadmap
# 1. implement tree recursion with repetition checking (could use a dict as a tree data structure? checking possible with that)
# 2. implement a way to show the tree (pdf? picture? research better method)
# 3. write readme (deliverable)
# 4. check for pip-8 compliance (deliverable)
