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






