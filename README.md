## leetcode_problems
These are a list of Leetcode problems I have solved in Python (sometimes Java) alongside with solution. Most of these problems are from Neetcode 150.

| #   | Array and Hashing                                                                                                   | Solution | Time | Space | Difficulty | Tag | Note |
| --- | ------------------------------------------------------------------------------------------------------- | -------- | ---- | ----- | ---------- | --- | ---- |
| 217 | [Contains Duplicate](https://leetcode.com/problems/contains-duplicate/description/)                     |[python_solution](./code_solutions/arrays_and_hashing/contains_duplicate.py)|O(N)      |O(N)       | Easy       |     |  Create Set and if set contains current number we're on, then we saw a duplicate, otherwise add it to the set if we seen the first time    |
| 242 | [Valid Anagram](https://leetcode.com/problems/valid-anagram/description/)                               |[python_solution](./code_solutions/arrays_and_hashing/isAnagram.py)          | O(N)     |O(N)       | Easy       |     |  Make char to frequency hashmap and check that both hashmap for both input has same number of frequency (and same characters too)   |
| 1   | [Two Sum](https://leetcode.com/problems/two-sum/description/)                                           | [python_solution](./code_solutions/arrays_and_hashing/two_sum.py)         |O(N)      |O(N)       | Easy       |     | You will make a hashmap of element -> index. Iterate through the list and compute the difference left (target- curr), and check if that is in the keys and if it is return the hashmap value for the difference key along with the index i that we were on for our curr, otherwise just add the current eleemnt and index to the hashmap.      |
| 49  | [Group Anagrams](https://leetcode.com/problems/group-anagrams/description/)                             | [python_solution] (./code_solutions/array_and_hashing/groupAnagram.py)         |      |       | Medium     |     |   create hashmap where key = word sorted, all anagrams will have the same sorted word. this maps to the list of the words that have these same sorted word in common   |

| 347 | [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/description/)           |          |      |       | Medium     |     |      |
| 271 | [Encode and Decode Strings](https://leetcode.com/problems/encode-and-decode-strings/description/)       |          |      |       | Medium     |     |      |
| 238 | [Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/description/) |          |      |       | Medium     |     |      |
| 36  | [Valid Sudoku](https://leetcode.com/problems/valid-sudoku/description/)                                 |          |      |       | Medium     |     |      |
| 128 | [Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/description/) |          |      |       | Medium     |     |      |




| #   | Two Pointer                                                                                                            | Solution | Time | Space | Difficulty | Tag | Note |
| --- | ----------------------------------------------------------------------------------------------------------------- | -------- | ---- | ----- | ---------- | --- | ---- |
| 125 | [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/description/)                                   |          |      |       | Easy       |     |      |
| 167 | [Two Sum II - Input Array Is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/) |          |      |       | Medium     |     |      |
| 15  | [3Sum](https://leetcode.com/problems/3sum/description/)                                                           |          |      |       | Medium     |     |      |
| 11  | [Container With Most Water](https://leetcode.com/problems/container-with-most-water/description/)                 |          |      |       | Medium     |     |      |
| 42  | [Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/description/)                             |          |      |       | Hard       |     |      |


| #   | Sliding Window                                                                                                                                       | Solution | Time | Space | Difficulty | Tag | Note |
| --- | ------------------------------------------------------------------------------------------------------------------------------------------- | -------- | ---- | ----- | ---------- | --- | ---- |
| 121 | [Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/)                               |          |      |       | Easy       |     |      |
| 3   | [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/description/) |          |      |       | Medium     |     |      |
| 424 | [Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/description/)               |          |      |       | Medium     |     |      |
| 567 | [Permutation in String](https://leetcode.com/problems/permutation-in-string/description/)                                                   |          |      |       | Medium     |     |      |
| 76  | [Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/description/)                                             |          |      |       | Hard       |     |      |
| 239 | [Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/description/)                                                 |          |      |       | Hard       |     |      |



| #   | Stack                                                                                                          | Solution | Time | Space | Difficulty | Tag | Note |
| --- | --------------------------------------------------------------------------------------------------------------- | -------- | ---- | ----- | ---------- | --- | ---- |
| 20  | [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/description/)                               |          |      |       | Easy       |     |      |
| 155 | [Min Stack](https://leetcode.com/problems/min-stack/description/)                                               |          |      |       | Medium     |     |      |
| 150 | [Evaluate Reverse Polish Notation](https://leetcode.com/problems/evaluate-reverse-polish-notation/description/) |          |      |       | Medium     |     |      |
| 22  | [Generate Parentheses](https://leetcode.com/problems/generate-parentheses/description/)                         |          |      |       | Medium     |     |      |
| 739 | [Daily Temperatures](https://leetcode.com/problems/daily-temperatures/description/)                             |          |      |       | Medium     |     |      |
| 853 | [Car Fleet](https://leetcode.com/problems/car-fleet/description/)                                               |          |      |       | Medium     |     |      |
| 84  | [Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/description/)     |          |      |       | Hard       |     |      |


| #   | Binary Search                                                                                                                   | Solution | Time | Space | Difficulty | Tag | Note |
| --- | ----------------------------------------------------------------------------------------------------------------------- | -------- | ---- | ----- | ---------- | --- | ---- |
| 704 | [Binary Search](https://leetcode.com/problems/binary-search/description/)                                               |          |      |       | Easy       |     |      |
| 74  | [Search a 2D Matrix](https://leetcode.com/problems/search-a-2d-matrix/description/)                                     |          |      |       | Medium     |     |      |
| 875 | [Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/description/)                                   |          |      |       | Medium     |     |      |
| 153 | [Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/) |          |      |       | Medium     |     |      |
| 33  | [Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/description/)             |          |      |       | Medium     |     |      |
| 981 | [Time Based Key-Value Store](https://leetcode.com/problems/time-based-key-value-store/description/)                     |          |      |       | Medium     |     |      |
| 4   | [Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/description/)                   |          |      |       | Hard       |     |      |



| #  | Linked List                                                                                                           | Solution | Time | Space | Difficulty | Tag | Note |
| -- | --------------------------------------------------------------------------------------------------------------- | -------- | ---- | ----- | ---------- | --- | ---- |
| 35 | [Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/description/)                           |          |      |       | Easy       |     |      |
| 36 | [Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/description/)                     |          |      |       | Easy       |     |      |
| 37 | [Reorder List](https://leetcode.com/problems/reorder-list/description/)                                         |          |      |       | Medium     |     |      |
| 38 | [Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/) |          |      |       | Medium     |     |      |
| 39 | [Copy List with Random Pointer](https://leetcode.com/problems/copy-list-with-random-pointer/description/)       |          |      |       | Medium     |     |      |
| 40 | [Add Two Numbers](https://leetcode.com/problems/add-two-numbers/description/)                                   |          |      |       | Medium     |     |      |
| 41 | [Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/description/)                               |          |      |       | Easy       |     |      |
| 42 | [Find the Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number/description/)               |          |      |       | Medium     |     |      |
| 43 | [LRU Cache](https://leetcode.com/problems/lru-cache/description/)                                               |          |      |       | Hard       |     |      |
| 44 | [Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/description/)                         |          |      |       | Hard       |     |      |
| 45 | [Reverse Nodes in k-Group](https://leetcode.com/problems/reverse-nodes-in-k-group/description/)                 |          |      |       | Hard       |     |      |


| #  | Trees                                                                                                                                                             | Solution | Time | Space | Difficulty | Tag | Note |
| -- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- | ---- | ----- | ---------- | --- | ---- |
| 46 | [Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/description/)                                                                               |          |      |       | Easy       |     |      |
| 47 | [Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/description/)                                                           |          |      |       | Easy       |     |      |
| 48 | [Diameter of Binary Tree](https://leetcode.com/problems/diameter-of-binary-tree/description/)                                                                     |          |      |       | Medium     |     |      |
| 49 | [Balanced Binary Tree](https://leetcode.com/problems/balanced-binary-tree/description/)                                                                           |          |      |       | Easy       |     |      |
| 50 | [Same Tree](https://leetcode.com/problems/same-tree/description/)                                                                                                 |          |      |       | Easy       |     |      |
| 51 | [Subtree of Another Tree](https://leetcode.com/problems/subtree-of-another-tree/description/)                                                                     |          |      |       | Medium     |     |      |
| 52 | [Lowest Common Ancestor of a Binary Search Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/)                       |          |      |       | Medium     |     |      |
| 53 | [Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/description/)                                                 |          |      |       | Medium     |     |      |
| 54 | [Binary Tree Right Side View](https://leetcode.com/problems/binary-tree-right-side-view/description/)                                                             |          |      |       | Medium     |     |      |
| 55 | [Count Good Nodes in Binary Tree](https://leetcode.com/problems/count-good-nodes-in-binary-tree/description/)                                                     |          |      |       | Medium     |     |      |
| 56 | [Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/description/)                                                             |          |      |       | Medium     |     |      |
| 57 | [Kth Smallest Element in a BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/)                                                         |          |      |       | Medium     |     |      |
| 58 | [Construct Binary Tree from Preorder and Inorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/) |          |      |       | Medium     |     |      |
| 59 | [Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/description/)                                                           |          |      |       | Hard       |     |      |
| 60 | [Serialize and Deserialize Binary Tree](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/description/)                                         |          |      |       | Hard       |     |      |


| #  | Tries                                                                                                                               | Solution | Time | Space | Difficulty | Tag | Note |
| -- | ----------------------------------------------------------------------------------------------------------------------------------- | -------- | ---- | ----- | ---------- | --- | ---- |
| 61 | [Implement Trie (Prefix Tree)](https://leetcode.com/problems/implement-trie-prefix-tree/description/)                               |          |      |       | Medium     |     |      |
| 62 | [Design Add and Search Words Data Structure](https://leetcode.com/problems/design-add-and-search-words-data-structure/description/) |          |      |       | Medium     |     |      |
| 63 | [Word Search II](https://leetcode.com/problems/word-search-ii/description/)                                                         |          |      |       | Hard       |     |      |

| #  | Backtracking                                                                                                       | Solution | Time | Space | Difficulty | Tag | Note |
| -- | ------------------------------------------------------------------------------------------------------------- | -------- | ---- | ----- | ---------- | --- | ---- |
| 71 | [Combination Sum](https://leetcode.com/problems/combination-sum/)                                             |          |      |       | Medium     |     |      |
| 72 | [Combination Sum II](https://leetcode.com/problems/combination-sum-ii/)                                       |          |      |       | Medium     |     |      |
| 73 | [Word Search](https://leetcode.com/problems/word-search/)                                                     |          |      |       | Medium     |     |      |
| 74 | [Palindrome Partitioning](https://leetcode.com/problems/palindrome-partitioning/)                             |          |      |       | Medium     |     |      |
| 75 | [Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number/) |          |      |       | Medium     |     |      |
| 76 | [N-Queens](https://leetcode.com/problems/n-queens/)                                                           |          |      |       | Hard       |     |      |
| 77 | [Word Search II](https://leetcode.com/problems/word-search-ii/)                                               |          |      |       | Hard       |     |      |

| #  | Heap/Priority Queue                                                                                           | Solution | Time | Space | Difficulty | Tag | Note |
| -- | ------------------------------------------------------------------------------------------------- | -------- | ---- | ----- | ---------- | --- | ---- |
| 64 | [Last Stone Weight](https://leetcode.com/problems/last-stone-weight/)                             |          |      |       | Easy       |     |      |
| 65 | [K Closest Points to Origin](https://leetcode.com/problems/k-closest-points-to-origin/)           |          |      |       | Medium     |     |      |
| 66 | [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/)                 |          |      |       | Medium     |     |      |
| 67 | [Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/) |          |      |       | Medium     |     |      |
| 68 | [Task Scheduler](https://leetcode.com/problems/task-scheduler/)                                   |          |      |       | Medium     |     |      |
| 69 | [Design Twitter](https://leetcode.com/problems/design-twitter/)                                   |          |      |       | Medium     |     |      |
| 70 | [Find Median from Data Stream](https://leetcode.com/problems/find-median-from-data-stream/)       |          |      |       | Hard       |     |      |

| #   | Graphs                                                                                                                                       | Solution | Time | Space | Difficulty | Tag | Note |
| --- | --------------------------------------------------------------------------------------------------------------------------------------------- | -------- | ---- | ----- | ---------- | --- | ---- |
| 78  | [Clone Graph](https://leetcode.com/problems/clone-graph/)                                                                                     |          |      |       | Medium     |     |      |
| 79  | [Course Schedule](https://leetcode.com/problems/course-schedule/)                                                                             |          |      |       | Medium     |     |      |
| 80  | [Pacific Atlantic Water Flow](https://leetcode.com/problems/pacific-atlantic-water-flow/)                                                     |          |      |       | Medium     |     |      |
| 81  | [Number of Islands](https://leetcode.com/problems/number-of-islands/)                                                                         |          |      |       | Medium     |     |      |
| 82  | [Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/)                                                   |          |      |       | Medium     |     |      |
| 83  | [Alien Dictionary](https://leetcode.com/problems/alien-dictionary/)                                                                           |          |      |       | Hard       |     |      |
| 84  | [Graph Valid Tree](https://leetcode.com/problems/graph-valid-tree/)                                                                           |          |      |       | Medium     |     |      |
| 85  | [Number of Connected Components in an Undirected Graph](https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/) |          |      |       | Medium     |     |      |
| 86  | [Redundant Connection](https://leetcode.com/problems/redundant-connection/)                                                                   |          |      |       | Medium     |     |      |
| 87  | [Course Schedule II](https://leetcode.com/problems/course-schedule-ii/)                                                                       |          |      |       | Medium     |     |      |
| 88  | [Minimum Height Trees](https://leetcode.com/problems/minimum-height-trees/)                                                                   |          |      |       | Medium     |     |      |
| 89  | [Reconstruct Itinerary](https://leetcode.com/problems/reconstruct-itinerary/)                                                                 |          |      |       | Hard       |     |      |
| 90  | [Word Ladder](https://leetcode.com/problems/word-ladder/)                                                                                     |          |      |       | Hard       |     |      |
| 91  | [Word Ladder II](https://leetcode.com/problems/word-ladder-ii/)                                                                               |          |      |       | Hard       |     |      |
| 92  | [Longest Increasing Path in a Matrix](https://leetcode.com/problems/longest-increasing-path-in-a-matrix/)                                     |          |      |       | Hard       |     |      |
| 93  | [Course Schedule III](https://leetcode.com/problems/course-schedule-iii/)                                                                     |          |      |       | Hard       |     |      |
| 94  | [Graph Coloring Problem](https://leetcode.com/problems/graph-coloring/)                                                                       |          |      |       | Hard       |     |      |
| 95  | [Cheapest Flights Within K Stops](https://leetcode.com/problems/cheapest-flights-within-k-stops/)                                             |          |      |       | Medium     |     |      |
| 96  | [Network Delay Time](https://leetcode.com/problems/network-delay-time/)                                                                       |          |      |       | Medium     |     |      |
| 97  | [Swim in Rising Water](https://leetcode.com/problems/swim-in-rising-water/)                                                                   |          |      |       | Hard       |     |      |
| 98  | [The Maze](https://leetcode.com/problems/the-maze/)                                                                                           |          |      |       | Medium     |     |      |
| 99  | [The Maze II](https://leetcode.com/problems/the-maze-ii/)                                                                                     |          |      |       | Medium     |     |      |
| 100 | [The Maze III](https://leetcode.com/problems/the-maze-iii/)                                                                                   |          |      |       | Hard       |     |      |

| #   | 1-Dimension Dynamic Programming                                                                                           | Solution | Time | Space | Difficulty | Tag | Note |
| --- | ------------------------------------------------------------------------------------------------- | -------- | ---- | ----- | ---------- | --- | ---- |
| 101 | [Climbing Stairs](https://leetcode.com/problems/climbing-stairs/)                                 |          |      |       | Easy       |     |      |
| 102 | [Min Cost Climbing Stairs](https://leetcode.com/problems/min-cost-climbing-stairs/)               |          |      |       | Easy       |     |      |
| 103 | [House Robber](https://leetcode.com/problems/house-robber/)                                       |          |      |       | Medium     |     |      |
| 104 | [House Robber II](https://leetcode.com/problems/house-robber-ii/)                                 |          |      |       | Medium     |     |      |
| 105 | [Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/)     |          |      |       | Medium     |     |      |
| 106 | [Palindromic Substrings](https://leetcode.com/problems/palindromic-substrings/)                   |          |      |       | Medium     |     |      |
| 107 | [Decode Ways](https://leetcode.com/problems/decode-ways/)                                         |          |      |       | Medium     |     |      |
| 108 | [Jump Game](https://leetcode.com/problems/jump-game/)                                             |          |      |       | Medium     |     |      |
| 109 | [Jump Game II](https://leetcode.com/problems/jump-game-ii/)                                       |          |      |       | Medium     |     |      |
| 110 | [Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray/)               |          |      |       | Medium     |     |      |
| 111 | [Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)                               |          |      |       | Medium     |     |      |
| 112 | [Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) |          |      |       | Easy       |     |      |


| #   | 2-Dimension Dynamic Programming                                                                                   | Solution | Time | Space | Difficulty | Tag | Note |
| --- | ----------------------------------------------------------------------------------------- | -------- | ---- | ----- | ---------- | --- | ---- |
| 113 | [Unique Paths](https://leetcode.com/problems/unique-paths/)                               |          |      |       | Medium     |     |      |
| 114 | [Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/)   |          |      |       | Medium     |     |      |
| 115 | [Distinct Subsequences](https://leetcode.com/problems/distinct-subsequences/)             |          |      |       | Hard       |     |      |
| 116 | [Coin Change](https://leetcode.com/problems/coin-change/)                                 |          |      |       | Medium     |     |      |
| 117 | [Coin Change II](https://leetcode.com/problems/coin-change-ii/)                           |          |      |       | Medium     |     |      |
| 118 | [0/1 Knapsack (Subset Sum)](https://leetcode.com/problems/partition-equal-subset-sum/)    |          |      |       | Medium     |     |      |
| 119 | [Target Sum](https://leetcode.com/problems/target-sum/)                                   |          |      |       | Medium     |     |      |
| 120 | [Interleaving String](https://leetcode.com/problems/interleaving-string/)                 |          |      |       | Medium     |     |      |
| 121 | [Edit Distance](https://leetcode.com/problems/edit-distance/)                             |          |      |       | Hard       |     |      |
| 122 | [Burst Balloons](https://leetcode.com/problems/burst-balloons/)                           |          |      |       | Hard       |     |      |
| 123 | [WildCard Matching](https://leetcode.com/problems/wildcard-matching/)                     |          |      |       | Hard       |     |      |
| 124 | [Regular Expression Matching](https://leetcode.com/problems/regular-expression-matching/) |          |      |       | Hard       |     |      |

| #   | Bit Manipulation                                                                                                         | Solution | Time | Space | Difficulty | Tag | Note |
| --- | --------------------------------------------------------------------------------------------------------------- | -------- | ---- | ----- | ---------- | --- | ---- |
| 125 | [Single Number](https://leetcode.com/problems/single-number/)                                                   |          |      |       | Easy       |     |      |
| 126 | [Number of 1 Bits](https://leetcode.com/problems/number-of-1-bits/)                                             |          |      |       | Easy       |     |      |
| 127 | [Counting Bits](https://leetcode.com/problems/counting-bits/)                                                   |          |      |       | Easy       |     |      |
| 128 | [Missing Number](https://leetcode.com/problems/missing-number/)                                                 |          |      |       | Easy       |     |      |
| 129 | [Sum of Two Integers](https://leetcode.com/problems/sum-of-two-integers/)                                       |          |      |       | Medium     |     |      |
| 130 | [Reverse Bits](https://leetcode.com/problems/reverse-bits/)                                                     |          |      |       | Easy       |     |      |
| 131 | [Bitwise AND of Numbers Range](https://leetcode.com/problems/bitwise-and-of-numbers-range/)                     |          |      |       | Medium     |     |      |
| 132 | [Maximum XOR of Two Numbers in an Array](https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/) |          |      |       | Hard       |     |      |


| #   | Math/Geometry                                                               | Solution | Time | Space | Difficulty | Tag | Note |
| --- | --------------------------------------------------------------------- | -------- | ---- | ----- | ---------- | --- | ---- |
| 133 | [Rotate Image](https://leetcode.com/problems/rotate-image/)           |          |      |       | Medium     |     |      |
| 134 | [Spiral Matrix](https://leetcode.com/problems/spiral-matrix/)         |          |      |       | Medium     |     |      |
| 135 | [Set Matrix Zeroes](https://leetcode.com/problems/set-matrix-zeroes/) |          |      |       | Medium     |     |      |
| 136 | [Happy Number](https://leetcode.com/problems/happy-number/)           |          |      |       | Easy       |     |      |
| 137 | [Plus One](https://leetcode.com/problems/plus-one/)                   |          |      |       | Easy       |     |      |
| 138 | [Pow(x, n)](https://leetcode.com/problems/powx-n/)                    |          |      |       | Medium     |     |      |
| 139 | [Multiply Strings](https://leetcode.com/problems/multiply-strings/)   |          |      |       | Medium     |     |      |
| 140 | [Detect Squares](https://leetcode.com/problems/detect-squares/)       |          |      |       | Medium     |     |      |


| #   | Greedy                                                                                                       | Solution | Time | Space | Difficulty | Tag | Note |
| --- | ------------------------------------------------------------------------------------------------------------- | -------- | ---- | ----- | ---------- | --- | ---- |
| 141 | [Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)                                           |          |      |       | Medium     |     |      |
| 142 | [Jump Game](https://leetcode.com/problems/jump-game/)                                                         |          |      |       | Medium     |     |      |
| 143 | [Jump Game II](https://leetcode.com/problems/jump-game-ii/)                                                   |          |      |       | Medium     |     |      |
| 144 | [Gas Station](https://leetcode.com/problems/gas-station/)                                                     |          |      |       | Medium     |     |      |
| 145 | [Hand of Straights](https://leetcode.com/problems/hand-of-straights/)                                         |          |      |       | Medium     |     |      |
| 146 | [Merge Triplets to Form Target Triplet](https://leetcode.com/problems/merge-triplets-to-form-target-triplet/) |          |      |       | Medium     |     |      |
| 147 | [Partition Labels](https://leetcode.com/problems/partition-labels/)                                           |          |      |       | Medium     |     |      |
| 148 | [Valid Parenthesis String](https://leetcode.com/problems/valid-parenthesis-string/)                           |          |      |       | Medium     |     |      |


| #   | Intervals                                                                                                         | Solution | Time | Space | Difficulty | Tag | Note |
| --- | --------------------------------------------------------------------------------------------------------------- | -------- | ---- | ----- | ---------- | --- | ---- |
| 149 | [Insert Interval](https://leetcode.com/problems/insert-interval/)                                               |          |      |       | Medium     |     |      |
| 150 | [Merge Intervals](https://leetcode.com/problems/merge-intervals/)                                               |          |      |       | Medium     |     |      |
| 151 | [Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/)                           |          |      |       | Medium     |     |      |
| 152 | [Meeting Rooms](https://leetcode.com/problems/meeting-rooms/)                                                   |          |      |       | Easy       |     |      |
| 153 | [Meeting Rooms II](https://leetcode.com/problems/meeting-rooms-ii/)                                             |          |      |       | Medium     |     |      |
| 154 | [Minimum Interval to Include Each Query](https://leetcode.com/problems/minimum-interval-to-include-each-query/) |          |      |       | Hard       |     |      |
