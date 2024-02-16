from lc import *

# https://leetcode.com/problems/least-number-of-unique-integers-after-k-removals

class Solution:
    def findLeastNumOfUniqueInts(self, a: List[int], k: int) -> int:
        return sum(0>(k:=k-c)for c in sorted(Counter(a).values()))

test('''
1481. Least Number of Unique Integers after K Removals
Medium

1636

167

Add to List

Share
Given an array of integers arr and an integer k. Find the least number of unique integers after removing exactly k elements.

 

Example 1:

Input: arr = [5,5,4], k = 1
Output: 1
Explanation: Remove the single 4, only 5 is left.
Example 2:
Input: arr = [4,3,1,1,3,3,2], k = 3
Output: 2
Explanation: Remove 4, 2 and either one of the two 1s or three 3s. 1 and 3 will be left.
 

Constraints:

1 <= arr.length <= 10^5
1 <= arr[i] <= 10^9
0 <= k <= arr.length
Accepted
135,830
Submissions
231,752
''')
