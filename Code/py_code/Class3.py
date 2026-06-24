# Hashing done in python 

slots: int = 10

hash_table = {}

# no necesario inicializar trabajando con diccionarios(???)
# def init():
#     for i in range(slots):
#         hash_table.append([]);

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
 
    # Diccionario
    slot = hash_fn_mod(key)
    if slot not in hash_table: 
        hash_table[slot] = []
    hash_table[slot].append(key)

    # if slot not in hash_table: 
    #     hash_table.append(slot)
    # for i, slot_i in enumerate(hash_table):
    #     if slot == slot_i:
    #         hash_table[i].append(key)
    #         break

def search(key: int) -> int:
    slot = hash_fn_mod(key)
    value = -1
    for i, key_i in enumerate(hash_table[slot]):
        if key_i == key:
            value = slot, i
    return value
    # if key in hash_table[slot]:
    #     return slot
    # else:
    #     return -1


#print(hash_fn_midSquare(300))
print(hash_fn_truncate(20242020194))









