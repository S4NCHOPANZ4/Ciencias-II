hashtable = {}
size = 1

def hash_fn(key: int) -> int:
    return key % size

def insert(key: int) -> int:
    slot = hash_fn(key)
    if slot not in hashtable:
        hashtable[slot] = []
    hashtable[slot].append(key)
    if len(hashtable[slot]) >= 2:
        return key
    return -1

size = int(input(""))
data = input("")
data = list(map(int, data.split()))

def run(data) -> int:
    for i in data:
        if insert(i) != -1:
            return i 
    return -1

print(run(data))
