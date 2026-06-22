## Class #1

- **Data anatomy**
- **Classical Methods**

# Data anatomy

**Record:** data containing multiple fields

**Key:** Unique ID 

**Key Field:** attribute targeted during comparasion, ex: (name, EMAIL, role)

## Internal search:
Executed within RAM, ex: (`int list = []`) running on RAM 

## External Search: 
- Executed across Secondaty Storage (Disk/Files)
- **Scalable** to massive (Non-volatile?) files
- Limited by I/O latency (Transfer time)
- Optimizacion focuses on reducing disk block **READS**

## Main problem:

**RAM <------ I/O Costly Transfers -----> Disk Storage**

## Performance Measures !!!

- **Number of Comparasions:** How many comps had to be done to acomplish an task (better appreciation)
- **Execution time:** Dependency on hardware (Absolute CPU dependent) 
- **Disk Access Operations:** Crucial for external block I/O analysis 

### Asymptotic Analysis (Big-O)

#### Worst case scenario with a dataset of n as **n -> Infinite**

![Theta](../resorurses/images/Theta.png)

- **f(n)** will never go above **C2 g(n)** meaning **O(f(n))**

# Classical Methods 

Classical methods are **foundational** and widely studied.

- Sequential Search (Lineal Search)
- Binary Search 
- Key Transformation Search (**Hashing**???) (Best performance on most scenarios)

## Sequencial Search 

Lineal search from `index 0 to n - 1`, suitable for unsorted datasets.

- **Best case:** O(1)
- **Worts case:** O(n)
- **Avg case:** O(n)

## Binary Search 








