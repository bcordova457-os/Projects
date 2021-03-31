import math, time, os
from multiprocessing import Process, Lock


def squarert(n, lock):
    start = time.time()
    sqrtn = int(math.ceil(math.sqrt(n)))

    for x in range(2, sqrtn + 1):
        if n % x == 0:
            print("%s is not a prime :(" % (n,))
            break
    else:
        print("%s is a prime!!" % (n,))

    end = time.time()
    print("This took %.2f seconds" % (end - start))

    WriteResults(n, end, start, lock)  # pass values to WriteResults function to write to file.


def WriteResults(n, end, start, lock):
    lock.acquire()  # enabling lock access to critical region.

    with open("Version2Results.txt", 'a') as v2Results:
        v2Results.write("Process ID: " + str(os.getpid()) + "\n")
        v2Results.write("N: " + str(n) + "\n")
        v2Results.write("Time: %.2f seconds" % (end - start) + "\n")

    lock.release()


def createThreads(i):
    n = 3517494308439479
    lock = Lock()
    p1 = Process(target=squarert, args=(n, lock))
    p2 = Process(target=squarert, args=(n, lock))
    p1.start()
    p2.start()
    p1.join()
    p2.join()

    print("\n")
    with open("Version2Results.txt", 'a') as file:  # main process prints that round i is complete.
        file.write("\nRound: " + str(i) + " complete.\n\n\n")


if __name__ == "__main__":
    for i in range(5):
        createThreads(i)
        i = i + 1

print("Process complete. See 'Version2Results.txt' for results")
