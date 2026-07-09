# Class 11 Unit(?)

## Cut Property 

For any cut (S,V/ S) of the graph, the minimum-weight edge crossing the cut must be in some MST


### Proof Strategy 

- Prim: At each step, minimum-weight edge from tree to non-tree satisfies cut propery Note: better for dense graphs

- Kruskal: Adding minimum-weight  adge that dosen't create cycle respects cut propery for its cut Note: better for sparse graphs

### Corollary 

Both Prim's and Kruskal's algorithms produce optimal solutions If all edge wights are distinct, MTS is unique 

### Algorithm Comparison 

Todo

### Practical Falctors 

- Graph density: Determines dominance of edge vs. vertex operations
- Data Structures: Choice of implementation (array,heap, union-find) affects constants
- Edge weight disritubion: Affects number of comparaions in practice
- Memory access patterns: Cache locality impacts real-world performance


### Advanced techniques 

- Boruvka's algorithm: Parallel-friendlyMST with O(E log V).

- Randomized approaches: Expected linear time under certain conditions. 

- Approximation methods: For every large graphs requiring approximate MTSs.




