from lc import *

# https://leetcode.com/problems/construct-smallest-number-from-di-string/solutions/6438131/2-line-code/?envType=daily-question&envId=2025

class Solution:
    def smallestNumber(self, pattern: str) -> str:
        for perm in permutations(map(str, range(1, len(pattern) + 2))):
            if all((p == 'I') == (a < b) for p, a, b in zip(pattern, perm, perm[1:])):
                return ''.join(perm)

class Solution:
    def smallestNumber(self, s: str) -> str:
        return next(''.join(p)for p in permutations(map(str,range(1,len(s)+2)))if all((c=='I')==(a<b)for c,a,b in zip(s,p,p[1:])))

class Solution:
    def smallestNumber(self, s: str) -> str:
        return next(''.join(p)for p in permutations('123456789'[:len(s)+1])if all((c>'D')==(a<b)for c,a,b in zip(s,p,p[1:])))

class Solution:
    def smallestNumber(self, s: str) -> str:
        return next(''.join(p)for p in permutations(digits[1:len(s)+2])if all((c>'D')==(a<b)for c,a,b in zip(s,p,p[1:])))

# https://leetcode.com/problems/construct-smallest-number-from-di-string/solutions/2422380/java-c-python-easy-reverse/?envType=daily-question&envId=2025-02-18

class Solution:
    def smallestNumber(self, s: str) -> str:
        res, stack = [], []
        for i,c in enumerate(s + 'I', 1):
            stack.append(str(i))
            if c == 'I':
                res += stack[::-1]
                stack = []
        return ''.join(res)

class Solution:
    def smallestNumber(self, s: str) -> str:
        q=[];return''.join(''.join((q[::-1],q:=[])[0])for i,c in enumerate(s+'I',1)if q.append(str(i))or'I'==c)

class Solution:
    def smallestNumber(self, s: str) -> str:
        r,p = [],[*'987654321']
        for k in map(len,s.split('I')):
            r += [p.pop()for _ in range(k+1)][::-1]
        return ''.join(r)

class Solution:
    def smallestNumber(self, s: str) -> str:
        r,p=[],[*'987654321'];[r:=r+[p.pop()for _ in range(k+1)][::-1]for k in map(len,s.split('I'))];return''.join(r)

class Solution:
    def smallestNumber(self, s: str) -> str:
        p=[*'987654321'];return''.join(''.join([p.pop()for _ in range(k+1)][::-1])for k in map(len,s.split('I')))

class Solution:
    def smallestNumber(self, s: str) -> str:
        res = []
        for i,c in enumerate(s + 'I', 1):
            if c == 'I':
                res += range(i, len(res), -1)
        return ''.join(map(str,res))

class Solution:
    def smallestNumber(self, s: str) -> str:
        r=[];[r:=r+[*range(i,len(r),-1)]for i,c in enumerate(s+'I',1)if'D'<c];return''.join(map(str,r))

class Solution:
    def smallestNumber(self, s: str) -> str:
        r='';[r:=r+''.join(map(str,range(i,len(r),-1)))for i,c in enumerate(s+'I',1)if'D'<c];return r

# https://leetcode.com/problems/construct-smallest-number-from-di-string/solutions/6435293/one-line-solution-o-n/?envType=daily-question&envId=2025

class Solution:
    def smallestNumber(self, p: str) -> str: 
        return ''.join(map(str,reduce(lambda a,i:a+[*range(i,len(a),-1)],(i for i,c in enumerate(p+'I',1) if c=='I'),[])))
        
class Solution:
    def smallestNumber(self, p: str) -> str:  
        return ''.join(map(str,reduce(lambda a,i:a+[*range(i,len(a),-1)],compress(count(1),map(eq,p+'I',repeat('I'))),[])))

class Solution:
    def smallestNumber(self, pattern: str) -> str:
        ans = []
        for i, ch in enumerate(pattern + 'I', start = 1):
            if ch == 'I':
                ans.extend(range(i, len(ans), -1))
        return ''.join(map(str, ans))

class Solution:
    def smallestNumber(self, s: str) -> str:
        r='';[r:=r+digits[i+1:len(r):-1]for i,c in enumerate(s+'I')if'D'<c];return r

test('''
2375. Construct Smallest Number From DI String
Medium
Topics
Companies
Hint
You are given a 0-indexed string pattern of length n consisting of the characters 'I' meaning increasing and 'D' meaning decreasing.

A 0-indexed string num of length n + 1 is created using the following conditions:

num consists of the digits '1' to '9', where each digit is used at most once.
If pattern[i] == 'I', then num[i] < num[i + 1].
If pattern[i] == 'D', then num[i] > num[i + 1].
Return the lexicographically smallest possible string num that meets the conditions.

 

Example 1:

Input: pattern = "IIIDIDDD"
Output: "123549876"
Explanation:
At indices 0, 1, 2, and 4 we must have that num[i] < num[i+1].
At indices 3, 5, 6, and 7 we must have that num[i] > num[i+1].
Some possible values of num are "245639871", "135749862", and "123849765".
It can be proven that "123549876" is the smallest possible num that meets the conditions.
Note that "123414321" is not possible because the digit '1' is used more than once.
Example 2:

Input: pattern = "DDD"
Output: "4321"
Explanation:
Some possible values of num are "9876", "7321", and "8742".
It can be proven that "4321" is the smallest possible num that meets the conditions.
 

Constraints:

1 <= pattern.length <= 8
pattern consists of only the letters 'I' and 'D'.
Seen this question in a real interview before?
1/5
Yes
No
Accepted
38.9K
Submissions
50.7K
Acceptance Rate
76.6%
Topics
String
Backtracking
Stack
Greedy
Companies
Hint 1
With the constraints, could we generate every possible string?
Hint 2
Yes we can. Now we just need to check if the string meets all the conditions.
Similar Questions
DI String Match
Easy
''')
