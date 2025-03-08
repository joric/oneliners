from lc import *

# https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/solutions/2460524/python-sliding-window-6-lines/?envType=daily-question&envId=2025-03-08

class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        max_black = black_count = blocks[:k-1].count('B')
        for i in range(k-1, len(blocks)):
            black_count += blocks[i] == 'B'
            max_black = max(max_black, black_count)
            black_count -= blocks[i - k + 1] == 'B'
        return k - max_black

# https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/solutions/2460759/python-1-liner/?envType=daily-question&envId=2025-03-08

class Solution:
    def minimumRecolors(self, b: str, k: int) -> int:
        return min((b[i:i+k].count('W')for i in range(len(b)-k+1)),default=1)

class Solution:
    def minimumRecolors(self, b: str, k: int) -> int:
        return min([b[i:i+k].count('W')for i in range(len(b)-k+1)]or[1])

test('''
2379. Minimum Recolors to Get K Consecutive Black Blocks
Easy
Topics
Companies
Hint
You are given a 0-indexed string blocks of length n, where blocks[i] is either 'W' or 'B', representing the color of the ith block. The characters 'W' and 'B' denote the colors white and black, respectively.

You are also given an integer k, which is the desired number of consecutive black blocks.

In one operation, you can recolor a white block such that it becomes a black block.

Return the minimum number of operations needed such that there is at least one occurrence of k consecutive black blocks.

 

Example 1:

Input: blocks = "WBBWWBBWBW", k = 7
Output: 3
Explanation:
One way to achieve 7 consecutive black blocks is to recolor the 0th, 3rd, and 4th blocks
so that blocks = "BBBBBBBWBW". 
It can be shown that there is no way to achieve 7 consecutive black blocks in less than 3 operations.
Therefore, we return 3.
Example 2:

Input: blocks = "WBWBBBW", k = 2
Output: 0
Explanation:
No changes need to be made, since 2 consecutive black blocks already exist.
Therefore, we return 0.
 

Constraints:

n == blocks.length
1 <= n <= 100
blocks[i] is either 'W' or 'B'.
1 <= k <= n
Seen this question in a real interview before?
1/5
Yes
No
Accepted
67.5K
Submissions
111.9K
Acceptance Rate
60.3%
Topics
String
Sliding Window
Companies
Hint 1
Iterate through all possible consecutive substrings of k characters.
Hint 2
Find the number of changes for each substring to make all blocks black, and return the minimum of these.
Similar Questions
Max Consecutive Ones III
Medium
Maximum Points You Can Obtain from Cards
Medium
Maximum Number of Vowels in a Substring of Given Length
Medium
''')
