# Pattern recognition

How to get from a problem statement to the right approach without guessing.

The order matters. Constraints first, shape second, pattern third. Most people jump straight to
"what pattern is this" and get it wrong, because the same-looking problem takes a different
approach at n = 100 and n = 100,000.

---

## The procedure

1. **Read the constraints before the examples.** They tell you the complexity you are allowed,
   which eliminates most patterns immediately.
2. **Name the shape.** Sorted? Contiguous? All combinations? A graph in disguise? One sentence.
3. **List the two or three patterns that fit both.** Not one. If only one comes to mind you have
   probably stopped thinking too early.
4. **Pick one and state the invariant** before writing code. "Left pointer is always the smallest
   unprocessed index" or "dp[i] is the max sum ending at i". If you cannot state it, you do not
   understand the approach yet.
5. **Write it. Then check the complexity against step 1.** If it does not fit, you picked wrong.

---

## Step 1: constraints to complexity budget

Work backwards from n. Assume roughly 10^7 operations per second in Python, not 10^8. Python is
slow enough that this matters and it is the reason a solution that passes in C++ times out for you.

| Constraint | Budget | What is reachable |
|---|---|---|
| n ≤ 10 | O(n!) | Permutations. Full brute force backtracking. |
| n ≤ 20 | O(2^n) | Subsets, bitmask DP. The exponent being 20 is a deliberate signal. |
| n ≤ 100 | O(n³) | Triple nested loop, interval DP, Floyd-Warshall. |
| n ≤ 500 | O(n³) tight, O(n²) safe | Interval DP, matrix work. |
| n ≤ 2,000 | O(n²) | 2-D DP, all pairs, expand-around-centre. |
| n ≤ 10^4 | O(n²) borderline in Python | Prefer O(n log n) if you can. |
| n ≤ 10^5 | O(n log n) | Sort, heap, binary search, ordered structures. |
| n ≤ 10^6 | O(n) | Two pointers, sliding window, prefix sum, hashmap, counting. |
| n ≤ 10^9 | O(log n) or O(1) | Binary search **on the answer**, maths, bit tricks. You cannot even build the input. |
| No n, but values ≤ 10^9 | Look at count, not value | The value range is a red herring, or a hint toward binary search on answer. |

Two constraint tells that are almost always deliberate:

- **A small alphabet.** "Lowercase English letters only" means an array of 26 counts, and it means
  a sliding window comparison is O(26) not O(k), which is how it becomes O(n).
- **A value range much smaller than n.** "1 ≤ nums[i] ≤ n" means the values can index the array.
  That is the tell for cyclic sort, or for marking by negation to get O(1) space.

---

## Step 2: shape to candidate patterns

| The problem says | Candidates |
|---|---|
| Array is **sorted** | Two pointers, binary search |
| Find a **pair/triplet summing to target** | Sorted → two pointers. Unsorted → hashmap. |
| **Contiguous** subarray or substring, optimise something | Sliding window |
| Contiguous, but with **many range queries** | Prefix sum |
| **k-th** largest, smallest, closest | Heap of size k, or quickselect |
| **Top k** frequent | Heap, or bucket sort for O(n) |
| **All** subsets, combinations, permutations, partitions | Backtracking |
| **Count the ways**, or min/max over a sequence of choices | DP |
| Can I **reach** / is it possible | DP, greedy, or BFS. Try greedy first, then find the counterexample. |
| **Shortest** path, unweighted | BFS |
| Shortest path, **weighted, non-negative** | Dijkstra |
| Shortest path, **negative weights** | Bellman-Ford |
| **All pairs** shortest path, n ≤ 400 | Floyd-Warshall |
| **Ordering with dependencies**, prerequisites | Topological sort |
| **Cycle** in a directed graph | DFS three-colour, or Kahn's |
| **Cycle** in an undirected graph | Union-find, or DFS tracking parent |
| **Connected components**, merging groups | Union-find, or DFS/BFS flood fill |
| **Next greater** or next smaller element | Monotonic stack |
| Brackets, undo, nesting | Stack |
| **Prefix** search, autocomplete, word dictionary | Trie |
| **Overlapping ranges**, meetings, merging | Sort intervals, usually by start |
| Linked list **middle** or **cycle** | Fast and slow pointers |
| Tree **path** or depth | DFS recursion |
| Tree **level by level** | BFS with a queue |
| It is a **BST** | Inorder traversal gives sorted order. Use it. |
| **O(1) extra space** demanded on an array | Index as hashmap, or mark by negation, or cyclic sort |
| Pairs cancel out, find the odd one | XOR |
| **Minimise the maximum**, or maximise the minimum | Binary search on the answer |

---

## The patterns, with their tells

### Two pointers
**Tell:** sorted array, and you need a pair or triplet.
**Invariant:** everything outside `[left, right]` has been ruled out and can never be the answer.
Moving a pointer must be provably safe. If you cannot argue why skipping a candidate is safe, this
is not the right pattern.

### Sliding window
**Tell:** contiguous, and "longest" or "shortest" or "at most k".
**Invariant:** the window `[left, right]` is always valid, or you are shrinking until it is.
Fixed size and variable size are different problems, decide which before you write.

### Binary search
**Tell:** sorted, or the answer space is monotonic even when the input is not.
The second one is the harder and more valuable case: "minimum capacity such that it fits in d days".
You are searching over answers, and `check(x)` is a separate function. Write `check` first.

### Prefix sum
**Tell:** repeated range sums, or "subarray summing to k".
With a hashmap of prefix counts this turns an O(n²) scan into O(n). The trick is storing
`prefix - k` lookups, not the prefixes themselves.

### Hashmap counting
**Tell:** anagrams, frequencies, "have I seen this before".
Usually the O(n) escape from an O(n²) brute force. Cheap and underused.

### Monotonic stack
**Tell:** "next greater", "previous smaller", largest rectangle, temperatures.
**Invariant:** the stack is increasing or decreasing at all times. When you pop, the element you
popped has just found its answer. Each element pushed once and popped once, hence O(n).

### Heap
**Tell:** k-th anything, merge k lists, running median, scheduling by priority.
Size-k heap gives O(n log k). For a running median you need two heaps facing each other.

### Backtracking
**Tell:** enumerate everything. Subsets, permutations, combinations, n-queens, sudoku.
Template is always: choose, recurse, un-choose. The interesting part is the pruning, not the
recursion. For duplicates, sort first and skip equal siblings.

### DP
**Tell:** overlapping subproblems and optimal substructure. Practically: "count the ways",
"minimum cost", "longest something".
Define `dp[i]` in one English sentence before writing anything. If the sentence is vague the
recurrence will be wrong. Do it top-down with memoisation first if bottom-up is not obvious.

### Graphs, BFS and DFS
**Tell:** grid, network, dependencies, "connected", "reachable".
Grids are graphs. BFS for shortest in unweighted, DFS for existence and for path enumeration.
Always ask: directed or undirected, weighted or not, cycles possible.

### Union-find
**Tell:** merging sets, counting components, detecting a cycle in an undirected graph.
With path compression and union by rank it is effectively O(1) per operation. Worth memorising the
20-line implementation cold.

### Trie
**Tell:** the word "prefix", or repeated lookups over a dictionary of words.
Word Search II is a trie problem wearing a backtracking costume.

### Intervals
**Tell:** meetings, ranges, merging, overlapping.
Almost always: sort by start, then sweep. Sort by end when you are maximising the count of
non-overlapping items, which is the greedy one.

### Fast and slow pointers
**Tell:** linked list cycle, middle node, or an array where values point to indices.
Find the Duplicate Number is this pattern disguised as an array problem.

### Bit manipulation
**Tell:** pairs cancel, "appears once", constraints mentioning powers of two, or O(1) space with a
small fixed universe.
`x & (x-1)` clears the lowest set bit. `x ^ x = 0`. Those two carry most of the problems.

---

## Traps

**Greedy that looks right.** Before committing to greedy, spend one minute actively trying to break
it with a counterexample. If you cannot break it in a minute, go ahead. Most wrong answers on
Medium problems are greedy where DP was needed.

**Sorting when you did not need to.** Sorting costs O(n log n) and sometimes destroys the index
information the problem wanted. Check whether a hashmap gets you O(n) first.

**Recursion depth.** Python's default limit is 1000. A DFS on a 10^5-node graph will blow the
stack. Convert to iterative with an explicit stack, or raise the limit and say so.

**Modifying a list while iterating it.** Silent wrong answers, no exception.

**Off-by-one in binary search.** Pick one template, `while left < right` with `right = mid` and
`left = mid + 1`, and use only that one. Consistency beats cleverness here.

**Answering the wrong question.** Return the length or return the subarray? The index or the value?
Read the return line of the examples again before you submit.

---

## Writing the footer

After solving, the footer block in each file takes thirty seconds and is the entire reason the repo
exists:

    # pattern:         the name from this file
    # time:            with a one-word reason, "sort dominates"
    # space:           excluding output
    # what I got wrong: the actual thing, in your own words

The last line is the one that matters. "Forgot the duplicate skip in the sorted loop" is useful.
"Was confused" is not. On review days you read these, never the code.
