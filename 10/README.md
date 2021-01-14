# Open Addressing, Cryptographic Hashing

- Open Addressing, Probing Strategies
- Uniform Hashing, Analysis
- Cryptographic Hashing

### Open Addressing

- another approach to collisions
- no chaining; instead all items stored in table.
- one item per slot => m >= n (m: #slots; n: #elements)
- probing
  - hash function specifies order of slots to probe for a key (for insert/search/delete)
  - h: U(U: universe of keys) \* {0,1,...., m-1}(trail count)
  - h(k,1), h(k,2) ....... h(k, m-1) (arbitrary key k to be a permutation of 0, 1,.....m-1)
  - Insert(k,v) : Keep probing until an empty slot is found. Insert item into that slot.
  - Search(k): As long as the slots you encounter by probing are occupied by keys = k,
    keep probing until you either encounter k or find an empty slot—return success or
    failure respectively.
  - replace item with special flag: **_DeleteMe_**, which Insert treats as None but
    Search doesn't

### Probling strategies

- linear probling: h(k, i) = (h'(k) + i ) mod m
- cluster: consecutive group of ocuupied slots which keep longer.

### Double hasing

- h(k, i) = (h1(k) + h2(k)) mod m where h1(k) and h2(k) are two ordinary hash functions.

### Uniform hasing assumption

- not equal to simple uniform hasing
- Each key is equally likely to have any one of the m! permutations as its probe sequence

### Password storage
