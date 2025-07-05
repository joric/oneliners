from lc import *

# https://leetcode.com/problems/find-lucky-integer-in-an-array/submissions/316935355/?envType=daily-question&envId=2025-07-05

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq = collections.Counter(arr)
        lucky = -1
        for k,v in freq.iteritems():
            if k==v:
                lucky = max(lucky, k)
        return lucky

class Solution:
    def findLucky(self, a: List[int]) -> int:
        c=Counter(a);return max([-1]+[i for i in c if i==c[i]])

test('''
1394. Find Lucky Integer in an Array
Solved
Easy
Topics
premium lock icon
Companies
Hint
Given an array of integers arr, a lucky integer is an integer that has a frequency in the array equal to its value.

Return the largest lucky integer in the array. If there is no lucky integer return -1.

 

Example 1:

Input: arr = [2,2,3,4]
Output: 2
Explanation: The only lucky number in the array is 2 because frequency[2] == 2.
Example 2:

Input: arr = [1,2,2,3,3,3]
Output: 3
Explanation: 1, 2 and 3 are all lucky numbers, return the largest of them.
Example 3:

Input: arr = [2,2,2,3,3]
Output: -1
Explanation: There are no lucky numbers in the array.
 

Constraints:

1 <= arr.length <= 500
1 <= arr[i] <= 500
Seen this question in a real interview before?
1/5
Yes
No
Accepted
171,691/243.6K
Acceptance Rate
70.5%
Topics
Array
Hash Table
Counting
icon
Companies
Hint 1
Count the frequency of each integer in the array.
Hint 2
Get all lucky numbers and return the largest of them.
''')
