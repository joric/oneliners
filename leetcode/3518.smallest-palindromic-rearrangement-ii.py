from lc import *

# https://leetcode.com/problems/smallest-palindromic-rearrangement-ii/solutions/8414918/smallest-palindromic-rearrangement-ii-by-qww5/


class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        def comb(n: int, m: int, k_limit: int) -> int:
            res = 1
            m = min(m, n - m)

            for i in range(1, m + 1):
                res = res * (n - i + 1) // i
                if res > k_limit:
                    return k_limit + 1
            return res

        partition = len(s) // 2
        bucket = [0] * 26

        for i in range(partition):
            bucket[ord(s[i]) - 97] += 1

        def permutations(rem: int) -> int:
            ways = 1
            for i in range(26):
                if bucket[i] == 0:
                    continue

                ways *= comb(rem, bucket[i], k)
                if ways > k:
                    break
                rem -= bucket[i]
            return ways

        left_chars = []
        start_index = 1

        for pos in range(partition):
            for i in range(26):
                if bucket[i] == 0:
                    continue

                bucket[i] -= 1

                ways = permutations(partition - pos - 1)
                if start_index + ways > k:
                    left_chars.append(chr(i + 97))
                    break

                bucket[i] += 1
                start_index += ways

        if len(left_chars) < partition:
            return ""

        mid = s[partition] if len(s) % 2 != 0 else ""
        left_str = "".join(left_chars)
        right_str = left_str[::-1]

        return left_str + mid + right_str

class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        p=len(s)//2;b=[s[:p].count(chr(i))for i in range(97,123)];j=[1];a=[];c=lambda n,x:(f:=[1],any(setitem(f,0,f[0]*(n-i+1)//i)or f[0]>k for i in range(1,min(x,n-x)+1)),f[0])[2];m=lambda q,d:(w:=[1],v:=[q],any(x and(setitem(w,0,w[0]*c(v[0],x)),setitem(v,0,v[0]-x))[0]or w[0]>k for x in d),w[0])[3];[any(b[i]and[setitem(b,i,b[i]-1),w:=m(p-len(a)-1,b)]and(j[0]+w>k and(a.append(chr(i+97))or 1)or[setitem(b,i,b[i]+1),setitem(j,0,j[0]+w)]and 0)for i in range(26))for _ in range(p)];z="".join(a);return z+(s[p]if len(s)%2 else"")+z[::-1]if len(a)==p else""

class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        n=len(s)//2;c=Counter(s[:n]);t=factorial(n)//prod(map(factorial,c.values()));return''.join([]if k>t else(a:=[c.subtract(x:=next(j for j in sorted(c)if(q:=t*c[j]//(n-i))>=k or(k:=k-q)<0))or(t:=q)and x for i in range(n)])+[s[n:-n or 1]]+a[::-1])

test('''
3518. Smallest Palindromic Rearrangement II
Hard
Topics
premium lock icon
Companies
Hint
You are given a palindromic string s and an integer k.

Return the k-th lexicographically smallest palindromic permutation of s. If there are fewer than k distinct palindromic permutations, return an empty string.

Note: Different rearrangements that yield the same palindromic string are considered identical and are counted once.

 

Example 1:

Input: s = "abba", k = 2

Output: "baab"

Explanation:

The two distinct palindromic rearrangements of "abba" are "abba" and "baab".
Lexicographically, "abba" comes before "baab". Since k = 2, the output is "baab".
Example 2:

Input: s = "aa", k = 2

Output: ""

Explanation:

There is only one palindromic rearrangement: "aa".
The output is an empty string since k = 2 exceeds the number of possible rearrangements.
Example 3:

Input: s = "bacab", k = 1

Output: "abcba"

Explanation:

The two distinct palindromic rearrangements of "bacab" are "abcba" and "bacab".
Lexicographically, "abcba" comes before "bacab". Since k = 1, the output is "abcba".
 

Constraints:

1 <= s.length <= 104
s consists of lowercase English letters.
s is guaranteed to be palindromic.
1 <= k <= 106
 
Seen this question in a real interview before?
1/6
Yes
No
Accepted
6,406/42.8K
Acceptance Rate
15.0%
Topics
Senior Staff
Hash Table
Math
String
Combinatorics
Counting
Weekly Contest 445
icon
Companies
Hint 1
Only build floor(n / 2) characters (the rest are determined by symmetry).
Hint 2
Count character frequencies and use half the counts for construction.
Hint 3
Incrementally choose each character (from smallest to largest) and calculate how many valid arrangements result if that character is chosen at the current index.
Hint 4
If the count is at least k, fix that character; otherwise, subtract the count from k and try the next candidate.
Hint 5
Use combinatorics to compute the number of permutations at each step.
''')
