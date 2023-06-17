from lc import *

class Solution:
    def makeArrayIncreasing(self, a: List[int], b: List[int]) -> int:
        b.sort();
        @cache
        def f(i,x):
            if i==len(a):
                return 0
            return min(1+f(i+1,b[j]) if (j:=bisect_right(b,x))<len(b) else inf, f(i+1,a[i]) if x<a[i] else inf)
        return r if (r:=f(0,-inf))<inf else -1

class Solution:
    def makeArrayIncreasing(self, a: List[int], b: List[int]) -> int:
        b.sort();f=cache(lambda i,x:i<len(a)and min((j:=bisect_right(b,x))<len(b)and 1+f(i+1,b[j])or inf,f(i+1,a[i])if x<a[i]else inf));r=f(0,-inf);return(-1,r)[r<inf]

test('''
1187. Make Array Strictly Increasing
Hard

835

19

Add to List

Share
Given two integer arrays arr1 and arr2, return the minimum number of operations (possibly zero) needed to make arr1 strictly increasing.

In one operation, you can choose two indices 0 <= i < arr1.length and 0 <= j < arr2.length and do the assignment arr1[i] = arr2[j].

If there is no way to make arr1 strictly increasing, return -1.

 

Example 1:

Input: arr1 = [1,5,3,6,7], arr2 = [1,3,2,4]
Output: 1
Explanation: Replace 5 with 2, then arr1 = [1, 2, 3, 6, 7].
Example 2:

Input: arr1 = [1,5,3,6,7], arr2 = [4,3,1]
Output: 2
Explanation: Replace 5 with 3 and then replace 3 with 4. arr1 = [1, 3, 4, 6, 7].
Example 3:

Input: arr1 = [1,5,3,6,7], arr2 = [1,6,3,3]
Output: -1
Explanation: You can't make arr1 strictly increasing.
 

Constraints:

1 <= arr1.length, arr2.length <= 2000
0 <= arr1[i], arr2[i] <= 10^9
 

Accepted
14,400
Submissions
31,560
Seen this question in a real interview before?

Yes

No
Use dynamic programming.
The state would be the index in arr1 and the index of the previous element in arr2 after sorting it and removing duplicates.
''')
