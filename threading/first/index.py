import threading, time

lock = threading.Lock()

results = {}

def fetch(item_id):
    print("Inside fetch function for item_id:", item_id)
    time.sleep(2)
    
    lock.acquire()
    print("Lock acquired for item_id:", item_id)
    try:
        results[item_id] = item_id * 10
    finally:
        lock.release()
        print("Lock released for item_id:", item_id)

threads = [threading.Thread(target=fetch, args=(i,)) for i in range(10)]

# The start method ask the os to create a new thread of execution and run your target function in that thread. 
# The start method returns immediately and the new thread runs concurrently with the main thread.

start_time = time.time()

for thread in threads:
    thread.start()

print("This is printed while the threads are running.")

print("Results so far:", results)


# The join method blocks the calling thread (in this case, the main thread) until the thread whose join() method is called is terminated.

for thread in threads:
    thread.join()



end_time = time.time()
print("Total Time", (end_time - start_time))

print("This is printed after the threads have completed.")
print("Results:", results)