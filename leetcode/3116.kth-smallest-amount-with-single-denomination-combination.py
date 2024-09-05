from lc import *

# Q3. https://leetcode.com/contest/weekly-contest-393
# https://leetcode.com/contest/weekly-contest-393

class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        def test(x):
            count = 0
            for i in range(len(coins)):
                for subset in combinations(coins,i+1):
                    count += (-1)**i * (x // lcm(*subset))
            return count
        return bisect_left(range(1<<62),k,key=test)

class Solution:
    def findKthSmallest(self, c: List[int], k: int) -> int:
        return bisect_left(range(1<<62),k,key=lambda x:sum((-1)**i*(x//lcm(*s))for i in range(len(c))for s in combinations(c,i+1)))

test('''
3116. Kth Smallest Amount With Single Denomination Combination
Hard

21

5

Add to List

Share
You are given an integer array coins representing coins of different denominations and an integer k.

You have an infinite number of coins of each denomination. However, you are not allowed to combine coins of different denominations.

Return the kth smallest amount that can be made using these coins.

 

Example 1:

Input: coins = [3,6,9], k = 3

Output:  9

Explanation: The given coins can make the following amounts:
Coin 3 produces multiples of 3: 3, 6, 9, 12, 15, etc.
Coin 6 produces multiples of 6: 6, 12, 18, 24, etc.
Coin 9 produces multiples of 9: 9, 18, 27, 36, etc.
All of the coins combined produce: 3, 6, 9, 12, 15, etc.

Example 2:

Input: coins = [5,2], k = 7

Output: 12 

Explanation: The given coins can make the following amounts:
Coin 5 produces multiples of 5: 5, 10, 15, 20, etc.
Coin 2 produces multiples of 2: 2, 4, 6, 8, 10, 12, etc.
All of the coins combined produce: 2, 4, 5, 6, 8, 10, 12, 14, 15, etc.

 

Constraints:

1 <= coins.length <= 15
1 <= coins[i] <= 25
1 <= k <= 2 * 109
coins contains pairwise distinct integers.
Accepted
1,217
Submissions
28,006
''')