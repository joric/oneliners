from lc import *

# https://leetcode.com/problems/maximum-fruits-harvested-after-at-most-k-steps/solutions/1624423/10-lines-python-solution/

class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        d = Counter();r = 1;left = Counter();right = Counter()
        for i,j in fruits:  d[i] = j
        ans = d[startPos]
        for i in range(startPos+1,startPos+k+1):
            right[i-startPos] = right[i-1-startPos] + d[i]
        for i in range(startPos - 1,startPos-k-2,-1):
            left[r] = left[r-1] + d[i];r+=1
        for i in range(1,k+1):
            ans = max(ans,max(right[i] + left[k - 2*i],left[i] + right[k - 2*i]) + d[startPos])
        return ans

class Solution:
    def maxTotalFruits(self, f: List[List[int]], s: int, k: int) -> int:
        c=Counter;d,l,x,r,t=c(),c(),c(),1,setitem;
        [t(d,i,j)for i,j in f];
        [t(x,i-s,x[i-1-s]+d[i])for i in range(s+1,s+k+1)];
        [t(l,r,l[r-1]+d[i])or(r:=r+1)for i in range(s-1,s-k-2,-1)];
        return max([d[s]]+[d[s]+max(x[i]+l[k-2*i],l[i]+x[k-2*i])for i in range(1,k+1)])

class Solution:
    def maxTotalFruits(self, f: List[List[int]], s: int, k: int) -> int:
        c=Counter;d,l,x,r,t=c(),c(),c(),1,setitem;[t(d,i,j)for i,j in f];[t(x,i-s,x[i-1-s]+d[i])for i in range(s+1,s+k+1)];[t(l,r,l[r-1]+d[i])or(r:=r+1)for i in range(s-1,s-k-2,-1)];return max([d[s]]+[d[s]+max(x[i]+l[k-2*i],l[i]+x[k-2*i])for i in range(1,k+1)])

test('''
2106. Maximum Fruits Harvested After at Most K Steps
Hard
Topics
premium lock icon
Companies
Hint
Fruits are available at some positions on an infinite x-axis. You are given a 2D integer array fruits where fruits[i] = [positioni, amounti] depicts amounti fruits at the position positioni. fruits is already sorted by positioni in ascending order, and each positioni is unique.

You are also given an integer startPos and an integer k. Initially, you are at the position startPos. From any position, you can either walk to the left or right. It takes one step to move one unit on the x-axis, and you can walk at most k steps in total. For every position you reach, you harvest all the fruits at that position, and the fruits will disappear from that position.

Return the maximum total number of fruits you can harvest.

 

Example 1:


Input: fruits = [[2,8],[6,3],[8,6]], startPos = 5, k = 4
Output: 9
Explanation: 
The optimal way is to:
- Move right to position 6 and harvest 3 fruits
- Move right to position 8 and harvest 6 fruits
You moved 3 steps and harvested 3 + 6 = 9 fruits in total.
Example 2:


Input: fruits = [[0,9],[4,1],[5,7],[6,2],[7,4],[10,9]], startPos = 5, k = 4
Output: 14
Explanation: 
You can move at most k = 4 steps, so you cannot reach position 0 nor 10.
The optimal way is to:
- Harvest the 7 fruits at the starting position 5
- Move left to position 4 and harvest 1 fruit
- Move right to position 6 and harvest 2 fruits
- Move right to position 7 and harvest 4 fruits
You moved 1 + 3 = 4 steps and harvested 7 + 1 + 2 + 4 = 14 fruits in total.
Example 3:


Input: fruits = [[0,3],[6,4],[8,5]], startPos = 3, k = 2
Output: 0
Explanation:
You can move at most k = 2 steps and cannot reach any position with fruits.


Other examples:

Input: fruits = [[200000,10000]], startPos = 200000, k = 0
Output: 10000

Constraints:

1 <= fruits.length <= 105
fruits[i].length == 2
0 <= startPos, positioni <= 2 * 105
positioni-1 < positioni for any i > 0 (0-indexed)
1 <= amounti <= 104
0 <= k <= 2 * 105
Seen this question in a real interview before?
1/5
Yes
No
Accepted
13,370/36.2K
Acceptance Rate
36.9%
Topics
Array
Binary Search
Sliding Window
Prefix Sum
Weekly Contest 271
icon
Companies
Hint 1
Does an optimal path have very few patterns? For example, could a path that goes left, turns and goes right, then turns again and goes left be any better than a path that simply goes left, turns, and goes right?
Hint 2
The optimal path turns at most once. That is, the optimal path is one of these: to go left only; to go right only; to go left, turn and go right; or to go right, turn and go left.
Hint 3
Moving x steps left then k-x steps right gives you a range of positions that you can reach.
Hint 4
Use prefix sums to get the sum of all fruits for each possible range.
Hint 5
Use a similar strategy for all the paths that go right, then turn and go left.
Similar Questions
Maximum Performance of a Team
Hard
''')
