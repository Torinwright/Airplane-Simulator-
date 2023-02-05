#!/usr/bin/python3

def display(debug, g):
  # print the adjacency matrix for the graph g and some debug info.
  print('\n'.join([str(r) for r in g]))
  print("size = %d" % len(g))
  print('\n'.join(debug))


def IsKey(g, c):
  # g is an adjacency matrix for a graph. g is an n by n matrix of 1's and 0's.
  # c is an integer from 0 to n-1 representing a vertex in the graph of g.
  # This function returns true if c is a key vertex in the graph of g.
  # A key vertex is a vertex with no edges coming in and n-1 edges going out.
  # A key vertex must have one edge to every other vertex, but no self edges.
  # This function has time complexity O(n) because we just loop once over each
  # row and once over each column.
  for r in range(len(g)):
    if g[r][c]:
      # there is an edge from r to c
      return False
  for c2 in range(len(g)):
    if not g[c][c2]:
      if c != c2:
        # There is no edge from c to c2
        return False
  return True


def IsYucca(g):
  # A digraph is Yucca if it has a key vertex as described above.
  # This function returns true if the graph g is Yucca.
  # g is the adjacency matrix for a digraph.
  #
  # A brute force algorithm would be to check every vertex in the
  # graph to see if it's key. The IsKey() check above is O(n) and
  # there are n vertices in g so the brute force algorithm is O(n^2).
  # That's not the algorithm listed here. This algorithm here is O(n).
  print()
  r = 1
  c = 0
  # r > c is an invariant
  debug = []
  while r < len(g):
    if g[r][c]:
      # Case 1
      # There is an edge in the graph to c so
      # c cannot be a key vertex.
      debug.append("col %d is bad. row %d survived" % (c, r))
      c = r
      r += 1
      # r > c is an invariant
      continue
    # Case 2
    # There is no edge in the graph from r to c so
    # r cannot be a key vertex.
    debug.append("col %d survived. row %d is bad" % (c, r))
    r += 1
    # r > c is an invariant
  display(debug, g)
  print(str((r, c)))
  is_yucca = IsKey(g, c)
  print("Vertex to check = %d. is_yucca = %s." % (c, is_yucca))
  return is_yucca

# Justification:
#
# r > c is an invariant. We can see by induction.
# It's true in the beginning because r = 1 and c = 0.
# If it's true at the start of the while loop then it's maintained in
# each of the 2 cases within the while loop.
#
# We increment r by 1 in every iteration of the while loop.
# This means the while loop terminates within n iterations.
#
# Another invariant is the following:
# if v is a vertex such that v >= 0 and v < r and v != c
# then v is not a key vertex.
# Proof: At the beginning r = 1 and c = 0 so there is no possible v that works and 
# the statement is trivially true.
# Now we assume the statement is true at the start of the while loop.
# We need to show it's still true at the end.
# In case 1 we know that starting value of c cannot be a key vertex so we can reset
# c to the value of r and the invariant is still true at the end.
# In case 2 the starting value of r cannot be a key vertex so 
# the invariant is still true at the end.
# 
# When we are completely done with the while loop r = len(g) so if there
# is a key vertex, it must be c.
# The last step is to check if c is indeed a key vertex in g. If so then the graph
# is YUCCA, otherwise it's not.
# 
# Time Complexity:
#
# In the justification above, we showed that the while loop iterates
# for up to n iterations. So that's O(n).
# The next step is to call IsKey() which is also O(n).
# So the whole function is O(n) Not including the time to print out the 
# adjacency matrix which is O(n^2).

# Test Graphs
def CheckIsYucca(g, expected):
  if IsYucca(g) == expected:
    print("OK")
  else:
    print(80*"x", " ERROR ")


def TestGraphs():
  test_graph_1 = [
    [0, 1, 1, 0, 1],
    [1, 0, 1, 0, 0],
    [0, 1, 0, 0, 1],
    [1, 1, 1, 0, 1],
    [0, 1, 1, 0, 0]]
  CheckIsYucca(test_graph_1, True)
  test_graph_2 = [
    [0, 1, 1, 0],
    [1, 0, 1, 1],
    [0, 0, 0, 0],
    [1, 0, 1, 0]]
  CheckIsYucca(test_graph_2, False)
  test_graph_a = [
    [0, 1, 1, 1, 1, 1],
    [0, 0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0, 0],
    [0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0]]
  CheckIsYucca(test_graph_a, True)
  test_graph_extra_1 = [
    [0, 1, 1, 1, 1, 1, 0],
    [1, 0, 1, 1, 1, 1, 0],
    [1, 1, 0, 1, 1, 1, 0],
    [1, 1, 1, 0, 1, 1, 0],
    [1, 1, 1, 1, 0, 1, 0],
    [1, 1, 1, 1, 1, 0, 0],
    [1, 1, 1, 1, 1, 1, 0]]
  CheckIsYucca(test_graph_extra_1, True)
  test_graph_extra_2 = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 0, 1, 1],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0]]
  CheckIsYucca(test_graph_extra_2, True)
  test_graph_extra_3 = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [1, 1, 0, 1, 0, 1, 1],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0]]
  CheckIsYucca(test_graph_extra_3, False)
  test_graph_extra_4 = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0]]
  CheckIsYucca(test_graph_extra_4, False)
  test_graph_extra_5 = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 0, 1, 1],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0]]
  CheckIsYucca(test_graph_extra_5, False)
  test_graph_extra_6 = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 0, 1, 1],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0]]
  CheckIsYucca(test_graph_extra_6, False)
  test_graph_extra_7 = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0]]
  CheckIsYucca(test_graph_extra_7, False)
  test_graph_extra_8 = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 0, 1, 1],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0]]
  CheckIsYucca(test_graph_extra_8, True)
  test_graph = [[0]]
  CheckIsYucca(test_graph, True)
  test_graph = [[1,0],
                [0,1]]
  CheckIsYucca(test_graph, False)
  test_graph = [[0,0],
                [1,0]]
  CheckIsYucca(test_graph, True)


if __name__ == "__main__":
  TestGraphs()

