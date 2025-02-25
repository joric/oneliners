from lc import *

# https://leetcode.com/problems/minimum-number-of-k-consecutive-bit-flips/discuss/238609/JavaC%2B%2BPython-One-Pass-and-O(1)-Space

class Solution:
    def minKBitFlips(self, a: List[int], k: int) -> int:
        c, r, n = 0, 0, len(a)
        for i in range(len(a)):
            if i >= k and a[i - k] > 1:
                a[i - k] -= 2
                c -= 1
            if c & 1 ^ a[i] == 0:
                if i + k > len(a):
                    return -1
                a[i] += 2
                c += 1
                r += 1
        return r

class Solution:
    def minKBitFlips(self, a: List[int], k: int) -> int:
        c,r,n=0,0,len(a)
        for i in range(n):
            if i>=k and a[i-k]>1:
                c -= 1
            if c%2==a[i]:
                if i+k>n:
                    return -1
                a[i]=2
                c += 1
                r += 1
        return r

# https://leetcode.com/problems/minimum-number-of-k-consecutive-bit-flips/discuss/3103263/Python-3-oror-8-lines-accumulate-w-explanation-oror-TS%3A-98-95

class Solution:
    def minKBitFlips(self, a: List[int], k: int) -> int:
        c, t = [0] * len(a), 0
        for i,x in enumerate(a):
            if i >= k:
                t ^= c[i-k]
            if t != x:
                continue
            if k > len(a)-i:
                return -1
            t ^= 1
            c[i] = 1
        return sum(c)

class Solution:
    def minKBitFlips(self, a: List[int], k: int) -> int:
        t,n=0,len(a);c=[0]*n
        for i,x in enumerate(a):
            i>=k and(t:=t^c[i-k])
            if t==x and (k>n-i or(t:=t^1,setitem(c,i,1))==0):
                return -1
        return sum(c)

class Solution:
    def minKBitFlips(self, a: List[int], k: int) -> int:
        t,n=0,len(a);c=[0]*n
        for i,x in enumerate(a):
            if x==(t:=i<k and t or t^c[i-k])and(k>n-i or not(t:=t^1,setitem(c,i,1))):
                return -1
        return sum(c)

class Solution:
    def minKBitFlips(self, a: List[int], k: int) -> int:
        t,n=0,len(a);c=[0]*n;return next((-1 for i,x in enumerate(a)if(t:=i<k and t or t^c[i-k])==x and(k>n-i or(t:=t^1,setitem(c,i,1))==0)),0)or sum(c)


# https://leetcode.com/problems/minimum-number-of-k-consecutive-bit-flips/discuss/5359837/Elixir-Greedy-and-Bit-Manipulation
# very cool, but out of memory

class Solution:
    def minKBitFlips(self, a: List[int], k: int) -> int:
        def f(n,m,c):
            if n==1: return c
            if n&1: return f(n>>1,m,c)
            if n<m: return -1
            return f(n^m,m,c+1)
        return f(reduce(lambda r,b:(r<<1)|b,a,1),(1<<k)-1,0)

# iterative version

class Solution:
    def minKBitFlips(self, a: List[int], k: int) -> int:
        n = reduce(lambda r,b:r<<1|b,a,1)
        m = (1<<k)-1
        c = 0
        while True:
            if n==0: return c
            if n%2:
                n >>= 1
            else:
                if n<m: return -1
                n = (n^m)>>1
                c += 1

class Solution:
    def minKBitFlips(self, a: List[int], k: int) -> int:
        n,m,c=1,(1<<k)-1,0;[n:=n<<1|b for b in a];
        for _ in a*2:
            if n&1<1:
                if n<m: break
                n = (n^m)>>1
                c += 1
            else:
                n >>= 1
        return(c,-1)[n>0]

class Solution:
    def minKBitFlips(self, a: List[int], k: int) -> int:
        n,m,c=1,(1<<k)-1,0;[n:=n<<1|b for b in a];return next((c,-1)[n>0]for _ in a*2 if n&1<1 and n<m or[(n:=n>>1)if n&1 else(n:=(n^m)>>1,c:=c+1)]==0)


# https://leetcode.com/problems/minimum-number-of-k-consecutive-bit-flips/discuss/1568109/Short-Python

class Solution:
    def minKBitFlips(self, a: List[int], k: int) -> int:
        n, c = len(a), []
        for i in range(n):
            if (len(c)-bisect_left(c,i-k+1)+a[i])%2==0:
                c.append(i)
                if i>n-k:
                    return -1
        return len(c)

class Solution:
    def minKBitFlips(self, a: List[int], k: int) -> int:
        n,c=len(a),[];return next((-1 for i in range(n)if(len(c)-bisect_left(c,i-k+1)+a[i])&1<1 and(c.append(i)or i>n-k)),0)or len(c)

# another solution

class Solution:
    def minKBitFlips(self, a: List[int], k: int) -> int:
        s=[0]*k;s.extend(map(xor,s,map(xor,[1]+a,a+[1])));return sum(s[-k:])and-1 or sum(s)

test('''
995. Minimum Number of K Consecutive Bit Flips
Hard

1440

74

Add to List

Share
You are given a binary array nums and an integer k.

A k-bit flip is choosing a subarray of length k from nums and simultaneously changing every 0 in the subarray to 1, and every 1 in the subarray to 0.

Return the minimum number of k-bit flips required so that there is no 0 in the array. If it is not possible, return -1.

A subarray is a contiguous part of an array.

 

Example 1:

Input: nums = [0,1,0], k = 1
Output: 2
Explanation: Flip nums[0], then flip nums[2].
Example 2:

Input: nums = [1,1,0], k = 2
Output: -1
Explanation: No matter how we flip subarrays of size 2, we cannot make the array become [1,1,1].
Example 3:

Input: nums = [0,0,0,1,0,1,1,0], k = 3
Output: 3
Explanation: 
Flip nums[0],nums[1],nums[2]: nums becomes [1,1,1,1,0,1,1,0]
Flip nums[4],nums[5],nums[6]: nums becomes [1,1,1,1,1,0,0,0]
Flip nums[5],nums[6],nums[7]: nums becomes [1,1,1,1,1,1,1,1]
 

Constraints:

1 <= nums.length <= 105
1 <= k <= nums.length
Accepted
59,188
Submissions
105,729
''')