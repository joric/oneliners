from lc import *

# https://leetcode.com/problems/maximum-number-of-integers-to-choose-from-a-range-i/discuss/3157700/Python-NumPy-one-line-brute-force

class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        import numpy as np
        return len(np.where(np.cumsum(np.setdiff1d(np.arange(1,n+1),banned))-maxSum<=0)[0])

# https://leetcode.com/problems/maximum-number-of-integers-to-choose-from-a-range-i/discuss/3146097/Python-Easy-to-Understand-Approach-!!

class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        cnt = 0
        total = 0
        banned = set(banned)
        for i in range(1,n+1):
            if i not in banned and maxSum>=total+i:
                cnt+=1
                total+=i
        return cnt

class Solution:
    def maxCount(self, b: List[int], n: int, m: int) -> int:
        c=t=0;b=set(b);[i not in b and m>=t+i and(c:=c+1,t:=t+i)for i in range(1,n+1)];return c

class Solution:
    def maxCount(self, b: List[int], n: int, m: int) -> int:
        t=0;b=set(b);return sum(i not in b and m>=t+i and(t:=t+i)>0 for i in range(1,n+1))

test('''
2554. Maximum Number of Integers to Choose From a Range I
Medium

346

24

Add to List

Share
You are given an integer array banned and two integers n and maxSum. You are choosing some number of integers following the below rules:

The chosen integers have to be in the range [1, n].
Each integer can be chosen at most once.
The chosen integers should not be in the array banned.
The sum of the chosen integers should not exceed maxSum.
Return the maximum number of integers you can choose following the mentioned rules.

 

Example 1:

Input: banned = [1,6,5], n = 5, maxSum = 6
Output: 2
Explanation: You can choose the integers 2 and 4.
2 and 4 are from the range [1, 5], both did not appear in banned, and their sum is 6, which did not exceed maxSum.
Example 2:

Input: banned = [1,2,3,4,5,6,7], n = 8, maxSum = 1
Output: 0
Explanation: You cannot choose any integer while following the mentioned conditions.
Example 3:

Input: banned = [11], n = 7, maxSum = 50
Output: 7
Explanation: You can choose the integers 1, 2, 3, 4, 5, 6, and 7.
They are from the range [1, 7], all did not appear in banned, and their sum is 28, which did not exceed maxSum.
 

Constraints:

1 <= banned.length <= 104
1 <= banned[i], n <= 104
1 <= maxSum <= 109
Accepted
33,844
Submissions
61,879
''')
