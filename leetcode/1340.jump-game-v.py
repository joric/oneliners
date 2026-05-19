from lc import *

# https://leetcode.com/problems/jump-game-v/solutions/496547/python-3-check-every-index-and-cache-int-0icp/


class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)
        @cache
        def f(i):
            m = 1
            for j in range(1, d+1):
                if i + j < n:
                    if arr[i+j] < arr[i]:
                        m = max(m, 1 + f(i+j))
                    else:
                        break

            for j in range(1, d+1):
                if i - j >= 0:
                    if arr[i-j] < arr[i]:
                        m = max(m, 1 + f(i-j))
                    else:
                        break
            return m
        return max(map(f,range(n)))

class Solution:
    def maxJumps(self, a: List[int], d: int) -> int:
        n=len(a);return max(map(f:=cache(lambda i:1+max([f(j)for r in(range(i+1,min(n,i-~d)),range(i-1,max(-1,i+~d),-1))for j in takewhile(lambda j:a[j]<a[i],r)]+[0])),range(n)))

test('''
1340. Jump Game V
Solved
Hard
Topics
premium lock icon
Companies
Hint
Given an array of integers arr and an integer d. In one step you can jump from index i to index:

i + x where: i + x < arr.length and  0 < x <= d.
i - x where: i - x >= 0 and  0 < x <= d.
In addition, you can only jump from index i to index j if arr[i] > arr[j] and arr[i] > arr[k] for all indices k between i and j (More formally min(i, j) < k < max(i, j)).

You can choose any index of the array and start jumping. Return the maximum number of indices you can visit.

Notice that you can not jump outside of the array at any time.

 

Example 1:


Input: arr = [6,4,14,6,8,13,9,7,10,6,12], d = 2
Output: 4
Explanation: You can start at index 10. You can jump 10 --> 8 --> 6 --> 7 as shown.
Note that if you start at index 6 you can only jump to index 7. You cannot jump to index 5 because 13 > 9. You cannot jump to index 4 because index 5 is between index 4 and 6 and 13 > 9.
Similarly You cannot jump from index 3 to index 2 or index 1.
Example 2:

Input: arr = [3,3,3,3,3], d = 3
Output: 1
Explanation: You can start at any index. You always cannot jump to any index.
Example 3:

Input: arr = [7,6,5,4,3,2,1], d = 1
Output: 7
Explanation: Start at index 0. You can visit all the indicies. 
 

Constraints:

1 <= arr.length <= 1000
1 <= arr[i] <= 105
1 <= d <= arr.length
 
Seen this question in a real interview before?
1/6
Yes
No
Accepted
43,559/66.9K
Acceptance Rate
65.1%
Topics
Senior Staff
Array
Dynamic Programming
Sorting
Weekly Contest 174
icon
Companies
Hint 1
Use dynamic programming. dp[i] is max jumps you can do starting from index i. Answer is max(dp[i]).
Hint 2
dp[i] = 1 + max (dp[j]) where j is all indices you can reach from i.
Similar Questions
Jump Game VII
Medium
Jump Game VIII
Medium
''')
