from lc import *

# https://leetcode.com/problems/prime-subtraction-operation/discuss/3721120/Python-almost-linear-solution-with-explanation

class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        primes = [0, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]
        prev_small = 0
        for v in nums:
            pos, is_found = bisect_left(primes, v), False
            for i in range(pos - 1, -1, -1):
                if v - primes[i] > prev_small:
                    prev_small = v - primes[i]
                    is_found = True
                    break
            if not is_found:
                return False
        return True

class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        g=range(2,n:=999);primes=sorted([0,*reduce(lambda r,x:r-set(range(x**2,n,x))if x in r else r,g,set(g))])
        prev_small = 0
        for v in nums:
            pos, is_found = bisect_left(primes, v), False
            for i in range(pos - 1, -1, -1):
                if v - primes[i] > prev_small:
                    prev_small = v - primes[i]
                    is_found = True
                    break
            if not is_found:
                return False
        return True

# https://leetcode.com/problems/prime-subtraction-operation/discuss/5386264/Small-Python-solution

# Pregenerated primes + 0 as a prefix for convenience
class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        primes = [0, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]
        min_value = 1
        for n in nums:
            best = n - primes[bisect_right(primes, n - min_value) - 1]
            if best < min_value:
                return False
            min_value = best + 1
        return True

class Solution:
    def primeSubOperation(self, a: List[int]) -> bool:
        m,g=1,range(2,n:=999);p=sorted([0,*reduce(lambda r,x:x in r and r-set(range(x**2,n,x))or r,g,set(g))]);return all(m<=(b:=n-p[bisect_right(p,n-m)-1])and(m:=b+1)for n in a)

test('''
2601. Prime Subtraction Operation
Medium

388

42

Add to List

Share
You are given a 0-indexed integer array nums of length n.

You can perform the following operation as many times as you want:

Pick an index i that you haven’t picked before, and pick a prime p strictly less than nums[i], then subtract p from nums[i].
Return true if you can make nums a strictly increasing array using the above operation and false otherwise.

A strictly increasing array is an array whose each element is strictly greater than its preceding element.

 

Example 1:

Input: nums = [4,9,6,10]
Output: true
Explanation: In the first operation: Pick i = 0 and p = 3, and then subtract 3 from nums[0], so that nums becomes [1,9,6,10].
In the second operation: i = 1, p = 7, subtract 7 from nums[1], so nums becomes equal to [1,2,6,10].
After the second operation, nums is sorted in strictly increasing order, so the answer is true.
Example 2:

Input: nums = [6,8,11,12]
Output: true
Explanation: Initially nums is sorted in strictly increasing order, so we don't need to make any operations.
Example 3:

Input: nums = [5,8,3]
Output: false
Explanation: It can be proven that there is no way to perform operations to make nums sorted in strictly increasing order, so the answer is false.
 

Other examples:

Input: nums = [998,2]
Output: true

Constraints:

1 <= nums.length <= 1000
1 <= nums[i] <= 1000
nums.length == n
Accepted
18,003
Submissions
46,695
''')
