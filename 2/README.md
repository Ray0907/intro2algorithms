# Models of Computation, Document Distance

## What is algorithm?

- computational procedure for solving a problem (input => algo -> output)

## Model of computation specifies

- what operations an algorithm is allowed
- cost (time, space, . . .) of each operation
- cost of algorithm = sum of opeation costs

## Random Access Machine (RAM)

- Random Access Memory(RAM) modeled by a big array
- Θ(1) registers (each 1 word)
- In Θ(1) time, can

  - load word @ ri into register rj
  - compute (+, −, ∗, /, &, |, ˆ) on registers
  - store register rj into memory @ ri

- What’s a word? w ≥ lg (memory size) bits

  - assume basic objects (e.g., int) fit in word
  - unit 4 in the course deals with big numbers

- realistic and powerful -> implement abstractions

## Pointer Machine

- dynamically allocated objects
- object has O(1) fields
- field = word(e.g int) or point to object/null(a.k.a reference)
- weaker than(can be implemented on ) RAM

## Python Model

- **_list_** is actually an array -> RAM L[i] = L[j] +5 -> O(1) time
- object with O(1) **attributes** (ubcluding reference) -> pointer machine x= x.next => O(1) time

- **list**
  - L.append(x) -> O(1) time - obvious if you think of infinite array but how would you have >1 on RAM via table doubling [Lecture 9]
- ![image](https://github.com/Ray0907/intro2algorithms/blob/master/static/2/2_list.png)

- ![image](https://github.com/Ray0907/intro2algorithms/blob/master/static/2/2_list_2.png)

## Document Distance Problem

- The document distance problem has applications in finding similar documents, detecting
  duplicates

- Some definitions:

  - Word = sequence of alphanumeic characters
  - Document = sequence of words(ignore space, punctuation, etc)

- The idea is to define distance in terms of shared words. Think of document D as a vector:
  D[w] = # occurrences of word W. For example:
- ![image](https://github.com/Ray0907/intro2algorithms/blob/master/static/2/2_document_counting.png)

- Document Distance Algorithm
  1.  split each document into words
  2.  count word frequencies (document vectors)
  3.  compute dot produvt( & divide)
