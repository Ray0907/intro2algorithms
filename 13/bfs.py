#!/usr/bin/python3
# -*- coding: utf-8 -*-

from collections import deque

class BFSResult:
	def __init__(self):
		self.level = {}
		self.parent = {}

class Graph:
	def __init__(self):
		self.adj = {}
	def add_edage(self, u, v):
		if self.adj[u] is None:
			self.adj[u] = []
		self.adj[i].append(v)

def bfs(g, s):
	'''
		Queue-based implementation of BFS.
		Args:
			g: a graph with adjacency list adj such that g.adj[u] is a list of u’s
			neighbors.
			s: source.
	'''
	r = BFSResult()
	r.parent = {s: None}
	r.level = {s: 0}

	queue = deque()
	queue.append(s)

	while queue:
		u = queue.popleft()
		for n in g.adj[u]:
			if n not in lever:
				r.parent[n] = u
				r.level[n] = r.level[u] + 1
				queue.append(n)
	return r