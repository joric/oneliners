from lc import *

# https://leetcode.com/problems/house-robber-iv/solutions/5188979/one-line-solution/?envType=daily-question&envId=2025-03-15

class Solution:
    def minCapability(self, a: List[int], k: int) -> int:
        def check(cap, q = 0):
            return sum(q := q == 0 and v <= cap for v in a) >= k
        minCap, maxCap = 0, max(a)
        result = maxCap
        while minCap <= maxCap:
            cap = minCap + (maxCap - minCap)//2
            if check(cap):
                result = cap
                maxCap = cap - 1
            else:
                minCap = cap + 1
        return result

class Solution:
    def minCapability(self, a: List[int], k: int) -> int:
        return bisect_right(range(max(a)+1),0,key=lambda c:sum(accumulate(a,lambda q,v:q==0 and v<=c,initial=0))>=k)

class Solution:
    def minCapability(self, a: List[int], k: int) -> int:
        return bisect_right(range(max(a)+1),0,key=lambda c,q=0:sum(q:=q==0 and v<=c for v in a)>=k)

class Solution:
    def minCapability(self, a: List[int], k: int) -> int:
        return bisect_right(range(10**9),0,key=lambda m,t=0:sum(t:=t<1 and m>=x for x in a)>=k)

class Solution:
    def minCapability(self, a: List[int], k: int) -> int:
        return bisect_left(range(10**9),1,key=lambda m,t=0:sum(t:=(1-t)*(m>=x)for x in a)>=k)

test('''
2560. House Robber IV
Medium
Topics
Companies
Hint
There are several consecutive houses along a street, each of which has some money inside. There is also a robber, who wants to steal money from the homes, but he refuses to steal from adjacent homes.

The capability of the robber is the maximum amount of money he steals from one house of all the houses he robbed.

You are given an integer array nums representing how much money is stashed in each house. More formally, the ith house from the left has nums[i] dollars.

You are also given an integer k, representing the minimum number of houses the robber will steal from. It is always possible to steal at least k houses.

Return the minimum capability of the robber out of all the possible ways to steal at least k houses.

 

Example 1:

Input: nums = [2,3,5,9], k = 2
Output: 5
Explanation: 
There are three ways to rob at least 2 houses:
- Rob the houses at indices 0 and 2. Capability is max(nums[0], nums[2]) = 5.
- Rob the houses at indices 0 and 3. Capability is max(nums[0], nums[3]) = 9.
- Rob the houses at indices 1 and 3. Capability is max(nums[1], nums[3]) = 9.
Therefore, we return min(5, 9, 9) = 5.
Example 2:

Input: nums = [2,7,9,3,1], k = 2
Output: 2
Explanation: There are 7 ways to rob the houses. The way which leads to minimum capability is to rob the house at index 0 and 4. Return max(nums[0], nums[4]) = 2.
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 109
1 <= k <= (nums.length + 1)/2
Seen this question in a real interview before?
1/5
Yes
No
Accepted
34.5K
Submissions
67K
Acceptance Rate
51.5%
Topics
Array
Binary Search
Companies
Hint 1
Can we use binary search to find the minimum value of a non-contiguous subsequence of a given size k?
Hint 2
Initialize the search range with the minimum and maximum elements of the input array.
Hint 3
Use a check function to determine if it is possible to select k non-consecutive elements that are less than or equal to the current "guess" value.
Hint 4
Adjust the search range based on the outcome of the check function, until the range converges and the minimum value is found.
Similar Questions
Container With Most Water
Medium
House Robber
Medium
''')
