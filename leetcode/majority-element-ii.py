from lc import *

# misra-gries

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        count1, count2, candidate1, candidate2 = 0, 0, 0, 1
        for n in nums:
            if n == candidate1:
                count1 += 1
            elif n == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1, count1 = n, 1
            elif count2 == 0:
                candidate2, count2 = n, 1
            else:
                count1, count2 = count1 - 1, count2 - 1
        return [n for n in (candidate1, candidate2)
                        if nums.count(n) > len(nums) // 3] 

# fast
class Solution:
    def majorityElement(self, a: List[int]) -> List[int]:
        t=len(a)//3;return[n for n in set(sorted(a)[t::max(t,1)]) if a.count(n)>t]

# slow
class Solution:
    def majorityElement(self, a: List[int]) -> List[int]:
        return[k for k,v in Counter(a).items() if v>len(a)/3]

class Solution:
    def majorityElement(self, a: List[int]) -> List[int]:
        return[i for i in{*a}if Counter(a)[i]>len(a)/3]

class Solution:
    def majorityElement(self, a: List[int]) -> List[int]:
        return[i for i in{*a}if a.count(i)>len(a)/3]

class Solution:
    def majorityElement(self, a: List[int]) -> List[int]:
        return{i for i in a if a.count(i)>len(a)/3}

test('''
229. Majority Element II
Medium

8266

363

Add to List

Share
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

 

Example 1:

Input: nums = [3,2,3]
Output: [3]
Example 2:

Input: nums = [1]
Output: [1]
Example 3:

Input: nums = [1,2]
Output: [1,2]
 

Constraints:

1 <= nums.length <= 5 * 10^4
-10^9 <= nums[i] <= 10^9
''', check=lambda e,x,*args:sorted(e)==sorted(x))

