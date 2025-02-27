from lc import *

# https://leetcode.com/problems/count-vowels-permutation/discuss/1315077/Python-2-solution%3A-dp-and-matrix-power-explained

import numpy as np
class Solution:
    def countVowelPermutation(self, n): 
        def power(mat, n, M):
            res = np.eye(len(mat), dtype = int)
            while n > 0:
                if n%2:
                    res = np.dot(mat, res) % M
                mat = np.dot(mat, mat) % M
                n //= 2
            return res
        M = 10**9 + 7
        mat = np.matrix([[0,1,0,0,0], [1,0,1,0,0], [1,1,0,1,1], [0,0,1,0,1], [1,0,0,0,0]])
        return np.sum(power(mat, n-1, M)) % M

class Solution:
    def countVowelPermutation(self, n: int) -> int:
        a,e,i,o,u = [1]*5
        for _ in range(n-1):
            a,e,i,o,u=e+i+u,a+i,e+o,i,i+o
        return (a+e+i+o+u)%(10**9+7)

class Solution:
    def countVowelPermutation(self, n: int) -> int:
        x=[1]*5;[x:=[sum(x[j]for j in p)for p in[[1,2,4],[0,2],[1,3],[2],[2,3]]]for k in range(n-1)];return sum(x)%(10**9+7)

class Solution:
    def countVowelPermutation(self, n: int) -> int:
        x=[1]*5;[(x:=(x[1]+x[2]+x[4],x[0]+x[2],x[1]+x[3],x[2],x[2]+x[3]))for k in range(n-1)];return sum(x)%(10**9+7)

#python 2
#class Solution(object):
#    def countVowelPermutation(self, n):
#        return sum(reduce(lambda(a,e,i,o,u),_:(e+i+u,a+i,e+o,i,i+o),range(n-1),[1]*5))%(10**9+7)

class Solution:
    def countVowelPermutation(self, n: int) -> int:
        return sum(reduce(lambda x,_:(x[1]+x[2]+x[4],x[0]+x[2],x[1]+x[3],x[2],x[2]+x[3]),range(n-1),[1]*5))%(10**9+7)

class Solution:
    def countVowelPermutation(self, n: int) -> int:
        return sum(reduce(lambda x,_:(lambda a,e,i,o,u:(e+i+u,a+i,e+o,i,i+o))(*x),[0]*(n-1),[1]*5))%(10**9+7)

class Solution:
    def countVowelPermutation(self, n: int) -> int:
        s=[1]*5;[s:=(lambda a,e,i,o,u:[e+i+u,a+i,e+o,i,i+o])(*s)for _ in[0]*~-n];return sum(s)

test('''
1220. Count Vowels Permutation
Hard

2599

176

Add to List

Share
Given an integer n, your task is to count how many strings of length n can be formed under the following rules:

Each character is a lower case vowel ('a', 'e', 'i', 'o', 'u')
Each vowel 'a' may only be followed by an 'e'.
Each vowel 'e' may only be followed by an 'a' or an 'i'.
Each vowel 'i' may not be followed by another 'i'.
Each vowel 'o' may only be followed by an 'i' or a 'u'.
Each vowel 'u' may only be followed by an 'a'.
Since the answer may be too large, return it modulo 10^9 + 7.

 

Example 1:

Input: n = 1
Output: 5
Explanation: All possible strings are: "a", "e", "i" , "o" and "u".
Example 2:

Input: n = 2
Output: 10
Explanation: All possible strings are: "ae", "ea", "ei", "ia", "ie", "io", "iu", "oi", "ou" and "ua".
Example 3: 

Input: n = 5
Output: 68
 

Constraints:

1 <= n <= 2 * 10^4
''')