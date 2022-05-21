from collections import deque

for test in range(1, 11):
    n = int(input())
    d = list(map(int, input().split()))
    queue = deque()
    for i in d:
        queue.append(i)
    i = 0
    while(i != -1):
        for i in range(1, 6):
            queue.append(queue.popleft()-i)
            if queue[-1] <= 0:
                i = -1
                break
    print("#", end='')
    print(test, end=' ')
    for i in range(7):
        print(queue.popleft(), end=' ')
    print(0)
