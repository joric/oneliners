from lc import *

# https://leetcode.com/problems/maximum-frequency-of-an-element-after-performing-operations-i/solutions/6055684/python-no-sort-9-lines/?envType=daily-question&envId=2025-10-21

class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        freqs = Counter(nums)
        start = min(freqs)
        window_count = sum(freqs[start + i] for i in range(k))
        best = 0
        for num in range(start, max(freqs) + 1):
            window_count += freqs[num + k] - freqs[num - k - 1]
            best = max(best, freqs[num] + min(window_count - freqs[num], numOperations)) 
        return best

class Solution:
    def maxFrequency(self, n: List[int], k: int, o: int) -> int:
        c=Counter(n)
        s=min(c)
        w=sum(c[s+i]for i in range(k))
        return max(c[x]+min((w:=w+c[x+k]-c[x-k-1])-c[x],o)for x in range(s,max(c)+1))

class Solution:
    def maxFrequency(self, n: List[int], k: int, o: int) -> int:
        s=min(c:=Counter(n));w=sum(c[s+i]for i in range(k));return max(c[x]+min((w:=w+c[x+k]-c[x-k-1])-c[x],o)for x in range(s,max(c)+1))

test('''
3346. Maximum Frequency of an Element After Performing Operations I
Solved
Medium
Topics
premium lock icon
Companies
Hint
You are given an integer array nums and two integers k and numOperations.

You must perform an operation numOperations times on nums, where in each operation you:

Select an index i that was not selected in any previous operations.
Add an integer in the range [-k, k] to nums[i].
Return the maximum possible frequency of any element in nums after performing the operations.

 

Example 1:

Input: nums = [1,4,5], k = 1, numOperations = 2

Output: 2

Explanation:

We can achieve a maximum frequency of two by:

Adding 0 to nums[1]. nums becomes [1, 4, 5].
Adding -1 to nums[2]. nums becomes [1, 4, 4].
Example 2:

Input: nums = [5,11,20,20], k = 5, numOperations = 1

Output: 2

Explanation:

We can achieve a maximum frequency of two by:

Adding 0 to nums[1].


Other examples;

Input: nums = [88,53], k = 27, numOperations = 2
Output: 2

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 105
0 <= k <= 105
0 <= numOperations <= nums.length
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
29,366/99.7K
Acceptance Rate
29.5%
Topics
Array
Binary Search
Sliding Window
Sorting
Prefix Sum
Biweekly Contest 143
icon
Companies
Hint 1
Sort the array and try each value in range as a candidate.
Similar Questions
Frequency of the Most Frequent Element
Medium
Count Elements With Maximum Frequency
Easy
''')
