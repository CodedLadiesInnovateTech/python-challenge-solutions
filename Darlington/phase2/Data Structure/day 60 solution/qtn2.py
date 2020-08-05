#program to create a heapsort, pushing all values onto a heap and 
# then popping off the smallest values one at a time.
import heapq
def heapsort(h):
    heap = []
    for value in h:
        heapq.heappush(heap, value)
    return [heapq.heappop(heap) for i in range(len(heap))]

print(heapsort([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100]))