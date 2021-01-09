# Hashing with Chaining

- Dictionaries & python
- motivation
- prehashing
- hashin
- chaining
- simple uniform hashing
- "Good" hash function

## Dictinonary: Abstract data type (ADT)

    - maintain set of items. each with a key
    	- insert(item): it will overwrite the exist key.
    	- delete(item)
    	- search(key): return item with given key or report doesn't exist.
    - O(lg n) via AVL => O(1)

## Motivation

    - docdist
    - database
    - compilers & interpreters
    - network router
    - network server
    - substring search
    - string commonalities
    - file or directory synchronization
    - cryptography

- simple approach
  - direct-access table: store items in array indexed by key.
  - basness
    1.  keys may not be nonnegetive integers.
    2.  large key range =⇒ large space
  - solution to 1 **_prehash_**
    - maps keys to nonegetive integers.
    - in theory, keys are finite and discrete.(sting of bits.)
    - in python hash(x) is the prehash of x
    - hash('\0B') = hash('\0\0C') = 64
    - ideally: hash(x) = hash(y) <=> x = y
  - solution to 2 **_hashing_**
  - reduce universe u of all keys (integers) down to reasonable size m for table.
  - idea: m ≈ n = # keys stored in dictionary
  - two keys ki
    , kj ∈ K collide if h(ki) = h(kj )
- chaining: Linked list of colliding elements in each slot of table
  - worst case theta(n)
- simple uniform hasing: each key is equally likely to be hashed to any slot of the table, independent of where other keys hasing.

  - analysis: expected length of chain for n keys, m slots => load factor α = n/m = expected # keys per slot = expected length of a chain
  - This implies that expected running time for search is Θ(1+α) — the 1 comes from applying
    the hash function and random access to the slot whereas the α comes from searching the
    list. This is equal to O(1) if α = O(1), i.e., m = Ω(n).

- hash function
  1.  division method: h(k) = k mod m
  2.  multiplication method: h(k) = [(a · k) mod 2w] >> (w − r)
  3.  universal hasing: h(k) = [(a · k + b) mod p] (a: random number between{0, p- 1}, p: prime > |u|)
  - worst case keys k1 != k2: pr{h(k1) = h(k2)} = 1/m
