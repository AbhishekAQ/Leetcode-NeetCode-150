"""
Find Eventual Safe States

Given a directed graph, return a list of all the vertices that are eventually safe. A vertex is eventually safe if all possible paths starting from that vertex lead to a terminal vertex (a vertex with no outgoing edges).

Example:
Input: graph = [[1,2],[2,3],[5],[0],[5],[],[]]
Output: [2,4,5,6]

Constraints:
n == graph.length
1 <= n <= 10^4
0 <= graph[i].length <= n
0 <= graph[i][j] <= n - 1
"""
# Solution goes below
