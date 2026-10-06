from lc import *

# https://leetcode.com/problems/remove-invalid-parentheses/solutions/75028/short-python-bfs-by-stefanpochmann-ld3m/?envType=daily-question&envId=2026-10-07

class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        level = {s}
        while True:
            valid = []
            for s in level:
                try:
                    eval('0,' + filter('()'.count, s).replace(')', '),'))
                    valid.append(s)
                except:
                    pass
            if valid:
                return valid
            level = {s[:i] + s[i+1:] for s in level for i in range(len(s))}

class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        def isvalid(s):
            ctr = 0
            for c in s:
                if c == '(':
                    ctr += 1
                elif c == ')':
                    ctr -= 1
                    if ctr < 0:
                        return False
            return ctr == 0
        level = {s}
        while True:
            valid = filter(isvalid, level)
            if valid:
                return valid
            level = {s[:i] + s[i+1:] for s in level for i in range(len(s))}

class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        def isvalid(s):
            try:
                eval('0,' + filter('()'.count, s).replace(')', '),'))
                return True
            except:
                pass
        level = {s}
        while True:
            valid = filter(isvalid, level)
            if valid:
                return valid
            level = {s[:i] + s[i+1:] for s in level for i in range(len(s))}


class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        def isvalid(s):
            s = filter('()'.count, s)
            while '()' in s:
                s = s.replace('()', '')
            return not s
        level = {s}
        while True:
            valid = filter(isvalid, level)
            if valid:
                return valid
            level = {s[:i] + s[i+1:] for s in level for i in range(len(s))}


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        l={s};return next(v for _ in count() if (v:=[x for x in l if reduce(lambda a,c:a+(c=='(')-(c==')')if a>=0 else a,x,0)==0]) or not (l:={x[:i]+x[i+1:] for x in l for i,_ in enumerate(x)}))

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        l=s,;return[v for _ in s*2if(v:=[x for x in l if reduce(lambda a,c:a<<(c<')')>>(c==')'),x,1)==1])or[l:={x[:i]+x[i+1:]for x in l for i in range(25)}]*0][0]

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        return(f:=lambda l:[x for x in l if(b:=1)and all((b:=b+(c<')')-(c==')'))for c in x)and b<2]or f({x[:i]+x[i+1:]for x in l for i in range(25)}))({s})

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        return(f:=lambda l:[x for x in l if reduce(lambda a,c:a and a+(c<')')-(c==')'),x,1)==1]or f({x[:i]+x[i+1:]for x in l for i in range(25)}))({s})

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        return(f:=lambda l:[x for x in l if reduce(lambda a,c:a<<(c<')')>>(c==')'),x,1)==1]or f({x[:i]+x[i+1:]for x in l for i in range(25)}))({s})

test('''
301. Remove Invalid Parentheses
Hard
Topics
premium lock icon
Companies
Hint
Given a string s that contains parentheses and letters, remove the minimum number of invalid parentheses to make the input string valid.

Return a list of unique strings that are valid with the minimum number of removals. You may return the answer in any order.

 

Example 1:

Input: s = "()())()"
Output: ["(())()","()()()"]
Example 2:

Input: s = "(a)())()"
Output: ["(a())()","(a)()()"]
Example 3:

Input: s = ")("
Output: [""]
 

Constraints:

1 <= s.length <= 25
s consists of lowercase English letters and parentheses '(' and ')'.
There will be at most 20 parentheses in s.
 
Seen this question in a real interview before?
1/6
Yes
No
Accepted
518,946/1M
Acceptance Rate
50.2%
Topics
String
Backtracking
Breadth-First Search
icon
Companies
Hint 1
Since we do not know which brackets can be removed, we try all the options! We can use recursion.
Hint 2
In the recursion, for each bracket, we can either use it or remove it.
Hint 3
Recursion will generate all the valid parentheses strings but we want the ones with the least number of parentheses deleted.
Hint 4
We can count the number of invalid brackets to be deleted and only generate the valid strings in the recusrion.
Similar Questions
Valid Parentheses
Easy
Minimum Number of Swaps to Make the String Balanced
Medium
''', sort=True)
