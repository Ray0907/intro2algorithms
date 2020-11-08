# Algorithmic Thinking, Peak Finding

## Straight forward

- worst case theta(n)

## Divide and Conquer

- if a[n/2] < a[(n/2)-1] then only look at left half 1 to a[n/2] to look for a peek
  else if a[n/2] > a[(n/2)-1] then only look at right half to look for a peak
  else a[n/2] is a peak

1D version worst case theta(logn)
| 1 | 2 | 3 | 4 | 5|....|n/2| (n/2)+1| ...| n-1| n
| :------ | :-------- | :-------- | :------ | :------ | :------ | :------ | :------ | :------ | :------ | :------

---

- 2D version.
  ![image](https://github.com/Ray0907/intro2algorithms/blob/master/static/1/2dversion.png)

- a is a peak iff a >=b, a>=d, a>=c, a>=e
- greedy ascent algorithm

$\theta$(nm)
