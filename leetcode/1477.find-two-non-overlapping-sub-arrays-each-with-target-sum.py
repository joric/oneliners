from lc import *

# https://leetcode.com/problems/find-two-non-overlapping-sub-arrays-each-with-target-sum/solutions/8512763/three-simple-lines-of-code-by-mikposp-ghnu/?envType=daily-question&envId=2026-09-17

class Solution:
    def minSumOfLengths(self, a: List[int], t: int) -> int:
        f=lambda a:[*accumulate(map(lambda p:d[p]-d.get(p-t,-inf),d:=dict(zip([0,*accumulate(a)],count(-1)))),min)];return(-1,r:=min(map(add,f(a),f(a[::-1])[::-1])))[r<inf]

class Solution:
    def minSumOfLengths(self, a: List[int], t: int) -> int:
        c=accumulate;f=lambda a:[*c(map(lambda p:d[p]-d.get(p-t,-inf),d:=dict(zip([0,*c(a)],count(-1)))),min)];return(-1,r:=min(map(add,f(a),f(a[::-1])[::-1])))[r<inf]

class Solution:
    def minSumOfLengths(self, a: List[int], t: int) -> int:
        c=accumulate;f=lambda a:[*c(map(lambda p:d[p]-d.get(p-t,-inf),d:=dict(zip(c([0]+a),count()))),min)];return(-1,r:=min(map(add,f(a),f(a[::-1])[::-1])))[r<inf]

class Solution:
    def minSumOfLengths(self, a: List[int], t: int) -> int:
        n=7**6;d={t:n-1};b=[n]*n;s=0;return min(n,*(b.append(min(b[-1],l:=d.setdefault((s:=s+x)+t,len(b))-(j:=d.get(s,0))))or l-~b[j]for x in a))%n-1

class Solution:
    def minSumOfLengths(self, a: List[int], t: int) -> int:
        n=7**6;d={0:n-1};b=[n]*n;s=0;return min(n,*(b.append(min(b[-1],l:=d.setdefault(s:=s+x,len(b))-(j:=d.get(s-t,0))))or l-~b[j]for x in a))%n-1

test('''
1477. Find Two Non-overlapping Sub-arrays Each With Target Sum
Solved
Medium
Topics
premium lock icon
Companies
Hint
You are given an array of integers arr and an integer target.

You have to find two non-overlapping sub-arrays of arr each with a sum equal target. There can be multiple answers so you have to find an answer where the sum of the lengths of the two sub-arrays is minimum.

Return the minimum sum of the lengths of the two required sub-arrays, or return -1 if you cannot find such two sub-arrays.

 

Example 1:

Input: arr = [3,2,2,4,3], target = 3
Output: 2
Explanation: Only two sub-arrays have sum = 3 ([3] and [3]). The sum of their lengths is 2.
Example 2:

Input: arr = [7,3,4,7], target = 7
Output: 2
Explanation: Although we have three non-overlapping sub-arrays of sum = 7 ([7], [3,4] and [7]), but we will choose the first and third sub-arrays as the sum of their lengths is 2.
Example 3:

Input: arr = [4,3,2,6,2,3,4], target = 6
Output: -1
Explanation: We have only one sub-array of sum = 6.
 

Constraints:

1 <= arr.length <= 105
1 <= arr[i] <= 1000
1 <= target <= 108
 
Seen this question in a real interview before?
1/6
Yes
No
Accepted
57,120/154K
Acceptance Rate
37.1%
Topics
Staff
Array
Hash Table
Binary Search
Dynamic Programming
Sliding Window
Biweekly Contest 28
icon
Companies
Hint 1
Let's create two arrays prefix and suffix where prefix[i] is the minimum length of sub-array ends before i and has sum = k, suffix[i] is the minimum length of sub-array starting at or after i and has sum = k.
Hint 2
The answer we are searching for is min(prefix[i] + suffix[i]) for all values of i from 0 to n-1 where n == arr.length.
Hint 3
If you are still stuck with how to build prefix and suffix, you can store for each index i the length of the sub-array starts at i and has sum = k or infinity otherwise, and you can use it to build both prefix and suffix.
Similar Questions
Find Subarrays With Equal Sum
Easy
''')
