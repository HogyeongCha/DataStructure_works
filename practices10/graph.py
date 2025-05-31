# Practice 10. Graph Representation 
import sys
from collections import deque
CONSTRUCT = 'C'
IS_ADJACENT = 'I'
GET_NEIGHBORS = 'N'
BFS = 'B'
DFS = 'D'
REACHABILITY = 'R'
TOPOLOGICAL_SORT = 'T'
SHORTEST_PATH = 'S'

class Graph:
  # Define a constructor and proper methods
  def __init__(self):
    self.adj_list = None
    self.num_vertices = 0
  
  def construct(self, n, edges):
    self.num_vertices = n
    self.adj_list = [[] for _ in range(n)]

    for u, v, w in edges:
      if u < 0 or u >= n or v < 0 or v >= n:
        raise Exception("Invalid vertex ID")
      self.adj_list[u].append((v, w))
  
  def is_adjacent(self, u, v):
    if u < 0 or u >= self.num_vertices or v < 0 or v >= self.num_vertices:
      raise Exception("Invalid vertex ID")
    for neighbor, _ in self.adj_list[u]:
      if neighbor == v:
        return True
    return False
  
  def get_neighbor(self, u):
    if u < 0 or u >= self.num_vertices:
      raise Exception("Invalid vertex ID")
    return [v for v, _ in self.adj_list[u]]

if __name__ == "__main__":
  if len(sys.argv) != 3:
    raise Exception("Correct usage: [program] [input] [output]")
  
  g = Graph()
  with open(sys.argv[1], 'r') as inFile:
    lines = inFile.readlines()
  with open(sys.argv[2], 'w') as outFile:
    i = 0
    while i < len(lines):
      words = lines[i].split()
      op = words[0]
      if op == CONSTRUCT:
        if len(words) != 3:
          raise Exception("CONSTRUCT: invalid input")
        n, m = int(words[1]), int(words[2])
        cnt, data = m, []
        # Construct a graph
        i += 1
        while cnt > 0 and i < len(lines):
          edge_info = lines[i].split()
          if len(edge_info) != 3:
            raise Exception("CONSTRUCT: invalid edge information")
          u = int(edge_info[0])
          v = int(edge_info[1])
          w = int(edge_info[2])
          data.append((u, v, w))
          cnt -= 1
          i += 1
        if cnt > 0:
          raise Exception("CONSTRUCT: Not enough edge information")
        g.construct(n, data)
        i -= 1
      elif op == IS_ADJACENT:
        if len(words) != 3:
          raise Exception("IS_ADJACENT: invalid input")
        u, v = int(words[1]), int(words[2])
        # Check if edge (u, v) exists in the graph
        result = g.is_adjacent(u, v)
        outFile.write(f"{u} {v} {'T' if result else 'F'}\n")
      elif op == GET_NEIGHBORS:
        if len(words) != 2:
          raise Exception("GET_NEIGHBORS: invalid input")
        u = int(words[1])
        # Get all the neighbors of u
        neighbors = g.get_neighbor(u)
        outFile.write(' '.join(map(str, neighbors)) + '\n')
      else:
        raise Exception("Undefined operator")
      i += 1
