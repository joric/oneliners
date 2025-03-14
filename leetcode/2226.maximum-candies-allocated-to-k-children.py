from lc import *

# https://leetcode.com/problems/maximum-candies-allocated-to-k-children/solutions/1908888/java-c-python-binary-search-with-explanation/?envType=daily-question&envId=2025-03-14

class Solution:
    def maximumCandies(self, c: List[int], k: int) -> int:
        left, right = 0, sum(c) / k
        while left < right:
            mid = (left + right + 1) / 2
            if k > sum(a / mid for a in c):
                right = mid - 1
            else:
                left = mid
        return int(left)

# https://leetcode.com/problems/maximum-candies-allocated-to-k-children/solutions/4939846/one-line-python-binary-search/?envType=daily-question&envId=2025-03-14

class Solution:
    def maximumCandies(self, c: List[int], k: int) -> int:
        return bisect_left(range(1,sum(c)//k+1),1,key=lambda m:sum(x//m for x in c)<k)

class Solution:
    def maximumCandies(self, c: List[int], k: int) -> int:
        return bisect_left(range(sum(c)//k),1,key=lambda m:sum(x//-~m for x in c)<k)

test('''
2226. Maximum Candies Allocated to K Children
Medium
Topics
Companies
Hint
You are given a 0-indexed integer array candies. Each element in the array denotes a pile of candies of size candies[i]. You can divide each pile into any number of sub piles, but you cannot merge two piles together.

You are also given an integer k. You should allocate piles of candies to k children such that each child gets the same number of candies. Each child can be allocated candies from only one pile of candies and some piles of candies may go unused.

Return the maximum number of candies each child can get.

 

Example 1:

Input: candies = [5,8,6], k = 3
Output: 5
Explanation: We can divide candies[1] into 2 piles of size 5 and 3, and candies[2] into 2 piles of size 5 and 1. We now have five piles of candies of sizes 5, 5, 3, 5, and 1. We can allocate the 3 piles of size 5 to 3 children. It can be proven that each child cannot receive more than 5 candies.
Example 2:

Input: candies = [2,5], k = 11
Output: 0
Explanation: There are 11 children but only 7 candies in total, so it is impossible to ensure each child receives at least one candy. Thus, each child gets no candy and the answer is 0.
 

Other examples:

Input: candies = [4,7,5], k = 16
Output: 1

Constraints:

1 <= candies.length <= 105
1 <= candies[i] <= 107
1 <= k <= 1012
Seen this question in a real interview before?
1/5
Yes
No
Accepted
72.3K
Submissions
168K
Acceptance Rate
43.0%
Topics
Array
Binary Search
Companies
Hint 1
For a fixed number of candies c, how can you check if each child can get c candies?
Hint 2
Use binary search to find the maximum c as the answer.
Similar Questions
Koko Eating Bananas
Medium
Minimum Limit of Balls in a Bag
Medium
Minimum Speed to Arrive on Time
Medium
Maximum Number of Removable Characters
Medium
Minimized Maximum of Products Distributed to Any Store
Medium
Minimum Time to Complete Trips
Medium
Minimize Maximum of Array
Medium
Maximize Happiness of Selected Children
Medium
''')
