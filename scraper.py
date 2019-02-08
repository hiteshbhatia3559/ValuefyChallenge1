import multiprocessing
import time
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
        #BLOCK BELOW IS GETTING ALL LINKS FOR THE URL
        try:
            data_list = sl.get_data(url, visited_urls)
            links = data_list[0]
            visited_urls = data_list[1]
        except:
            print('Connection to host not found, skipping url...')
            links = {}
            #assigns empty links if url getting fails so url skips
        for item in links:
            if length > 2: #CHANGE THIS NUMBER WITH HOW MANY URLS YOU NEED
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
    print('Time elapsed : '+str(elapsed)+' seconds')
    print(visited_urls)
    with open('saved_urls','w') as WriteFile:
        for listed_item in internal_url_list:
            WriteFile.write(listed_item)
            WriteFile.write(',')