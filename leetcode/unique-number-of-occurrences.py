from lc import *

# https://leetcode.com/problems/unique-number-of-occurrences/discuss/949934/python-3-one-line

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        return len(Counter(arr))==len(set(Counter(arr).values()))

class Solution:
    def uniqueOccurrences(self, a: List[int]) -> bool:
        return eq(*map(len,map(set,(a,Counter(a).values()))))

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        return len(set(arr))==len(set(Counter(arr).values()))

class Solution:
    def uniqueOccurrences(self, a: List[int]) -> bool:
        return len(c:=Counter(a))==len({*c.values()})

class Solution:
    def uniqueOccurrences(self, a: List[int]) -> bool:
        return len({*a})==len({*Counter(a).values()})

test('''

1207. Unique Number of Occurrences
Easy

2232

51

Add to List

Share
Given an array of integers arr, return true if the number of occurrences of each value in the array is unique, or false otherwise.

Example 1:

Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.

Example 2:

Input: arr = [1,2]
Output: false

Example 3:

Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
Output: true

Example 4:

Input: arr = [1, 2,2, 3,3,3, 4,4,4,4]
Output: true

Constraints:

1 <= arr.length <= 1000
-1000 <= arr[i] <= 1000

''')

