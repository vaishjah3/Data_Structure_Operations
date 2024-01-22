#Implementation of a queue using list
queue=[]
queue.append('a')
queue.append('b')
queue.append('c')
#print(queue)
queue.pop()
queue.pop()
#print(queue)

#Implementation of queue using collections.deque
from collections import deque
q=deque()
q.append('a')
q.append('b')
q.append('c')
#print(q)
q.popleft()
q.popleft()
#print(q)

#Implementation of a queue using python's queue module
from queue import Queue
qu=Queue(maxsize=3)
qu.put('a')
qu.put('b')
qu.put('c')
print(qu.get())
print(qu.get())

