hashTable = {}
different = 0
size = 0
def hash_fn_mod(key: int) -> int:
    return key % size

def insert(key: int):
    global different
    slot = hash_fn_mod(key)
    if search(key) == -1:
        different+=1
        if slot not in hashTable:
            hashTable[slot] = []
        hashTable[slot].append(key)

def search(key: int) -> int:
    slot = hash_fn_mod(key)
    if slot not in hashTable:
        return -1
    if key not in hashTable[slot]:
        return -1
    return slot

size = int(input())
for i in range(size):
    n = int(input(""))
    insert(n)

print(different)