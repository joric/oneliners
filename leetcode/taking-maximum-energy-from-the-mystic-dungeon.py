from lc import *

# Q1. https://leetcode.com/contest/weekly-contest-397
# https://leetcode.com/problems/taking-maximum-energy-from-the-mystic-dungeon

class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        n = len(energy)
        dp = [0] * n
        for i in range(n - 1, -1, -1):
            next_index = i + k
            if next_index >= n:
                dp[i] = energy[i]
            else:
                dp[i] = energy[i] + dp[next_index]
        return max(dp)

# https://leetcode.com/problems/taking-maximum-energy-from-the-mystic-dungeon/discuss/5145723/JavaC%2B%2BPython-DP

class Solution:
    def maximumEnergy(self, e: List[int], k: int) -> int:
        @cache
        def f(i):
            if i >= len(e):
                return 0
            return e[i]+f(i+k)
        return max(map(f,range(len(e))))

class Solution:
    def maximumEnergy(self, e: List[int], k: int) -> int:
        return max(map(f:=cache(lambda i:i<len(e)and e[i]+f(i+k)or 0),range(len(e))))

class Solution:
    def maximumEnergy(self, e: List[int], k: int) -> int:
        for i in range(len(e)-k-1,-1,-1):
            e[i] += e[i+k]
        return max(e)

class Solution:
    def maximumEnergy(self, e: List[int], k: int) -> int:
        [setitem(e,i,e[i]+e[i+k])for i in range(len(e)-k)[::-1]];return max(e)

test('''
3147. Taking Maximum Energy From the Mystic Dungeon
Medium

42

7

Add to List

Share
In a mystic dungeon, n magicians are standing in a line. Each magician has an attribute that gives you energy. Some magicians can give you negative energy, which means taking energy from you.

You have been cursed in such a way that after absorbing energy from magician i, you will be instantly transported to magician (i + k). This process will be repeated until you reach the magician where (i + k) does not exist.

In other words, you will choose a starting point and then teleport with k jumps until you reach the end of the magicians' sequence, absorbing all the energy during the journey.

You are given an array energy and an integer k. Return the maximum possible energy you can gain.

 

Example 1:

Input:  energy = [5,2,-10,-5,1], k = 3

Output: 3

Explanation: We can gain a total energy of 3 by starting from magician 1 absorbing 2 + 1 = 3.

Example 2:

Input: energy = [-2,-3,-1], k = 2

Output: -1

Explanation: We can gain a total energy of -1 by starting from magician 2.

 

Constraints:

1 <= energy.length <= 105
-1000 <= energy[i] <= 1000
1 <= k <= energy.length - 1
 

​​​​​​
Accepted
15,979
Submissions
46,492
''')
