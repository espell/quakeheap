import time
from fibheap import Fib_Heap
from quake import quake_heap

def fibInsert(k):
    start = time.time_ns()
    queue = Fib_Heap()
    for i in range(k):
        queue.pq_insert(queue, i, i)
    end = time.time_ns()
    return (end - start)

def quakeInsert(k):
    start = time.time_ns()
    queue = quake_heap()
    for i in range(k):
        queue.pq_insert(i, i)
    end = time.time_ns()
    return (end - start)

def fibStraightInsert(k):
    start = time.time_ns()
    queue = Fib_Heap()
    for i in range(k):
        queue.pq_insert(queue, i, i)
    queue.pq_delete_min(queue)
    end = time.time_ns()
    return (end - start)

def quakeStraightInsert(k):
    start = time.time_ns()
    queue = quake_heap()
    for i in range(k):
        queue.pq_insert(i, i)
    queue.pq_delete_min()
    end = time.time_ns()
    return (end - start)

def fibInsertDelete(k):
    start = time.time_ns()
    queue = Fib_Heap()
    for i in range(k):
        queue.pq_insert(queue, i, i)
    i = 0
    for i in range(k//2 + k//3):
        try:
            queue.pq_delete_min(queue)
        except:
            end = time.time_ns()
            return (end - start)
    end = time.time_ns()
    return (end - start)

def quakeInsertDelete(k):
    start = time.time_ns()
    queue = quake_heap()
    for i in range(k):
        queue.pq_insert(i, i)
    i = 0
    for i in range(k//2 + k//3):
        queue.pq_delete_min()

    end = time.time_ns()
    return (end - start)


def quakeInsert10Delete2(k):
    start = time.time_ns()
    queue = quake_heap()
    i = 1
    while i <= k:
        for ctr in range(10):
            queue.pq_insert(ctr, ctr)
        queue.pq_delete_min()
        queue.pq_delete_min()
        i += 1
    end = time.time_ns()
    return (end - start)

def fibInsert10Delete2(k):
    start = time.time_ns()
    queue = Fib_Heap()
    i = 1
    while i <= k:
        for ctr in range(10):
            queue.pq_insert(queue, ctr, ctr)
        queue.pq_delete_min(queue)
        queue.pq_delete_min(queue)
        i += 1
    end = time.time_ns()
    return (end - start)

def quakeInsert2Delete1(k):
    start = time.time_ns()
    queue = quake_heap()
    i = 1
    while i <= k:
        for ctr in range(2):
            queue.pq_insert(ctr, ctr)
        queue.pq_delete_min()
        i += 1
    end = time.time_ns()
    return (end - start)

def fibInsert2Delete1(k):
    start = time.time_ns()
    queue = Fib_Heap()
    i = 1
    while i <= k:
        for ctr in range(2):
            queue.pq_insert(queue, ctr, ctr)
        queue.pq_delete_min(queue)
        i += 1
    end = time.time_ns()
    return (end - start)

def fibInsertkDeleteHalf(k):
    start = time.time_ns()
    queue = Fib_Heap()
    i = 0
    while i <= k:
        queue.pq_insert(queue, i, i)
        i += 1
    i = 0
    while i <= k/2:
        queue.pq_delete_min(queue)
        i += 1
    i = 0
    while i <= k:
        queue.pq_insert(queue, i, i)
        i += 1
    i = 0
    while i <= k/2:
        queue.pq_delete_min(queue)
        i += 1
    end = time.time_ns()

    return (end - start)

def quakeInsertkDeleteHalf(k):
    start = time.time_ns()
    queue = quake_heap()
    i = 0
    while i <= k:
        queue.pq_insert(i, i)
        i += 1
    i = 0
    while i <= k/2:
        queue.pq_delete_min()
        i += 1
    i = 0
    while i <= k:
        queue.pq_insert(i, i)
        i += 1
    i = 0
    while i <= k/2:
        queue.pq_delete_min()
        i += 1
    end = time.time_ns()
    return (end - start)

def brokenDown(reps):
    print("######## Insert 10000 Times #######")
    qqueue_versions = []
    fqueue_versions = []
    qstep1 = []
    fstep1 = []
    for i in range(reps):
        qqueue_versions.append(quake_heap())
        fqueue_versions.append(Fib_Heap())
        #Quake Part
        start = time.time_ns()
        for j in range(10000):
            qqueue_versions[i].pq_insert(j, j)
        end = time.time_ns()
        qstep1.append(start - end)
        #Fib Part
        start = time.time_ns()
        for j in range(10000):
            fqueue_versions[i].pq_insert(fqueue_versions[i], j, j)
        end = time.time_ns()
        fstep1.append(start - end)
    print("Quake Heaps are", sum(qstep1)/len(qstep1) - sum(fstep1)/len(fstep1), "ns slower at this step\n")
                                    #Average

    print("######## Delete-min 5000 Times #######")
    qstep2 = []
    fstep2 = []
    for i in range(reps):
        #Quake Part
        start = time.time_ns()
        for j in range(5000):
            qqueue_versions[i].pq_delete_min()
        end = time.time_ns()
        qstep2.append(start - end)
        #Fib Part
        start = time.time_ns()
        for j in range(5000):
            fqueue_versions[i].pq_delete_min(fqueue_versions[i])
        end = time.time_ns()
        fstep2.append(start - end)
    print("Quake Heaps are", sum(qstep2)/len(qstep2) - sum(fstep2)/len(fstep2), "ns slower at this step\n")

    print("######## Insert 10000 More Times #######")
    qstep3 = []
    fstep3 = []
    for i in range(reps):
        qqueue_versions.append(quake_heap())
        fqueue_versions.append(Fib_Heap())
        start = time.time_ns()
        for j in range(10000):
            qqueue_versions[i].pq_insert(j, j)
        end = time.time_ns()
        qstep3.append(start - end)
        start = time.time_ns()
        for j in range(10000):
            fqueue_versions[i].pq_insert(fqueue_versions[i], j, j)
        end = time.time_ns()
        fstep3.append(start - end)
    print("Quake Heaps are", sum(qstep3)/len(qstep3) - sum(fstep3)/len(fstep3), "ns slower at this step\n")


    print("######## Delete-min 5000 More Times #######")
    qstep4 = []
    fstep4 = []
    for i in range(reps):
        start = time.time_ns()
        for j in range(5000):
            qqueue_versions[i].pq_delete_min()
        end = time.time_ns()
        qstep4.append(start - end)
        start = time.time_ns()
        for j in range(5000):
            fqueue_versions[i].pq_delete_min(fqueue_versions[i])
        end = time.time_ns()
        fstep4.append(start - end)
    print("Quake Heaps are", sum(qstep4)/len(qstep4) - sum(fstep4)/len(fstep4), "ns slower at this step\n")

def main():

    print("################ Broken down test ###############\n") #This lets us see the times of the individual stages
    reps = 5
    brokenDown(reps)
    print("\n################ End of Broken down test ###############\n")

    num_reps = 5
    lower_bound = 10

    print("######## Insert k #######")
    k = lower_bound
    timeQuake = 0
    timeFib = 0
    while k <= 100000:
        for q in range(num_reps):
            timeQuake += quakeInsert(k)
            timeFib += fibInsert(k)
        avgTime = timeQuake/num_reps - timeFib/num_reps
        print("Quake Heaps are", avgTime,"ns slower than Fibonacci on", k,"elements.")
        k *= 10

    print("\n######## Insert k, then delete-min 1 #######")
    k = lower_bound
    timeQuake = 0
    timeFib = 0
    while k <= 100000:
        for q in range(num_reps):
            timeQuake += quakeStraightInsert(k)
            timeFib += fibStraightInsert(k)
        avgTime = timeQuake/num_reps - timeFib/num_reps
        print("Quake Heaps are", avgTime,"ns slower than Fibonacci on", k,"elements.")
        k *= 10

    print("\n######## Insert k then delete-min 80% k #######")

    k = lower_bound
    timeQuake = 0
    timeFib = 0
    while k <= 10000:
        for q in range(num_reps):
            timeQuake += quakeInsertDelete(k)
            timeFib += fibInsertDelete(k)
        avgTime = timeQuake/num_reps - timeFib/num_reps
        print("Quake Heaps are", avgTime,"ns slower than Fibonacci on", k * 10,"total elements.")
        k *= 10


    print("\n######## Insert 10 then delete-min 2, k times #######")

    k = lower_bound
    timeQuake = 0
    timeFib = 0
    while k <= 10000:
        for q in range(num_reps):
            timeQuake += quakeInsert10Delete2(k)
            timeFib += fibInsert10Delete2(k)
        avgTime = timeQuake/num_reps - timeFib/num_reps
        print("Quake Heaps are", avgTime, "ns slower than Fibonacci on", k * 10,"total elements.")
        k *= 10

    print("\n######## Insert 2 then delete-min 1, k times #######")

    k = lower_bound
    timeQuake = 0
    timeFib = 0
    while k <= 10000:
        for q in range(num_reps):
            timeQuake += quakeInsert2Delete1(k)
            timeFib += fibInsert2Delete1(k)
        avgTime = timeQuake/num_reps - timeFib/num_reps
        print("Quake Heaps are", avgTime, "ns slower than Fibonacci on", k * 2,"total elements.")
        k *= 10


    print("\n######## Insert k then delete-min k/2 times, 2 times #######")
    k = lower_bound
    timeQuake = 0
    timeFib = 0
    while k <= 10000:
        for q in range(num_reps):
            timeQuake += quakeInsertkDeleteHalf(k)
            timeFib += fibInsertkDeleteHalf(k)
        avgTime = timeQuake/num_reps - timeFib/num_reps
        print("Quake Heaps are", avgTime,"ns slower than Fibonacci on", k * 10, "total added elements.")
        k *= 10

    k = lower_bound
    timeQuake = 0
    timeFib = 0



"""
def main():
    print("######## Fibonacci #########")
    k = 100
    while k <= 1000000:
        start = time.time_ns()
        queue = Fib_Heap()
        for i in range(k):
            queue.pq_insert(queue, i, i)
        #don't include debugging print statements if you're trying to get an accurate time
        #print(queue.pq_get_size(queue))
        #min = queue.pq_find_min(queue)
        #print(min.key)
        queue.pq_delete_min(queue)
        #min = queue.pq_find_min(queue)
        end = time.time_ns()
        print(k, " elements: ")
        print("Time (in ns) to insert and then delete min: ", (end - start))

        #print(min.key)
        k = k * 10
    print("")

    print("########## Quake ############")
    k = 100
    while k <= 1000000:
        start = time.time_ns()
        queue = quake_heap()
        for i in range(k):
            queue.pq_insert(i, i)
        #don't include debugging print statements if you're trying to get an accurate time
        #print(queue.pq_get_size(queue))
        #min = queue.pq_find_min(queue)
        #print(min.key)
        queue.pq_delete_min()
        #min = queue.pq_find_min(queue)
        end = time.time_ns()
        print(k, " elements: ")
        print("Time (in ns) to insert and then delete min: ", (end- start))
        k *= 10
"""
main()
