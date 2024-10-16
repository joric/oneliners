from lc import *

# https://leetcode.com/problems/kth-distinct-string-in-an-array/discuss/5588042/One-line-solution

class Solution:
    def kthDistinct(self, a: List[str], k: int) -> str:
        c=Counter(a);return next((s for i,s in enumerate(x for x in a if c[x]<1)if i==k-1),'')

class Solution:
    def kthDistinct(self, a: List[str], k: int) -> str:
        return next((s for i,s in enumerate(x for x in a if a.count(x)<2)if i==k-1),'')

# https://leetcode.com/problems/kth-distinct-string-in-an-array/discuss/1550617/Python-simple-2-lines-solution

class Solution:
    def kthDistinct(self, a: List[str], k: int) -> str: 
        d=[s for s,c in Counter(a).items()if c==1];return d[k-1:]and d[k-1]or''

class Solution:
    def kthDistinct(self, a: List[str], k: int) -> str:
        return next(iter([x for x in a if a.count(x)<2][k-1:]),'')

# https://leetcode.com/problems/kth-distinct-string-in-an-array/discuss/5588041/Python-One-Liner-for-Fun

class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        return([k for k,v in Counter(arr).items()if v<2]+['']*k)[k-1]

class Solution:
    def kthDistinct(self, a: List[str], k: int) -> str:
        return([x for x in a if a.count(x)<2]+k*[''])[k-1]

test('''
2053. Kth Distinct String in an Array
Easy

758

32

Add to List

Share
A distinct string is a string that is present only once in an array.

Given an array of strings arr, and an integer k, return the kth distinct string present in arr. If there are fewer than k distinct strings, return an empty string "".

Note that the strings are considered in the order in which they appear in the array.

 

Example 1:

Input: arr = ["d","b","c","b","c","a"], k = 2
Output: "a"
Explanation:
The only distinct strings in arr are "d" and "a".
"d" appears 1st, so it is the 1st distinct string.
"a" appears 2nd, so it is the 2nd distinct string.
Since k == 2, "a" is returned. 
Example 2:

Input: arr = ["aaa","aa","a"], k = 1
Output: "aaa"
Explanation:
All strings in arr are distinct, so the 1st string "aaa" is returned.
Example 3:

Input: arr = ["a","b","a"], k = 3
Output: ""
Explanation:
The only distinct string is "b". Since there are fewer than 3 distinct strings, we return an empty string "".
 

Constraints:

1 <= k <= arr.length <= 1000
1 <= arr[i].length <= 5
arr[i] consists of lowercase English letters.
Accepted
67,007
Submissions
91,552
''')