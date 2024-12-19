from lc import *

# https://leetcode.com/problems/construct-string-with-repeat-limit/discuss/1926919/Easy-Python-with-explanation

class Solution:
    def repeatLimitedString(self, s: str, repeat_limit: int) -> str:
        counter = collections.Counter(s)
        res = ""
        is_only_one = False
        chars = sorted(set(s), reverse=True)
        i = 0
        while i < len(chars):
            char = chars[i]
            if counter[char]:
                if is_only_one:
                    res += char
                    counter[char] -= 1
                    is_only_one = False
                    i = 0
                    continue
                else:
                    need = min(counter[char], repeat_limit)
                    res += char * need
                    counter[char] -= need
                    if counter[char]:
                        is_only_one = True
            i += 1
        return res


# https://leetcode.com/problems/construct-string-with-repeat-limit/discuss/1785008/3-Liner-Python-Solution

class Solution:
    def repeatLimitedString(self, s: str, k: int) -> str:
        c=p=0
        r=[]
        h=[]
        a = iter(sorted(s)[::-1])
        while x := (h.pop() if c <= k and h else next(a,0)):
            c = 1 if x != p else c+1
            if c <= k:
                r.append(x)
            else:
                h.append(x)
            p = x
        return ''.join(r)

class Solution:
    def repeatLimitedString(self, s: str, k: int) -> str:
        a,r,h=iter(sorted(s)[::-1]),[],[]
        def f(c,p):
            if x:=h.pop()if c<=k and h else next(a,0):
                c = (c+1,1)[x!=p]
                if c <= k:
                    r.append(x)
                else:
                    h.append(x)
                p = x
                f(c,p)
        f(0,0)
        return''.join(r)

class Solution:
    def repeatLimitedString(self, s: str, k: int) -> str:
        a,r,h=iter(sorted(s)[::-1]),[],[];(f:=lambda c,p:(x:=h.pop()if c<=k and h else next(a,0))and(r.append(x)if k>=(c:=(c+1,1)[x!=p])else h.append(x),f(c,x)))(0,0);return''.join(r)

test('''
2182. Construct String With Repeat Limit
Medium

800

57

Add to List

Share
You are given a string s and an integer repeatLimit. Construct a new string repeatLimitedString using the characters of s such that no letter appears more than repeatLimit times in a row. You do not have to use all characters from s.

Return the lexicographically largest repeatLimitedString possible.

A string a is lexicographically larger than a string b if in the first position where a and b differ, string a has a letter that appears later in the alphabet than the corresponding letter in b. If the first min(a.length, b.length) characters do not differ, then the longer string is the lexicographically larger one.

 

Example 1:

Input: s = "cczazcc", repeatLimit = 3
Output: "zzcccac"
Explanation: We use all of the characters from s to construct the repeatLimitedString "zzcccac".
The letter 'a' appears at most 1 time in a row.
The letter 'c' appears at most 3 times in a row.
The letter 'z' appears at most 2 times in a row.
Hence, no letter appears more than repeatLimit times in a row and the string is a valid repeatLimitedString.
The string is the lexicographically largest repeatLimitedString possible so we return "zzcccac".
Note that the string "zzcccca" is lexicographically larger but the letter 'c' appears more than 3 times in a row, so it is not a valid repeatLimitedString.
Example 2:

Input: s = "aababab", repeatLimit = 2
Output: "bbabaa"
Explanation: We use only some of the characters from s to construct the repeatLimitedString "bbabaa". 
The letter 'a' appears at most 2 times in a row.
The letter 'b' appears at most 2 times in a row.
Hence, no letter appears more than repeatLimit times in a row and the string is a valid repeatLimitedString.
The string is the lexicographically largest repeatLimitedString possible so we return "bbabaa".
Note that the string "bbabaaa" is lexicographically larger but the letter 'a' appears more than 2 times in a row, so it is not a valid repeatLimitedString.
 

Constraints:

1 <= repeatLimit <= s.length <= 105
s consists of lowercase English letters.
Accepted
44,409
Submissions
70,065
''')
