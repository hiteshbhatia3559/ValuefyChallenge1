import re
import requests
import time

start = time.time()

masterUrlList = ['https://medium.com/']
visitedUrlList = set()
i = 0
while i <= 10:
    url = masterUrlList[i]
    print(url)

    response = requests.get(url).text
    newList = re.findall(r'"((https)s?://medium\.com/.*?)"', response)
    newList = set(i[0] for i in newList)

    masterUrlList += newList #adds all elements of newList to masterUrlList

    visitedUrlList.add(url)
    print(len(visitedUrlList))

    masterUrlList = list(dict.fromkeys(masterUrlList))
    print(len(masterUrlList))

    i += 1

elapsed = time.time() - start

print('Visited Url List')
print(visitedUrlList)
print(len(visitedUrlList))

print('Master Url List')
print(masterUrlList)
print(len(masterUrlList))

print("Time Elapsed: {0}s".format(elapsed))