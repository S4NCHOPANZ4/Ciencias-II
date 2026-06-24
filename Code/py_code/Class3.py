# Hashing done in python 

slots = 10

hash_table = []

def init():
    for i in range(slots):
        hash_table.append([]);
def hash_fn_mod(key: int) -> int:
    return key % slots

def hash_fn_midSquare(key: int) -> str:
    remove_ = 1
    temp = str(key**2) 
    return temp[remove_:-remove_]

def hash_fn_truncate(key: int) -> str:
    positions = (3,4,8)
    key_str = str(key)
    slot = ''
    for p in positions:
        slot += key_str[p]
    return slot

def insert(key: int):
    slot = hash_fn_mod(key)
    hash_table[slot].append(key)


#print(hash_fn_midSquare(300))
print(hash_fn_truncate(20242020194))









