# Computational Complexity

- P, EXP, R
- Most problems are uncomputable
- NP
- Hardness & completeness
- Reductions

## definitions

- P = {problems solvable in polynomial (n^c) time}
- EXP = {problems solvable in exponential (2^(n^c)) time}
- • R = {problems solvable in finite time} **_recursive_**

## Examples

- negative-weight cycle detection ∈ P
- n × n Chess ∈ EXP but ∈/ P
- Tetris ∈ EXP but don’t know whether ∈ P

## Halting Problem

- Given a computer program, does it ever halt (stop)?
  - uncomputable (∈/ R): no algorithm solves it (correctly in finite time on all inputs)
  - decision problem: answer is YES or NO

## Most Decision Problems are Uncomputable

- program ≈ binary string ≈ nonneg. integer ∈ N
- decision problem = a function from binary strings (≈ nonneg. integers) to {YES (1),
  NO (0)}
- ≈ infinite sequence of bits ≈ real number ∈ R
  |N|  |R|: no assignment of unique nonneg. integers to real numbers (R uncountable)
- => not nearly enough programs for all problems
- each program solves only one problem
- => almost all problems cannot be solved

## NP

- NP = {Decision problems solvable in polynomial time via a **_lucky_** algorithm}. The **_lucky_**
  algorithm can make lucky guesses, always **_right_** without trying all options.
  - nondeterministic model: algorithm makes guesses & then says YES or NO
  - guesses guaranteed to lead to YES outcome if possible (no otherwise)

## NP-hardness

- is the defining property of a class of problems that are informally "at least as hard as the hardest problems in NP". A simple example of an NP-hard problem is the subset sum problem.

## Example

- Tetris ∈ NP
  - nondeterministic algorithm: guess each move, did I survive?
  - proof of YES: list what moves to make (rules of Tetris are easy)

## P =/= NP

- Big conjecture (worth $1,000,000)
  - ≈ cannot engineer luck
  - ≈ generating (proofs of) solutions can be harder than checking them

## Examples of NP-Complete Problems

- Knapsack (pseudopoly, not poly)
- 3-Partition: given n integers, can you divide them into triples of equal sum?
- Traveling Salesman Problem: shortest path that visits all vertices of a given graph
  — decision version: is minimum weight ≤ x?
- longest common subsequence of k strings
- Minesweeper, Sudoku, and most puzzles
- SAT: given a Boolean formula (and, or, not), is it ever true? x and not x → NO
- shortest paths amidst obstacles in 3D
- 3-coloring a given graph
- find largest clique in a given graph
