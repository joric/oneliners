from lc import *

# https://leetcode.com/problems/maximum-element-after-decreasing-and-rearranging/discuss/4289169/Python-one-line

class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, l: List[int]) -> int:
        return [*accumulate([1]+sorted(l)[1:],lambda x,y:min(x+1,y))][-1]

# https://leetcode.com/problems/maximum-element-after-decreasing-and-rearranging/discuss/4289380/One-line-Python-List-Comprehension-Faster-than-91

class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, a: List[int]) -> int:
        return len(a)-max([i+1-x for i,x in enumerate(sorted(a))]+[0])

# https://leetcode.com/problems/maximum-element-after-decreasing-and-rearranging/discuss/1185804/JavaC%2B%2BPython-Sort-and-One-pass

class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, a: List[int]) -> int:
        a.sort()
        r = 0
        for x in a:
            r=min(r+1, x)
        return r

class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, a: List[int]) -> int:
        return reduce(lambda r,x:min(r+1,x),sorted(a),0)

class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, a: List[int]) -> int:
        r=0;[r:=min(r+1,c)for c in sorted(a)];return r

class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, a: List[int]) -> int:
        sort(a);r=0;[r:=min(r+1,c)for c in a];return r

test('''
1846. Maximum Element After Decreasing and Rearranging
Medium

621

150

Add to List

Share
You are given an array of positive integers arr. Perform some operations (possibly none) on arr so that it satisfies these conditions:

The value of the first element in arr must be 1.
The absolute difference between any 2 adjacent elements must be less than or equal to 1. In other words, abs(arr[i] - arr[i - 1]) <= 1 for each i where 1 <= i < arr.length (0-indexed). abs(x) is the absolute value of x.
There are 2 types of operations that you can perform any number of times:

Decrease the value of any element of arr to a smaller positive integer.
Rearrange the elements of arr to be in any order.
Return the maximum possible value of an element in arr after performing the operations to satisfy the conditions.

 

Example 1:

Input: arr = [2,2,1,2,1]
Output: 2
Explanation: 
We can satisfy the conditions by rearranging arr so it becomes [1,2,2,2,1].
The largest element in arr is 2.
Example 2:

Input: arr = [100,1,1000]
Output: 3
Explanation: 
One possible way to satisfy the conditions is by doing the following:
1. Rearrange arr so it becomes [1,100,1000].
2. Decrease the value of the second element to 2.
3. Decrease the value of the third element to 3.
Now arr = [1,2,3], which satisfies the conditions.
The largest element in arr is 3.
Example 3:

Input: arr = [1,2,3,4,5]
Output: 5
Explanation: The array already satisfies the conditions, and the largest element is 5.
 

Example 4:

Input: arr = [73,98,9]
Output: 3

Constraints:

1 <= arr.length <= 10^5
1 <= arr[i] <= 10^9
Accepted
46,272
Submissions
72,426
''')


