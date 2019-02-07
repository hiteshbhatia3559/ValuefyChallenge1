import re
import requests
import time

start = time.time()

masterUrlList = ['https://medium.com/']
visitedUrlList = set()
for url in masterUrlList:
    response = requests.get(url).text
    newList = re.findall(r'"((https)s?://medium\.com/.*?)"', response)
    newList = set(i[0] for i in newList)

    masterUrlList += newList #adds all elements of newList from masterUrlList

    visitedUrlList.add(url)
    print(url)
    masterUrlList = [i for i in masterUrlList if i not in visitedUrlList]

    if len(visitedUrlList) == 75:
        break


elapsed = time.time() - start

print(visitedUrlList)
print(len(visitedUrlList))

print(masterUrlList)
print(len(masterUrlList))

print("Time Elapsed: {0}s".format(elapsed))