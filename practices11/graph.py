# Practice 11. Graph traversals and topological sort (djikstra)
import sys
import heapq
from collections import deque

CONSTRUCT = 'C'
IS_ADJACENT = 'I'
GET_NEIGHBORS = 'N'
TOPOLOGICAL_SORT = 'T'
SHORTEST_PATH = 'S'

class Graph:
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
  
  def topological_sort(self):
    in_degree = [0] * self.num_vertices
    for u in range(self.num_vertices):
      for v, _ in self.adj_list[u]:
        in_degree[v] += 1
    
    queue = deque()
    for u in range(self.num_vertices):
      if in_degree[u] == 0:
        queue.append(u)
    
    result = []
    
    while queue:
      u = queue.popleft()
      result.append(u)
      
      for v, _ in self.adj_list[u]:
        in_degree[v] -= 1
        if in_degree[v] == 0:
          queue.append(v)
    
    if len(result) != self.num_vertices:
      return None
    
    return result
  
  def shortest_path(self, source, target):
    dist = [float('inf')] * self.num_vertices
    dist[source] = 0
    
    prev = [None] * self.num_vertices
    
    pq = [(0, source)]
    
    while pq:
      d, u = heapq.heappop(pq)
      
      if d > dist[u]:
        continue
      
      for v, w in self.adj_list[u]:
        if dist[u] + w < dist[v]:
          dist[v] = dist[u] + w
          prev[v] = u
          heapq.heappush(pq, (dist[v], v))
    
    if dist[target] == float('inf'):
      return None
    
    path = []
    curr = target
    while curr is not None:
      path.append(curr)
      curr = prev[curr]
    
    path.reverse()
    
    return path

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
        result = g.is_adjacent(u, v)
        outFile.write(f"{u} {v} {'T' if result else 'F'}\n")
      elif op == GET_NEIGHBORS:
        if len(words) != 2:
          raise Exception("GET_NEIGHBORS: invalid input")
        u = int(words[1])
        neighbors = g.get_neighbor(u)
        outFile.write(' '.join(map(str, neighbors)) + '\n')
      elif op == TOPOLOGICAL_SORT:
        result = g.topological_sort()
        if result is None:
          outFile.write("The graph has a cycle, topological sort is not possible.\n")
        else:
          outFile.write(' '.join(map(str, result)) + '\n')
      elif op == SHORTEST_PATH:
        if len(words) != 3:
          raise Exception("SHORTEST_PATH: invalid input")
        source, target = int(words[1]), int(words[2])
        path = g.shortest_path(source, target)
        if path is None:
          outFile.write("No path exists.\n")
        else:
          outFile.write(' '.join(map(str, path)) + '\n')
      else:
        raise Exception("Undefined operator")
      i += 1