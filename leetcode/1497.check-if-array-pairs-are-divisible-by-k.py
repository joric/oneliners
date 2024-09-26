from lc import *

# https://leetcode.com/problems/check-if-array-pairs-are-divisible-by-k/discuss/5421383/One-Line-Solution

class Solution:
    def canArrange(self, a: List[int], k: int) -> bool:
        c = Counter(v%k for v in a)
        for r in c:
            if r and c[r] != c[k - r]:
                return False
        return c[0]%2 == 0

class Solution:
    def canArrange(self, a: List[int], k: int) -> bool:
        return (c:=Counter(v%k for v in a))[0]%2==0 and all(c[r]==c[k-r] for r in c if r)

class Solution:
    def canArrange(self, a: List[int], k: int) -> bool:
        c=Counter(v%k for v in a);return c[0]%2==0 and all(c[r]==c[k-r]for r in c if r)

test('''
1497. Check If Array Pairs Are Divisible by k
Medium

1759

94

Add to List

Share
Given an array of integers arr of even length n and an integer k.

We want to divide the array into exactly n / 2 pairs such that the sum of each pair is divisible by k.

Return true If you can find a way to do that or false otherwise.

 

Example 1:

Input: arr = [1,2,3,4,5,10,6,7,8,9], k = 5
Output: true
Explanation: Pairs are (1,9),(2,8),(3,7),(4,6) and (5,10).
Example 2:

Input: arr = [1,2,3,4,5,6], k = 7
Output: true
Explanation: Pairs are (1,6),(2,5) and(3,4).
Example 3:

Input: arr = [1,2,3,4,5,6], k = 10
Output: false
Explanation: You can try all possible pairs to see that there is no way to divide arr into 3 pairs each with sum divisible by 10.
 

Constraints:

arr.length == n
1 <= n <= 105
n is even.
-109 <= arr[i] <= 109
1 <= k <= 105
Accepted
54,159
Submissions
140,476
''')
