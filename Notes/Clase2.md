# Class 2

- Hashing

## Hashing Fundamentals

### Concept of hashing (Dispersion) I 

A mapping technique that converts an arbitrary search key into a valid integer index within a fixed-size array mapping (data representation) target.

"It does not matter what dataset you are working with, find a way to convert it into an integer"

### Direct addresing  vs Hash Tables (networks)

- **Direct Addressing**: Ideal case where each key maps is assigned to an exact memory slot. (Get to the result within one unique question) (Constant growth).  

- **Hash Table**: Maps massive key domains to a compressed table capacity (m), where m << abs(U).

### Concept of Disperion II

#### Load factor(alpha)

$alpha = n/m$ (number of stores keys / Total table size)

alpha ->  1, the probability of index mapping collisions escalates exponentially. (The closer to one we get closer to direct addresing).

Note: Keys are the elements to store, key fields are the result of our data represention (mapping) 
table size can be defined by mod(10)

## Hash Functions

###  Classical Hash Fucntions I

**mod 10**

Uses the algebraic remainder of integrer division.

h(key) = key (mod m)

*Recommendation*:
Table size m should be a prime number not close to powers of 2.

***Note***:
- $mod 10:\quad 0 - 1 - 2 - 3 - ... - 9$
- $mod 2:\quad 0 - 1$
- $mod m: \quad m \, slots$

### Classical Hash Fucntions II

**Mid-square method** 

squares the key and extracts the specified central digits 

Example:

key = 45 $\to$ 45*45 = 2025 $\to$ Exract middle digits (02)


###  Classical Hash Fucntions III

**Truncation Method**

Extracts and concentrates abitrary digits from pre-selected key positions while discarding others.

###  Classical Hash Fucntions IV

**Base Convertion**

Interprets the original ke in base p, then converts it to base q to isolate stabl indexes.

#### Examples:

- Dec $\to$ Hex
- Char $\to$ ASCII


## Collisions

**Definition** 

Occurs when two or more distinct keys generate the exact sam hash index output.

h(k1) = h(k2) where k1 != k2

**Note**: By the Pigeonhole Principle we must create a hash fn that provides one element on each slot, avoiding all colisions is impossible. (permutation and combination)

## Collision Handling: Open Addresing 

### Reassignment Theory

All elements are stored directly inside the array table. If a collision occurs we probe alternative slots sequentially until an empty cell is found.


#### Probing Strategies 

- **Linear Probing**: h(k,i) = (h'(k) + i) (mod m)
- **Quadratic Probing**: h(k,i) = (h'(k) + c1 i + c2 i*i) (mod m)

### Nested Arrays (Buckets)

Each slot in the main tablepoints to an array profile slot that can hold a fixed nimber to multiple items.  

### Sequential Chaining 

Each slot in the main table functions as a head pointer to a Singly Linked list.

## Analysis

**Access Complexity**

- **Average Case**: O(1) assuming even, uniform distribution of key entries.
- **Worst Case**: O(n) access operations, if all inserted keys collide into the exact same index link sequence.

Note: to keep Design focus performant, monitor table density profiles. Rehash the entire table into a larger footprint when alpha > 0.75
