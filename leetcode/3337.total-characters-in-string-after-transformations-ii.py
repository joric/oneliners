from lc import *

# https://leetcode.com/problems/total-characters-in-string-after-transformations-ii/solutions/6742197/if-you-use-numpy-beware-of-the-integer-overflow/

import numpy as np

class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
        cnt,mo = [0]*26,7+10**9
        cnt = np.array(cnt, dtype=object)

        for l in s:
            cur = ord(l) - ord('a')
            cnt[cur] += 1

        ref = np.zeros((26,26), dtype=object)

        for i in range(26):
            temp = nums[i]
            new = [0]*26

            for j in range(nums[i]):
                k = (i+j+1)%26
                new[k] += 1
                new[k] %= mo

            ref[i] = np.array(new, dtype=object)

        ref = ref.T

        while t:
            if t%2:
                cnt = (ref @ cnt) % mo
            t //= 2
            ref = (ref @ ref) % mo
        
        return int(np.sum(cnt)%mo)

# https://leetcode.com/problems/total-characters-in-string-after-transformations-ii/solutions/5974501/python-using-numpy/?envType=daily-question&envId=2025-05-14

import numpy as np

MOD = 10**9 + 7
class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
        base,cur = np.zeros((26,26)), np.eye(26)
        for i,v in enumerate(nums):
            for j in range(i+1, i+v+1):
                base[i][j%26]=1
        def mul(a,b):
            c = np.dot(a,b)
            for i,j in product(range(26),repeat=2):
                c[i][j]%=MOD
            return c
        while t:
            if t&1>0: cur=mul(cur,base)
            base=mul(base,base)
            t>>=1
        data=[sum(r)%MOD for r in cur]
        return sum(data[ord(ch)-97] for ch in s)%MOD

import numpy as np
MOD = 10**9 + 7
class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
        base,cur = np.zeros((26,26), dtype=object), np.eye(26, dtype=object)
        for i,v in enumerate(nums):
            for j in range(i+1, i+v+1):
                base[i][j%26]=1
        while t:
            if t&1>0: cur=np.dot(cur,base)%MOD
            base=np.dot(base,base)%MOD
            t>>=1
        data=[sum(r)%MOD for r in cur]
        return sum(data[ord(ch)-97] for ch in s)%MOD

class Solution:
    def lengthAfterTransformations(self, s: str, t: int, a: List[int]) -> int:
        p,n,m=__import__('numpy'),26,10**9+7
        u,v=p.eye(n,dtype=object),p.zeros((n,n),dtype=object)
        [setitem(v[i],j%n,1)for i,x in enumerate(a)for j in range(i+1,i+x+1)]
        all((t&1 and(u:=p.dot(u,v)%m),v:=p.dot(v,v)%m,t:=t>>1)[2] for _ in count())
        return sum(sum(u[ord(c)-97])%m for c in s)%m

class Solution:
    def lengthAfterTransformations(self, s: str, t: int, a: List[int]) -> int:
        p,m,o=__import__('numpy'),10**9+7,object;u,v=p.eye(n:=26,dtype=o),p.zeros((n,n),dtype=o);[setitem(v[i],j%n,1)for i,x in enumerate(a)for j in range(i+1,i+x+1)];all((t&1 and(u:=p.dot(u,v)%m),v:=p.dot(v,v)%m,t:=t>>1)[2]for _ in count());return sum(sum(u[ord(c)-97])%m for c in s)%m

test('''
3337. Total Characters in String After Transformations II
Hard
Topics
Companies
Hint
You are given a string s consisting of lowercase English letters, an integer t representing the number of transformations to perform, and an array nums of size 26. In one transformation, every character in s is replaced according to the following rules:

Replace s[i] with the next nums[s[i] - 'a'] consecutive characters in the alphabet. For example, if s[i] = 'a' and nums[0] = 3, the character 'a' transforms into the next 3 consecutive characters ahead of it, which results in "bcd".
The transformation wraps around the alphabet if it exceeds 'z'. For example, if s[i] = 'y' and nums[24] = 3, the character 'y' transforms into the next 3 consecutive characters ahead of it, which results in "zab".
Return the length of the resulting string after exactly t transformations.

Since the answer may be very large, return it modulo 109 + 7.

 

Example 1:

Input: s = "abcyy", t = 2, nums = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2]

Output: 7

Explanation:

First Transformation (t = 1):

'a' becomes 'b' as nums[0] == 1
'b' becomes 'c' as nums[1] == 1
'c' becomes 'd' as nums[2] == 1
'y' becomes 'z' as nums[24] == 1
'y' becomes 'z' as nums[24] == 1
String after the first transformation: "bcdzz"
Second Transformation (t = 2):

'b' becomes 'c' as nums[1] == 1
'c' becomes 'd' as nums[2] == 1
'd' becomes 'e' as nums[3] == 1
'z' becomes 'ab' as nums[25] == 2
'z' becomes 'ab' as nums[25] == 2
String after the second transformation: "cdeabab"
Final Length of the string: The string is "cdeabab", which has 7 characters.

Example 2:

Input: s = "azbk", t = 1, nums = [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]

Output: 8

Explanation:

First Transformation (t = 1):

'a' becomes 'bc' as nums[0] == 2
'z' becomes 'ab' as nums[25] == 2
'b' becomes 'cd' as nums[1] == 2
'k' becomes 'lm' as nums[10] == 2
String after the first transformation: "bcabcdlm"
Final Length of the string: The string is "bcabcdlm", which has 8 characters.

 

Constraints:

1 <= s.length <= 105
s consists only of lowercase English letters.
1 <= t <= 109
nums.length == 26
1 <= nums[i] <= 25
Seen this question in a real interview before?
1/5
Yes
No
Accepted
4.4K
Submissions
13.1K
Acceptance Rate
33.5%
Topics
Hash Table
Math
String
Dynamic Programming
Counting
Companies
Hint 1
Model the problem as a matrix multiplication problem.
Hint 2
Use exponentiation to quickly multiply matrices.
''')
