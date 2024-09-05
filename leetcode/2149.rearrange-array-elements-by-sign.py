from lc import *

# https://leetcode.com/problems/rearrange-array-elements-by-sign
# cannot be done in O(1) space O(n) time with swaps because every swap breaks natural order for the next step
# can be done in O(1) space and O(n^2) time

# O(n^2), TLE
class Solution:
    def rearrangeArray(self, a: List[int]) -> List[int]:
        def rr(i,j):
            t = a[i];
            while i>j:
                a[i] = a[i-1]
                i -= 1
            a[j] = t
        j = -1
        for i,x in enumerate(a):
            if j>=0:
                if (x<0 and a[j]>=0) or (x>=0 and a[j]<0):
                    rr(i,j)
                    j = j+2 if i-j>=2 else -1
            elif (x<0 and i%2==0) or (x>=0 and i%2!=0):
                j = i
        return a

# https://leetcode.com/problems/rearrange-array-elements-by-sign/discuss/4723541/Two-solutions.-O(n).-One-pass

class Solution:
    def rearrangeArray(self, a: List[int]) -> List[int]:
        r,i,j=[0]*len(a),0,1
        for x in a:
            if x < 0:
                r[j] = x
                j += 2
            else:
                r[i] = x
                i += 2 
        return r

class Solution:
    def rearrangeArray(self, a: List[int]) -> List[int]:
        r,i,j=[0]*len(a),-2,-1;[setitem(r,(i:=i+2*(1-(t:=int(x<0))),j:=j+2*t)[t],x)for x in a];return r

# https://leetcode.com/problems/rearrange-array-elements-by-sign/discuss/3523881/One-Line-Solution

class Solution:
    def rearrangeArray(self, a: List[int]) -> List[int]:
        a.sort(key=lambda x:(x>0)-(x<0));return chain(*zip(a[len(a)//2:],a))

class Solution:
    def rearrangeArray(self, a: List[int]) -> List[int]:
        return chain(*zip((x for x in a if x>0),(x for x in a if x<0)))

class Solution:
    def rearrangeArray(self, a: List[int]) -> List[int]:
        return chain(*zip(*[[x for x in a if o(x,0)]for o in(ge,le)]))

class Solution:
    def rearrangeArray(self, a: List[int]) -> List[int]:
        return chain(*zip(filter(f:=(0).__le__,a),filterfalse(f,a)))

class Solution:
    def rearrangeArray(self, a: List[int]) -> List[int]:
        a.sort(key=(0).__le__);return chain(*zip(a[len(a)//2:],a))

class Solution:
    def rearrangeArray(self, a: List[int]) -> List[int]:
        a.sort(key=0..__le__);return chain(*zip(a[len(a)//2:],a)) # also works with key=.0.__le__

test('''
2149. Rearrange Array Elements by Sign
Medium

2448

105

Add to List

Share
You are given a 0-indexed integer array nums of even length consisting of an equal number of positive and negative integers.

You should rearrange the elements of nums such that the modified array follows the given conditions:

Every consecutive pair of integers have opposite signs.
For all integers with the same sign, the order in which they were present in nums is preserved.
The rearranged array begins with a positive integer.
Return the modified array after rearranging the elements to satisfy the aforementioned conditions.

 

Example 1:

Input: nums = [3,1,-2,-5,2,-4]
Output: [3,-2,1,-5,2,-4]
Explanation:
The positive integers in nums are [3,1,2]. The negative integers are [-2,-5,-4].
The only possible way to rearrange them such that they satisfy all conditions is [3,-2,1,-5,2,-4].
Other ways such as [1,-2,2,-5,3,-4], [3,1,2,-2,-5,-4], [-2,3,-5,1,-4,2] are incorrect because they do not satisfy one or more conditions.  
Example 2:

Input: nums = [-1,1]
Output: [1,-1]
Explanation:
1 is the only positive integer and -1 the only negative integer in nums.
So nums is rearranged to [1,-1].
 

Constraints:

2 <= nums.length <= 2 * 10^5
nums.length is even
1 <= |nums[i]| <= 10^5
nums consists of equal number of positive and negative integers.
Accepted
165,908
Submissions
201,607
''')