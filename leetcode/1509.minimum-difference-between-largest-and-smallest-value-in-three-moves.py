from lc import *

# https://leetcode.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves/discuss/730567/JavaC%2B%2BPython-Straight-Forward

class Solution:
    def minDifference(self, a: List[int]) -> int:
        return min(a-b for a,b in zip(nlargest(4,a),nsmallest(4,a)[::-1]))

class Solution:
    def minDifference(self, a: List[int]) -> int:
        return min(map(sub,nlargest(4,a),nsmallest(4,a)[::-1]))

# https://leetcode.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves/discuss/802386/Python-3-lines-well-explained-Greedy-O(nlogn)

class Solution:
    def minDifference(self, a: List[int]) -> int:
        a.sort();return a[4:]and min(a[-3]-a[1],a[-4]-a[0],a[-1]-a[3],a[-2]-a[2])or 0

class Solution:
    def minDifference(self, a: List[int]) -> int:
        a.sort();return min(map(sub,a[-4:],a[:4]))

test('''
1509. Minimum Difference Between Largest and Smallest Value in Three Moves
Medium

1676

184

Add to List

Share
You are given an integer array nums.

In one move, you can choose one element of nums and change it to any value.

Return the minimum difference between the largest and smallest value of nums after performing at most three moves.

 

Example 1:

Input: nums = [5,3,2,4]
Output: 0
Explanation: We can make at most 3 moves.
In the first move, change 2 to 3. nums becomes [5,3,3,4].
In the second move, change 4 to 3. nums becomes [5,3,3,3].
In the third move, change 5 to 3. nums becomes [3,3,3,3].
After performing 3 moves, the difference between the minimum and maximum is 3 - 3 = 0.
Example 2:

Input: nums = [1,5,0,10,14]
Output: 1
Explanation: We can make at most 3 moves.
In the first move, change 5 to 0. nums becomes [1,0,0,10,14].
In the second move, change 10 to 0. nums becomes [1,0,0,0,14].
In the third move, change 14 to 1. nums becomes [1,0,0,0,1].
After performing 3 moves, the difference between the minimum and maximum is 1 - 0 = 1.
It can be shown that there is no way to make the difference 0 in 3 moves.
Example 3:

Input: nums = [3,100,20]
Output: 0
Explanation: We can make at most 3 moves.
In the first move, change 100 to 7. nums becomes [3,7,20].
In the second move, change 20 to 7. nums becomes [3,7,7].
In the third move, change 3 to 7. nums becomes [7,7,7].
After performing 3 moves, the difference between the minimum and maximum is 7 - 7 = 0.
 

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
Accepted
89,012
Submissions
161,635
''')