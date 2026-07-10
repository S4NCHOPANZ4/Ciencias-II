hashTable = {}
size = 0
max_ = ("",0)

def hashFn(key: str) -> int:
    sum = 0
    for i in key:
        sum += ord(i)
    return sum

def insert(key: str):
    global max_
    slot = hashFn(key)
    if slot not in hashTable:
        hashTable[slot] = (key, 1)
    else:
        hashTable[slot] = (hashTable[slot][0], hashTable[slot][1] + 1)

    if hashTable[slot][1] > max_[1]:
        max_ = hashTable[slot]

n = int(input(""))
v = input("").split()
for i in v:
    insert(i)

print(max_[0], max_[1])