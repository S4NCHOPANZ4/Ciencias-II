# Class 4

- File indexing  
- Performance

## General Concepts

### External Storage Foundations I 

#### File organization 

The physisical and logical arrangement of data records withing a secondary non-colatile storage file, determining how  block are allocated and mapped.

- Hard Disk fragmentation. 


#### Blocks and Records 

- Record: The logical unit of user data collection. 
- Block(page): the minimum phyisical data unit transferred during a single dick input/output hardware operation.

## External Storage Foundations II

### External Search Contraint 

Main memory CPU operations take nanoseconds, while disk seeking takes milliseconds. **Optimization means minimizing Block Reads, not comparasions (Streaming)**.

CPU speed >> Disk Speed 

## File Indexing Architectures

### Indexing 

Am auxiliary data structure containing ordered (Key, Pointer) tuples used to find the exact disk block containing target records without a full sequential file scan.

- **Key**: Logic part asosiated to the file (name)
- **Pointer**: Phisical address


#### Primary Indexes 
Built directly on a file's ordered  primary key field. Tipically sparse, containing  one entry per data block. (1:1 search)


#### Secondary Indexes 
Built on unordered non-primary fields. Dense structure containing an individual entry for every distinct record pointer.


##### Structural property 

Binary searching the sparse Index Table finds the correct clock address instantly, requiring only a single data blovk I/O ferch operation 

#### Multilevel Indexes 

When a file grows too large for RAM, a secondary index is buil t on top id the primary index, creating a search treee strucure (e.g., B+ Trees)
