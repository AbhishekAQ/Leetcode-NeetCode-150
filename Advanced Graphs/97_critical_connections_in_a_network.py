"""
Critical Connections in a Network

You are given a network of n nodes labeled from 0 to n-1 and a list of connections where connections[i] = [ai, bi] represents a connection between nodes ai and bi. Return all critical connections in the network in any order.
A critical connection is an edge that, if removed, will make some nodes unable to reach each other.

Example:
Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
Output: [[1,3]]

Constraints:
1 <= n <= 10^5
connections.length == n - 1
connections[i].length == 2
0 <= ai, bi <= n - 1
ai != bi
"""
# Solution goes below
