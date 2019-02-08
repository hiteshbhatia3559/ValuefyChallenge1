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
            links = sl.get_data(url)
        except:
            print('Connection to host not found, skipping url...')
            links = {}
            #assigns empty links if url getting fails so url skips
        for item in links:
            if length > 10:
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