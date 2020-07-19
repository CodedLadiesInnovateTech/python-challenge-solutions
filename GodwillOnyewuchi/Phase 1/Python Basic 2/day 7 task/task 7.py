import time

currentTime = time.time()
for i in range(10000):
    print(i)
    executionTime = time.time() - currentTime
print(f'ExecutionTime: {executionTime}')