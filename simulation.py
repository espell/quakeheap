import time
from fibheap import Fib_Heap
from quake import quake_heap

print("######## Fibonacci #########")
start = time.time_ns()
queue = Fib_Heap()
for i in range(1000):
    queue.pq_insert(queue, i, i)
#don't include debugging print statements if you're trying to get an accurate time
#print(queue.pq_get_size(queue))
#min = queue.pq_find_min(queue)
#print(min.key)
queue.pq_delete_min(queue)
#min = queue.pq_find_min(queue)
end = time.time_ns()
print("Time (in ns) to insert 1000 elements and then delete min: ")
print(end - start)
print("")
#print(min.key)

print("########## Quake ############")
start = time.time_ns()
queue = quake_heap()
for i in range(1000):
    queue.pq_insert(i, i)
#don't include debugging print statements if you're trying to get an accurate time
#print(queue.pq_get_size(queue))
#min = queue.pq_find_min(queue)
#print(min.key)
queue.pq_delete_min()
#min = queue.pq_find_min(queue)
end = time.time_ns()
print("Time (in ns) to insert 1000 elements and then delete min: ")
print(end - start)
