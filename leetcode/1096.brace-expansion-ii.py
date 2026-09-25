from lc import *

# https://leetcode.com/problems/brace-expansion-ii/solutions/1257748/python3-recursive-solution-by-ye15-9aa6/?envType=daily-question&envId=2026-09-25

class Solution:
    def braceExpansionII(self, e: str) -> List[str]:
        m,s={},[]
        for i,x in enumerate(e):
            if x=='{':s+=[i]
            if x=='}':m[s.pop()]=i
        def f(l,h):
            a=[['']]
            if l+1<h:
                i=l
                while i<h:
                    x=e[i]
                    if x==',':a+=[['']]
                    else:
                        y,i=(f(i+1,m[i]),m[i])if x=='{'else(x,i)
                        a+=[[u+v for u in a.pop() for v in y]]
                    i+=1
            return sorted({u for b in a for u in b})
        return f(0,len(e))

class Solution:
    def braceExpansionII(self, e: str) -> List[str]:
        q=['{'+e+'}'];a=set();[q.extend(s[:l]+w+s[r+1:]for w in s[l+1:r].split(','))if~(l:=s[:(r:=s.find('}'))].rfind('{'))else a.add(s)for s in q];return sorted(a)

# https://leetcode.com/problems/brace-expansion-ii/solutions/322002/python3-concise-iterative-solution-using-yw76/?envType=daily-question&envId=2026-09-25

class Solution:
    def braceExpansionII(self, expression: str) -> List[str]:
        stack,res,cur=[],[],[]
        for i in range(len(expression)):
            v=expression[i]
            if v.isalpha():
                cur=[c+v for c in cur or ['']]
            elif v=='{':
                stack.append(res)
                stack.append(cur)
                res,cur=[],[]
            elif v=='}':
                pre=stack.pop()
                preRes=stack.pop()
                cur=[p+c for c in res+cur for p in pre or ['']]
                res=preRes
            elif v==',':
                res+=cur
                cur=[]
        return sorted(set(res+cur))

class Solution:
    def braceExpansionII(self, e:str)->List[str]:
        return sorted({r for t in m[1].split(',')for r in self.braceExpansionII(m[0]+t+m[2])}if(m:=split('{([^{}]*)}',e,1))[1:]else{*e.split(',')})

class Solution:
    def braceExpansionII(self, e:str)->List[str]:
        return(f:=lambda e:sorted({r for t in m[1].split(',')for r in f(m[0]+t+m[2])}if(m:=split('{([^{}]*)}',e,1))[1:]else{*e.split(',')}))(e)

class Solution:
    def braceExpansionII(self, e:str)->List[str]:
        s=split;f=lambda e:sum([f(m[0]+t+m[2])for t in s(',',m[1])],[])if(m:=s('{([^{}]*)}',e,1))[1:]else s(',',e);return sorted({*f(e)})

class Solution:
    def braceExpansionII(self, e:str)->List[str]:
        f=lambda e:sum([f(m[0]+t+m[2])for t in split(',',m[1])],[])if(m:=split('{([^{}]*)}',e,1))[1:]else m;return sorted({*f(e)})

test('''
1096. Brace Expansion II
Hard
Topics
premium lock icon
Companies
Hint
Under the grammar given below, strings can represent a set of lowercase words. Let R(expr) denote the set of words the expression represents.

The grammar can best be understood through simple examples:

Single letters represent a singleton set containing that word.
R("a") = {"a"}
R("w") = {"w"}
When we take a comma-delimited list of two or more expressions, we take the union of possibilities.
R("{a,b,c}") = {"a","b","c"}
R("{{a,b},{b,c}}") = {"a","b","c"} (notice the final set only contains each word at most once)
When we concatenate two expressions, we take the set of possible concatenations between two words where the first word comes from the first expression and the second word comes from the second expression.
R("{a,b}{c,d}") = {"ac","ad","bc","bd"}
R("a{b,c}{d,e}f{g,h}") = {"abdfg", "abdfh", "abefg", "abefh", "acdfg", "acdfh", "acefg", "acefh"}
Formally, the three rules for our grammar:

For every lowercase letter x, we have R(x) = {x}.
For expressions e1, e2, ... , ek with k >= 2, we have R({e1, e2, ...}) = R(e1) ∪ R(e2) ∪ ...
For expressions e1 and e2, we have R(e1 + e2) = {a + b for (a, b) in R(e1) × R(e2)}, where + denotes concatenation, and × denotes the cartesian product.
Given an expression representing a set of words under the given grammar, return the sorted list of words that the expression represents.

 

Example 1:

Input: expression = "{a,b}{c,{d,e}}"
Output: ["ac","ad","ae","bc","bd","be"]
Example 2:

Input: expression = "{{a,z},a{b,c},{ab,z}}"
Output: ["a","ab","ac","z"]
Explanation: Each distinct word is written only once in the final answer.
 

Constraints:

1 <= expression.length <= 60
expression[i] consists of '{', '}', ','or lowercase English letters.
The given expression represents a set of words based on the grammar given in the description.
 
Seen this question in a real interview before?
1/6
Yes
No
Accepted
30,862/48.1K
Acceptance Rate
64.1%
Topics
Principal
Hash Table
String
Backtracking
Stack
Breadth-First Search
Sorting
Weekly Contest 142
icon
Companies
Hint 1
You can write helper methods to parse the next "chunk" of the expression. If you see eg. "a", the answer is just the set {a}. If you see "{", you parse until you complete the "}" (the number of { and } seen are equal) and that becomes a chunk that you find where the appropriate commas are, and parse each individual expression between the commas.
Similar Questions
Brace Expansion
Medium
''')
