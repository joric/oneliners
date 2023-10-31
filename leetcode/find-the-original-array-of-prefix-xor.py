from lc import *

# https://leetcode.com/problems/find-the-original-array-of-prefix-xor/discuss/2678904/JavaC%2B%2BPython-Easy-and-Concise-with-Explantion

class Solution:
    def findArray(self, p: List[int]) -> List[int]:
        return starmap(xor,pairwise([0]+p))

class Solution:
    def findArray(self, p: List[int]) -> List[int]:
        return map(xor,p,[0]+p[:-1])

class Solution:
    def findArray(self, p: List[int]) -> List[int]:
        return map(xor,p,[0]+p)

test('''
2433. Find The Original Array of Prefix Xor
Medium

644

32

Add to List

Share
You are given an integer array pref of size n. Find and return the array arr of size n that satisfies:

pref[i] = arr[0] ^ arr[1] ^ ... ^ arr[i].
Note that ^ denotes the bitwise-xor operation.

It can be proven that the answer is unique.

 

Example 1:

Input: pref = [5,2,0,3,1]
Output: [5,7,2,3,2]
Explanation: From the array [5,7,2,3,2] we have the following:
- pref[0] = 5.
- pref[1] = 5 ^ 7 = 2.
- pref[2] = 5 ^ 7 ^ 2 = 0.
- pref[3] = 5 ^ 7 ^ 2 ^ 3 = 3.
- pref[4] = 5 ^ 7 ^ 2 ^ 3 ^ 2 = 1.
Example 2:

Input: pref = [13]
Output: [13]
Explanation: We have pref[0] = arr[0] = 13.
 

Constraints:

1 <= pref.length <= 10^5
0 <= pref[i] <= 10^6
''')

