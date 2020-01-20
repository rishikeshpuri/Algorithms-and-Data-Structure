from queue import Queue

def interLeaveQueue(q):
    if (q.qsize() % 2 != 0):
        print("Input even number of integers.")
    s = []
    halfSize = int(q.qsize() / 2)

    for i in range(halfSize):
        s.append(q.queue[0])
        q.get()
    print('1st :',s)
    print()

    while len(s) != 0:
        q.put(s[-1])
        s.pop()
    print('2nd :',q.queue)

    for i in range(halfSize):
        q.put(q.queue[0])
        q.get()
    print()
    print('3rd :',q.queue)

    for i in range(halfSize):
        s.append(q.queue[0])
        q.get()
    print()
    print('4th :', s)
    print('5th :', q.queue)

    while len(s) != 0:
        q.put(s[-1])
        s.pop()
        q.put(q.queue[0])
        q.get()

q = Queue()
q.put(1)
q.put(2)
q.put(3)
q.put(4)
q.put(5)
q.put(6)
q.put(7)
q.put(8)
q.put(9)
q.put(10)
interLeaveQueue(q)
length = q.qsize()
for i in range(length):
    print(q.queue[0], end=' ')
    q.get()
