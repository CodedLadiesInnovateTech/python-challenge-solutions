#program to create a queue and display all the members and size of the queue.
import queue
q = queue.Queue()
for x in range(4):
    q.put(x)
print("Members of the queue:")
y=z=q.qsize()

for n in list(q.queue):
    print(n, end=" ")
print("\nSize of the queue:")
print(q.qsize())