from lc import *

# https://leetcode.com/problems/hand-of-straights/discuss/135598/C%2B%2BJavaPython-O(MlogM)-Complexity

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        c = Counter(hand)
        for i in sorted(c):
            if c[i] > 0:
                for j in range(groupSize)[::-1]:
                    c[i + j] -= c[i]
                    if c[i + j] < 0:
                        return False
        return True

class Solution:
    def isNStraightHand(self, h: List[int], g: int) -> bool:
        c=Counter(h);return all(0>=c[i]or all(c.update({i+j:-c[i]})or 0<=c[i+j]for j in range(g)[::-1])for i in sorted(c))

class Solution:
    def isNStraightHand(self, h: List[int], g: int) -> bool:
        c=Counter();[c.update({x:1,x+1:-1,x+g:c[x]>=0})for x in sorted(h)];return+c==c

test('''
846. Hand of Straights
Medium

2536

176

Add to List

Share
Alice has some number of cards and she wants to rearrange the cards into groups so that each group is of size groupSize, and consists of groupSize consecutive cards.

Given an integer array hand where hand[i] is the value written on the ith card and an integer groupSize, return true if she can rearrange the cards, or false otherwise.

 

Example 1:

Input: hand = [1,2,3,6,2,3,4,7,8], groupSize = 3
Output: true
Explanation: Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8]
Example 2:

Input: hand = [1,2,3,4,5], groupSize = 4
Output: false
Explanation: Alice's hand can not be rearranged into groups of 4.

 

Constraints:

1 <= hand.length <= 104
0 <= hand[i] <= 109
1 <= groupSize <= hand.length
 

Note: This question is the same as 1296: https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/

Accepted
170,407
Submissions
304,827
''')

