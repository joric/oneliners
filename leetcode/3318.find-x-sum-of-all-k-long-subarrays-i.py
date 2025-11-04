from lc import *

# https://leetcode.com/problems/find-x-sum-of-all-k-long-subarrays-i/solutions/5949380/one-line-solution-by-mikposp-7mbr/?envType=daily-question&envId=2025-11-04

class Solution:
    def findXSum(self, a: List[int], k: int, x: int) -> List[int]:
        def f(i):
            c = Counter(a[i:i + k])
            t = nlargest(x,c,lambda y:(c[y],y))
            return sum(map(lambda y:y*c[y],t))
        return map(f,range(len(a)+1-k))

class Solution:
    def findXSum(self, a: List[int], k: int, x: int) -> List[int]:
        return[sum(map(prod,nlargest(x,Counter(a[i:i+k]).items(),lambda q:q[::-1])))for i in range(len(a)-k+1)]

test('''
3318. Find X-Sum of All K-Long Subarrays I
Solved
Easy
Topics
premium lock icon
Companies
Hint
You are given an array nums of n integers and two integers k and x.

The x-sum of an array is calculated by the following procedure:

Count the occurrences of all elements in the array.
Keep only the occurrences of the top x most frequent elements. If two elements have the same number of occurrences, the element with the bigger value is considered more frequent.
Calculate the sum of the resulting array.
Note that if an array has less than x distinct elements, its x-sum is the sum of the array.

Return an integer array answer of length n - k + 1 where answer[i] is the x-sum of the subarray nums[i..i + k - 1].

 

Example 1:

Input: nums = [1,1,2,2,3,4,2,3], k = 6, x = 2

Output: [6,10,12]

Explanation:

For subarray [1, 1, 2, 2, 3, 4], only elements 1 and 2 will be kept in the resulting array. Hence, answer[0] = 1 + 1 + 2 + 2.
For subarray [1, 2, 2, 3, 4, 2], only elements 2 and 4 will be kept in the resulting array. Hence, answer[1] = 2 + 2 + 2 + 4. Note that 4 is kept in the array since it is bigger than 3 and 1 which occur the same number of times.
For subarray [2, 2, 3, 4, 2, 3], only elements 2 and 3 are kept in the resulting array. Hence, answer[2] = 2 + 2 + 2 + 3 + 3.
Example 2:

Input: nums = [3,8,7,8,7,5], k = 2, x = 2

Output: [11,15,15,15,12]

Explanation:

Since k == x, answer[i] is equal to the sum of the subarray nums[i..i + k - 1].

 

Constraints:

1 <= n == nums.length <= 50
1 <= nums[i] <= 50
1 <= x <= k <= nums.length
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
36,173/56.5K
Acceptance Rate
64.1%
Topics
Array
Hash Table
Sliding Window
Heap (Priority Queue)
Weekly Contest 419
icon
Companies
Hint 1
Implement the x-sum function. Then, run x-sum on every subarray of nums of size k.
''')
