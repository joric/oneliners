from lc import *

class Solution:
    def arraySign(self, nums: List[int]) -> int:
        return 0 if 0 in nums else -1 if sum(filter(lambda x:x<0, nums))%2 else 1

class Solution:
    def arraySign(self, nums: List[int]) -> int:
        return 0 if 0 in nums else -1 if len([x for x in nums if x<0])%2 else 1

class Solution:
    def arraySign(self, nums: List[int]) -> int:
        return 0 if 0 in nums else -1 if reduce(lambda _,x:x<0, nums)%2 else 1

class Solution:
    def arraySign(self, nums: List[int]) -> int:
        return reduce(lambda a,c:0 if c==0 else a if c>0 else -a, nums, 1)

class Solution:
    def arraySign(self, nums: List[int]) -> int:
        return reduce(lambda x,y:x*(y and copysign(1,y)), nums, 1)

class Solution:
    def arraySign(self, nums: List[int]) -> int:
        return reduce(lambda x,y:x*(y and y/abs(y)), nums, 1)

class Solution:
    def arraySign(self, nums: List[int]) -> int:
        return reduce(lambda x,y:(x*y>0)-(x*y<0), nums, 1)

test('''
1822. Sign of the Product of an Array
Easy

1737

173

Add to List

Share
There is a function signFunc(x) that returns:

1 if x is positive.
-1 if x is negative.
0 if x is equal to 0.
You are given an integer array nums. Let product be the product of all values in the array nums.

Return signFunc(product).

 

Example 1:

Input: nums = [-1,-2,-3,-4,3,2,1]
Output: 1
Explanation: The product of all values in the array is 144, and signFunc(144) = 1
Example 2:

Input: nums = [1,5,0,2,-3]
Output: 0
Explanation: The product of all values in the array is 0, and signFunc(0) = 0
Example 3:

Input: nums = [-1,1,-1,1,-1]
Output: -1
Explanation: The product of all values in the array is -1, and signFunc(-1) = -1
 

Constraints:

1 <= nums.length <= 1000
-100 <= nums[i] <= 100
Accepted
242,783
Submissions
367,500
Seen this question in a real interview before?

Yes

No
If there is a 0 in the array the answer is 0
To avoid overflow make all the negative numbers -1 and all positive numbers 1 and calculate the prod
''')


