from collections import deque

queue = deque()
queue.append('Task 1')
queue.append('Task 2')
queue.append('Task 3')
print(queue)

queue.popleft()
print(queue)
queue.appendleft('Task 1')
print(queue)
queue.pop()
print(queue)
queue.append('Task 3')
print(queue)

# set.. hash set

myset = set()

myset.add(2)
myset.add(3)
myset.add(5)

print(myset)
print(len(myset))
print(2 in myset)
print(1 in myset)
myset.remove(2)
print(myset)

# set comprehension
print(set([1, 2, 5, 6, 7, 8]))
sett = set()
sett = {i for i in range(1, 5)}
print(sett)


#hash map
myMap = {}
myMap["apple"] = 10
myMap["banana"] = 20
 
print(myMap)
print(len(myMap))

print("apple" in myMap)
myMap.pop("apple")
print("apple" in myMap)
 
myMap = {"alice": 90, "bob": 45}
print(myMap)

# Dict comprehension...
myMap = {i:i*2 for i in range(3)}
print(myMap)

# looping through a map..
myMap = {"alice":90, "bob": 45}
for key in myMap:
    print(key, myMap[key])

for value in myMap.values():
    print(value)

for key, value in myMap.items():
    print(key, value)    