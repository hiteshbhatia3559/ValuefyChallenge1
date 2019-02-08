import threading
import time

def sleeper(n, name) :
    print('Hi, I am {}. Going to sleep for {} seconds \n'.format(name,n))
    time.sleep(n)
    print('{} has woken up from sleep \n'.format(name))


threads_list = []
start = time.time()
for i in range(5):
    t = threading.Thread(target = sleeper, name='Thread {}'.format(i), args=(5, 'Thread {}'.format(i)))
    t.start()
    threads_list.append(t)
    print('{} has started \n'.format(t.name))


for i in threads_list:
    i.join()

elapsed = time.time() - start
print('All threads have finished jobs')
print('Time taken : '+str(elapsed))