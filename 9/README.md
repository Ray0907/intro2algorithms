# Table Doubling, Karp-Rabin

## Grow table: m -> m'

- make table of size m'
- build new hash h'
- rehash:
  - for item in T;
    - T'insert(item)

When n reaches m, say

- m + =1?
- ⇒ rebuild every step
- ⇒ n inserts cost Θ(1 + 2 + · · · + n) = Θ(n^2)
- m ∗ =2? m = Θ(n) still (r+ =1)
- ⇒ rebuild at insertion 2i
- ⇒ n inserts cost Θ(1 + 2 + 4 + 8 + · · · + n) where n is really the next power of 2
  = Θ(n)
  • a few inserts cost linear time, but Θ(1) **_on average_**

Amortization

- operation takes T(n) amortized if k operations take <= k \* T(n) time
- think of meaning T(n) on average where the average over all operations.

## Table doubling

- k inserts take O(k) time => O(1) amortized/ insert
- ALSO: K inserts & deletes take O(k)

## String matching

- given two string s & t : does s occur as a substring of t?
- simple algorithm

      - any(s == t[i : i + len(s)] for i in range(len(t) − len(s)))
      — O(|s|) time for each substring comparison
      ⇒ O(|s| · (|t| − |s|)) time
      = O(|s| · |t|) potentially quadratic

## Rolling hash ADT

- r.append(c): add character c to end of x
- r.skip(c): delete first character of x (assuming it is c)
- r maintains a string x
  - r() : hash value of x = h(x)

## Karp-Robin algorithm

- for c in s : rs.append(c)
- for c in t[: len(s)] : rt.append(c)

      if rs() == rt():
      	for i in range(len(s), len(t)):
      		rt.skip(t[i- len(s)])
      		rt.append(t[i])
      		if rs() == rt():
      		check whether s == t[i- len(s)+1:i+1 ]
      	if equal:
      		found match
      	else:
      	happens with probability  <= 1/|s| // O(1) expected time
