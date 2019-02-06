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
