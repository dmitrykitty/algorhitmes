import heapq

data = [10, 20, 43, 1, 2, 65, 17, 44, 2, 3, 1]
data2 = data[:]

heapq.heapify(data)

print(data)

#i
# l = 2 * i + 1
# r = 2 * i + 2

heapq.heappop(data)
print(data)



