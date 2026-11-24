from lc import *

# https://leetcode.com/problems/smallest-unique-subarray/solutions/8253603/javacpython-rolling-hash-binary-search-b-gzhm/?envType=daily-question&envId=2026-11-25

class Solution:
    def smallestUniqueSubarray(self, a: List[int]) -> int:
        res = n = len(a)
        b = 215215
        mod = (1 << 31) - 1
        l, r = 1, n
        while l < r:
            k = (l + r) // 2
            h, p = 0, 1
            for i in range(k):
                h = (h * b + a[i]) % mod
                p = (p * b) % mod
            c = Counter([h])
            for i in range(k, n):
                h = (h * b + a[i] - a[i - k] * p) % mod
                c[h] += 1
            if 1 in c.values():
                r = k
            else:
                l = k + 1
        return l

class Solution: # MLE
    def smallestUniqueSubarray(self, a: List[int]) -> int:
        return bisect_left(range(len(a)+1),1,key=lambda k:1in Counter(zip(*[a[i:]for i in range(k)])).values())

class Solution: # MLE
    def smallestUniqueSubarray(self, a: List[int]) -> int:
        return bisect_left(range(1,len(a)+1),1,key=lambda k:1in Counter(tuple(a[i:i+k])for i in range(len(a)-k+1)).values())+1

class Solution:
    def smallestUniqueSubarray(self, a: List[int]) -> int:
        m=10**18+9;return bisect_left(range(len(s:=[*accumulate(a,lambda h,x:(h*7**20+x)%m,initial=0)])),1,key=lambda k:1in Counter((h-g*p)%m for p in[pow(7**20,k,m)]for g,h in zip(s,s[k:])).values())

class Solution:
    def smallestUniqueSubarray(self, a: List[int]) -> int:
        m=10**18+9;return bisect_left(range(len(s:=[*accumulate([0,*a],lambda h,x:(h*7**20+x)%m)])),1,key=lambda k:1in Counter((h-g*p)%m for p in[pow(7**20,k,m)]for g,h in zip(s,s[k:])).values())

test('''
3934. Smallest Unique Subarray
Hard
Topics
premium lock icon
Companies
Hint
You are given an integer array nums.

Find the minimum length of a subarray that is not identical to any other subarray in nums.

Return an integer denoting the minimum possible length of such a subarray.

Two subarrays are considered identical if they have the same length and the same elements in corresponding positions.

 

Example 1:

Input: nums = [3,3,3]

Output: 3

Explanation:

Subarrays of length 1: [3] → appears 3 times
Subarrays of length 2: [3, 3] → appears 2 times
Subarrays of length 3: [3, 3, 3] → appears once
The subarray [3, 3, 3] is unique, so the smallest unique subarray length is 3.

Example 2:

Input: nums = [2,1,2,3,3]

Output: 1

Explanation:

Subarrays of length 1:

[2] → appears 2 times
[1] → appears once
[3] → appears 2 times
The subarray [1] is unique, so the smallest unique subarray length is 1.
Example 3:

Input: nums = [1,1,2,2,1]

Output: 2

Explanation:

Subarrays of length 1:

[1] → appears 3 times
[2] → appears 2 times
Subarrays of length 2:

[1, 1] → appears once
[1, 2] → appears once
[2, 2] → appears once
[2, 1] → appears once
There is at least one subarray of length 2 that is unique, so the smallest unique subarray length is 2.
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 105
 
Seen this question in a real interview before?
1/6
Yes
No
Accepted
8,799/21.9K
Acceptance Rate
40.3%
Topics
Senior Staff
Array
Hash Table
Binary Search
Rolling Hash
Suffix Array
Hash Function
Weekly Contest 502
icon
Companies
Hint 1
Think in terms of checking a fixed length len: count all subarrays of length len, and see whether any one appears exactly once.
Hint 2
Use rolling hash so each subarray can be represented in O(1) after preprocessing, instead of comparing arrays directly.
Hint 3
The answer can be binary searched because if there is a unique subarray of length len, then there is also a unique subarray of some length > len.
Hint 4
For each checked length, store frequencies of hashes in a hashmap. If any hash has frequency 1, that length works.
''')
