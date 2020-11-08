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

online Latex[https://www.codecogs.com/latex/eqneditor.php]

- a is a peak iff a >=b, a>=d, a>=c, a>=e
- greedy ascent algorithm
- <a href="https://www.codecogs.com/eqnedit.php?latex=\theta(nm)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\theta(nm)" title="\theta(nm)" /></a> theata(n^2) (if m=n)

n cols m rows
n->
mˇ
find max

- O(mlogn)

# Asymptotic notation

- f(10^7) O(1) means theata(1)
- f(20\*n ^7) O(n^7)
- f(log(n^100)) O(log(n)) (Reminds: log(10^3) = 3\* log(10))
- <a href="https://www.codecogs.com/eqnedit.php?latex=log_{\log&space;5}{\(log&space;n)&space;}^{100}&space;->&space;\theta(log(log&space;n))" target="_blank"><img src="https://latex.codecogs.com/gif.latex?log_{\log&space;5}{\(log&space;n)&space;}^{100}&space;->&space;\theta(log(log&space;n))" title="log_{\log 5}{\(log n) }^{100} -> \theta(log(log n))" /></a>

- <a href="https://www.codecogs.com/eqnedit.php?latex=log_{\log&space;5}{\(log&space;(n^{100}))&space;}&space;->&space;log(100log&space;n)->\theta(log(log&space;n))" target="_blank"><img src="https://latex.codecogs.com/gif.latex?log_{\log&space;5}{\(log&space;(n^{100}))&space;}&space;->&space;log(100log&space;n)->\theta(log(log&space;n))" title="log_{\log 5}{\(log (n^{100})) } -> log(100log n)->\theta(log(log n))" /></a>
