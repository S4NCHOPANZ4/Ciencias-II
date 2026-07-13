
def linearSearch(data, x) -> int:
    for i in range(len(data)):
        if data[i] == x: 
            return i
    return -1 
    
def binarySearch(data, x):
    bottom = 0
    top = len(data)-1
    while bottom <= top:
        middle = (top + bottom)//2
        if data[middle] == x:
            return middle
        elif data[middle] < x:
            bottom = middle + 1
        else:
            top = middle-1 
    return -1

hashTable = {}

def hashModFn(key):
    return key % 10

def hashMidSquareFn(key) -> str:
    return str(key**2)[1:-1]

def hashTruncateFn(key):
    #20242020194
    key = str(key)
    return key[3]+key[6]+key[-1]

def insert(key):
    slot = hashModFn(key)
    if slot not in hashTable:
        hashTable[slot] = []
    hashTable[slot].append(key)

def insertItems(data):
    for key_ in data:
        insert(key_)

def search(x):
    slot = hashModFn(x)
    if slot not in hashTable:
        return -1
    for i in hashTable[slot]:
        if i == x:
            return (slot, i)
    return -1


def main():
    data = [1,2,3,4,5]
    # print(hashTruncateFn(20242020194))
    insertItems(data)
    print(search(2))
    print(search(8))
    return 0

main()