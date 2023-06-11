from collections import deque

class PathFinding:
  def __init__(self, game):
    self.game = game  # reference to the game
    self.map = game.map.mini_map  # reference to the game map
    self.ways = [-1, 0], [0, -1], [1, 0], [0, 1], [-1, -1], [1, -1], [1, 1], [-1, 1]  # potential movement directions
    self.graph = {}  # graph representation of the map
    self.get_graph()  # initialize the graph

  def get_path(self, start, goal):
    # find a path from start to goal
    self.visited = self.bfs(start, goal, self.graph)
    path = [goal]
    step = self.visited.get(goal, start)

    while step and step != start:
      path.append(step)
      step = self.visited[step]
    return path[-1]  # return the next step towards the goal

  def bfs(self, start, goal, graph):
    # breadth-first search algorithm
    queue = deque([start])
    visited = {start: None}

    while queue:
      cur_node = queue.popleft()
      if cur_node == goal:
        break
      next_nodes = graph[cur_node]

      for next_node in next_nodes:
        if next_node not in visited and next_node not in self.game.object_handler.npc_positions:
          queue.append(next_node)
          visited[next_node] = cur_node
    return visited

  def get_next_nodes(self, x, y):
    # return valid adjacent nodes
    return [(x + dx, y + dy) for dx, dy in self.ways if (x + dx, y + dy) not in self.game.map.world_map]

  def get_graph(self):
    # create a graph representation of the map
    for y, row in enumerate(self.map):
      for x, col in enumerate(row):
        if not col:
          self.graph[(x, y)] = self.graph.get((x, y), []) + self.get_next_nodes(x, y)
