# TikTok OA — Tiered Problem Set

Built to match the reported structure: **4 questions, 70 minutes**, Easy → Medium → Medium-hard → Hard.

**No solutions here on purpose.** Write your answer, send it, get it reviewed. Reading solutions feels like progress and isn't.

---

## How to use this

**Work in tier order, but don't finish a tier before starting the next.** Do 2 from Tier 1, then 2 from Tier 2, then come back. Mixing forces *recognition* — deciding which pattern applies — which is the skill the test actually measures.

**Time yourself from the first problem.** Targets:

| Tier | Target time | Why |
|---|---|---|
| Q1 | under 8 min | free points, pure speed |
| Q2 | under 18 min | where you should be strongest |
| Q3 | under 22 min | careful reading beats cleverness |
| Q4 | whatever's left | brute force, take partial credit |

**Before writing any code:** read every example and name the edge case it's testing. Every problem below has at least one example that exists purely as a trap.

---

# TIER 1 — Easy (single loop)

## 1.1 `countDrops`

Given an array `readings`, return the number of positions where a value is **strictly less** than the value immediately before it.

- `readings = [3, 1, 4, 4, 2]` → `2` (1 after 3, and 2 after 4)
- `readings = [1, 2, 3]` → `0`
- `readings = [5, 5, 5]` → `0` (equal is not a drop)
- `readings = [7]` → `0`

*Constraints:* `0 ≤ readings.length ≤ 100000`, `-10^9 ≤ readings[i] ≤ 10^9`

## 1.2 `longestRun`

Given an array `values`, return the length of the longest run of consecutive equal elements.

- `values = [1, 1, 2, 2, 2, 3]` → `3`
- `values = [4, 5, 6]` → `1`
- `values = []` → `0`
- `values = [8, 8]` → `2`

*Constraints:* `0 ≤ values.length ≤ 100000`

## 1.3 `runningTotal`

Given an array `amounts`, return an array where element `i` is the sum of all elements from index 0 through `i`.

- `amounts = [1, 2, 3, 4]` → `[1, 3, 6, 10]`
- `amounts = [5]` → `[5]`
- `amounts = [-2, 5, -3]` → `[-2, 3, 0]`
- `amounts = []` → `[]`

*Constraints:* `0 ≤ amounts.length ≤ 100000`

> This is prefix sums in disguise. Recognizing it here makes Tier 3 easier.

---

# TIER 2 — Medium (hashmap / validation)

## 2.1 `validateDigitWindows` — *the one you screenshotted*

You're given a matrix `numbers` of **3 rows** and `n` columns, digits 1–9. A 3×3 sliding window moves left to right, giving `n - 2` positions.

Return an array of length `n - 2` where element `i` is `true` if window `i` contains every digit from 1 to 9, `false` otherwise.

- `numbers = [[1,2,3,2,5,7],[4,5,6,1,7,6],[7,8,9,4,8,3]]` → `[true, false, true, false]`

*Constraints:* `3 ≤ n ≤ 500`. A solution no worse than O(n³) will pass.

> Nine cells, digits 1–9. If no two are equal, what must the window contain? That observation removes all the counting.

## 2.2 `isValidSudokuBoard`

Given a 9×9 board of characters (digits `'1'`–`'9'` or `'.'` for empty), return `true` if it's valid. Valid means: no repeated digit in any row, any column, or any of the nine 3×3 sub-boxes. Empty cells are ignored, and the board need not be solvable.

- A board with two `5`s in the top row → `false`
- A board with two `8`s in the same 3×3 box → `false`
- A sparse board with no conflicts → `true`

*Constraints:* board is always 9×9.

> The hard part is indexing the 3×3 boxes. `(row // 3, col // 3)` identifies which box a cell belongs to. That trick shows up constantly.

## 2.3 `groupAnagrams`

Given an array of strings `words`, group them so that anagrams are together. Return an array of groups. Groups may be in any order; words within a group may be in any order.

- `words = ["eat","tea","tan","ate","nat","bat"]` → `[["eat","tea","ate"],["tan","nat"],["bat"]]`
- `words = [""]` → `[[""]]`
- `words = ["a"]` → `[["a"]]`

*Constraints:* `1 ≤ words.length ≤ 10000`, lowercase letters.

> The whole problem is choosing a **key** that's identical for anagrams and different for everything else. Two good options; one is O(n·k log k), the other O(n·k).

## 2.4 `firstUniqueOrder`

Given an array `orderIds`, return the **first** value that appears exactly once. If every value repeats, return `-1`.

- `orderIds = [4, 5, 4, 6, 5, 7]` → `6`
- `orderIds = [2, 2, 3, 3]` → `-1`
- `orderIds = [9]` → `9`
- `orderIds = []` → `-1`

*Constraints:* `0 ≤ orderIds.length ≤ 100000`

> "Two-pass with a hashmap" — the exact phrase from the ColorStack thread.

---

# TIER 3 — Medium-hard (simulation with conditions)

The pattern here is never algorithmic difficulty. It's holding several stated rules in your head without dropping one. **Write the rules down as a list before you code.**

## 3.1 `processInventory`

A warehouse processes a list of operations against a stock level starting at `0`. Each operation is a pair `[type, amount]`:

- type `1` — **restock**: add `amount` to stock, but stock can never exceed `capacity`. Any excess is discarded.
- type `2` — **ship**: remove `amount` from stock. If stock is insufficient, ship nothing (the whole operation is skipped) and increment a `failed` counter.
- type `3` — **audit**: if stock is odd, discard one unit.

Return `[finalStock, failed]`.

- `operations = [[1,5],[2,3],[3,0],[2,10]]`, `capacity = 10` → `[1, 1]`
  - restock → 5; ship 3 → 2; audit → 2 is even, unchanged; ship 10 → insufficient, failed = 1
- `operations = [[1,20]]`, `capacity = 8` → `[8, 0]`
- `operations = [[2,1]]`, `capacity = 10` → `[0, 1]`

*Constraints:* `1 ≤ operations.length ≤ 100000`, `1 ≤ capacity ≤ 10^9`

## 3.2 `robotPath`

A robot starts at `(0, 0)` on an infinite grid, facing **north**. It executes a command string:

- `'F'` — move forward one unit in the direction it faces
- `'L'` — turn left 90° (does not move)
- `'R'` — turn right 90° (does not move)
- `'B'` — move backward one unit **without** changing direction

Return the robot's final coordinates as `[x, y]`. North is `+y`, east is `+x`.

- `commands = "FFRF"` → `[1, 2]`
- `commands = "FB"` → `[0, 0]`
- `commands = "LLF"` → `[0, -1]`
- `commands = ""` → `[0, 0]`

*Constraints:* `0 ≤ commands.length ≤ 100000`

> Direction vectors in a list, with an index you rotate: `dirs = [(0,1),(1,0),(0,-1),(-1,0)]`. Turning right is `+1` mod 4, left is `-1` mod 4. Learn this shape — grid simulation problems reuse it endlessly.

## 3.3 `ticketQueue`

`n` people stand in a queue. `tickets[i]` is how many tickets person `i` wants. Each round, the person at the front buys **one** ticket, then goes to the back of the queue — unless they now have all they wanted, in which case they leave.

Return how many rounds pass before the person originally at position `k` finishes and leaves.

- `tickets = [2, 3, 2]`, `k = 2` → `6`
- `tickets = [5, 1, 1, 1]`, `k = 0` → `8`
- `tickets = [1]`, `k = 0` → `1`

*Constraints:* `1 ≤ tickets.length ≤ 100`, `1 ≤ tickets[i] ≤ 100`

> Simulate it literally first. There's a one-pass arithmetic solution, but write the obvious version first — that's the exam habit.

---

# TIER 4 — Hard (dynamic programming)

**Goal here is recognition and partial credit, not mastery.** The tell for DP: *"count the ways," "minimum/maximum cost," "can you reach,"* and each answer depends on smaller versions of the same question.

## 4.1 `minCostClimb`

You're given an array `cost` where `cost[i]` is the price of stepping on stair `i`. You may start at index 0 or index 1, and from any stair you can climb 1 or 2 steps. Return the minimum total cost to move past the last stair.

- `cost = [10, 15, 20]` → `15`
- `cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]` → `6`
- `cost = [5, 5]` → `5`

*Constraints:* `2 ≤ cost.length ≤ 1000`

> Start here. It's the gentlest true DP problem there is. Ask: *what's the cheapest way to reach stair i?* and notice it only depends on stairs `i-1` and `i-2`.

## 4.2 `maxNonAdjacentSum`

Given an array `values` of non-negative integers, return the maximum sum you can collect if you may **not** pick two adjacent elements.

- `values = [1, 2, 3, 1]` → `4` (1 + 3)
- `values = [2, 7, 9, 3, 1]` → `12` (2 + 9 + 1)
- `values = [5]` → `5`
- `values = []` → `0`

*Constraints:* `0 ≤ values.length ≤ 100000`

> At every element you face one choice: take it and skip the next, or skip it. Two running values are enough — you don't need an array.

## 4.3 `countGridPaths`

A robot starts at the top-left of an `m × n` grid and can move only **right** or **down**. Some cells are blocked. Return the number of distinct paths to the bottom-right.

`grid[i][j] == 1` means blocked, `0` means open.

- `grid = [[0,0,0],[0,1,0],[0,0,0]]` → `2`
- `grid = [[0,1],[0,0]]` → `1`
- `grid = [[1]]` → `0` (start is blocked)

*Constraints:* `1 ≤ m, n ≤ 100`

> Paths into a cell = paths from above + paths from the left. Blocked cells contribute zero. This one is worth learning properly — grid DP appears constantly and it's the most approachable hard-tier pattern.

---

## Suggested order

If you only get through eight of these, make it these eight:

1. **1.1** `countDrops` — warm up
2. **2.1** `validateDigitWindows` — your highest-value target
3. **1.2** `longestRun`
4. **2.4** `firstUniqueOrder` — the reported Q2 shape
5. **3.2** `robotPath` — learn the direction-vector idiom
6. **2.2** `isValidSudokuBoard` — the `//3` box trick
7. **3.1** `processInventory` — rule-tracking under pressure
8. **4.1** `minCostClimb` — one honest attempt at DP

Then, if there's time left, do a **full timed mock**: pick one untouched problem from each tier, set 70 minutes, phone out of the room, no pausing.
