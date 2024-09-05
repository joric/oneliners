from lc import *

# https://leetcode.com/problems/number-of-atoms/discuss/140802/Python-20-lines-very-readable-simplest-and-shortest-solution-36-ms-beats-100/1642899

class Solution:
    def countOfAtoms(self, formula: str) -> str:
        dic, coeff, stack, elem, cnt, i = defaultdict(int), 1, [], '', 0, 0
        for c in formula[::-1]:
            if c.isdigit():
                cnt += int(c) * (10**i)
                i += 1
            elif c == ')':
                cnt = cnt or 1
                stack.append(cnt)
                coeff *= cnt
                i = cnt = 0
            elif c == '(':
                coeff //= stack.pop()
                i = cnt = 0
            elif c.isupper():
                elem += c
                dic[elem[::-1]] += (cnt or 1) * coeff
                elem = ''
                i = cnt = 0
            elif c.islower():
                elem += c
        return ''.join(k + str(v > 1 and v or '') for k, v in sorted(dic.items()))

class Solution:
    def countOfAtoms(self, a: str) -> str:
        d,k,q,e,t,i = defaultdict(int),1,[],'',0,0
        for c in a[::-1]:
            if c == ')':
                q.append(t or 1)
                k *= q[-1]
                i = t = 0
            elif c == '(':
                k //= q.pop()
                i = t = 0
            elif c.isupper():
                d[(e+c)[::-1]] += (t or 1)*k
                e = ''
                i = t = 0
            elif c.isdigit():
                t += int(c)*10**i
                i += 1
            elif c.islower():
                e += c
        return ''.join(k+('',str(v))[v>1]for k,v in sorted(d.items()))

class Solution:
    def countOfAtoms(self, a: str) -> str:
        d,q,p=defaultdict(int),[],[1,'',0,0]
        for c in a[::-1]:
            def f(c,k,e,t,i):
                if c == ')':      return q.append(t or 1)or(k*q[-1],e,0,0)
                elif c == '(':    return k//q.pop(),e,0,0
                elif c.isupper(): return setitem(d,w:=(e+c)[::-1],d[w]+(t or 1)*k)or(k,'',0,0)
                elif c.isdigit(): return k,e,t+int(c)*10**i,i+1
                elif c.islower(): return k,e+c,t,i
                return k,e,t,i
            p = f(c,*p)
        return ''.join(k+('',str(v))[v>1]for k,v in sorted(d.items()))

class Solution:
    def countOfAtoms(self, a: str) -> str:
        d,q,p=defaultdict(int),[],[1,'',0,0];[p:=(lambda c,k,e,t,i:q.append(t or 1)or(k*q[-1],e,0,0)if c==')'else(k//q.pop(),e,0,0)if c=='('else(setitem(d,w:=(e+c)[::-1],d[w]+(t or 1)*k)or(k,'',0,0))if c.isupper()else(k,e,t+int(c)*10**i,i+1)if c.isdigit()else(k,e+c,t,i)if c.islower()else(k,e,t,i))(c,*p)for c in a[::-1]];return''.join(k+('',str(v))[v>1]for k,v in sorted(d.items()))

class Solution:
    def countOfAtoms(self, a: str) -> str:
        d,q,p=Counter(),[],[1,'',0,0];[p:=(lambda c,k,e,t,i:c==')'and(q.append(t or 1)or(k*q[-1],e,0,0))or c=='('and(k//q.pop(),e,0,0)or c.isupper()and(setitem(d,w:=(e+c)[::-1],d[w]+(t or 1)*k)or(k,'',0,0))or c.isdigit()and(k,e,t+int(c)*10**i,i+1)or c.islower()and(k,e+c,t,i)or(k,e,t,i))(c,*p)for c in a[::-1]];return''.join(k+('',str(v))[v>1]for k,v in sorted(d.items()))

# https://leetcode.com/problems/number-of-atoms/discuss/109333/Neat-Python-with-Explanation-35ms

class Solution:
    def countOfAtoms(self, a: str) -> str:
        d=[*filter(lambda c:c,split(r'([A-Z]{1}[a-z]?|\(|\)|\d+)',a))]
        q,i,n= [Counter()],0,len(d)
        while i<n:
            t = d[i]
            if t == '(':
                q.append(Counter())
            else:
                c = 1
                j = i+1
                if j<n and d[j].isdigit():
                    c = int(d[j])
                    i = j
                m = q.pop()if t== ')'else{t:1}
                for k in m:
                    q[-1][k] += c*m[k]
            i+=1
        return''.join(k+('',str(v))[v>1]for k,v in sorted(q[-1].items()))

class Solution:
    def countOfAtoms(self, a: str) -> str:
        d,q=re.findall(r'[A-Z][a-z]?|\(|\)|\d+',a),[Counter()];(f:=lambda i:d[i:]and(t:=d[i],q.append(Counter())if t=='('else(c:=1,d[(j:=i+1):]and d[j].isdigit()and(c:=int(d[j]),i:=j),[setitem(q[-1],k,q[-1][k]+c*v)for k,v in(q.pop()if t== ')'else{t:1}).items()]),f(i+1)))(0);return''.join(k+('',str(v))[v>1]for k,v in sorted(q[-1].items()))

# https://leetcode.com/problems/number-of-atoms/discuss/5475322/one-line-solution/

class Solution:
    def countOfAtoms(self, s: str) -> str:
        p = r'([A-Z][a-z]*)(\d*)'
        f = lambda m:re.sub(p,lambda g:g[1]+str(int(g[2]or 1)*int(m[2]or 1)),m[1])
        while '(' in s:
            s = re.sub('\((\w+)\)(\d*)', f, s)
        c = sum((Counter({m[1]:int(m[2]or 1)}) for m in finditer(p,s)), Counter())
        return ''.join(e + str(c)*(c>1) for e,c in sorted(c.items()))

class Solution:
    def countOfAtoms(self, s: str) -> str:
        p='([A-Z][a-z]*)(\d*)';[s:=re.sub('\((\w+)\)(\d*)',lambda m:re.sub(p,lambda g:g[1]+str(int(g[2]or 1)*int(m[2]or 1)),m[1]),s)for _ in s];return''.join(e+str(c)*(c>1)for e,c in sorted(sum((Counter({m[1]:int(m[2]or 1)})for m in finditer(p,s)),Counter()).items()))

test('''
726. Number of Atoms
Hard

1324

303

Add to List

Share
Given a string formula representing a chemical formula, return the count of each atom.

The atomic element always starts with an uppercase character, then zero or more lowercase letters, representing the name.

One or more digits representing that element's count may follow if the count is greater than 1. If the count is 1, no digits will follow.

For example, "H2O" and "H2O2" are possible, but "H1O2" is impossible.
Two formulas are concatenated together to produce another formula.

For example, "H2O2He3Mg4" is also a formula.
A formula placed in parentheses, and a count (optionally added) is also a formula.

For example, "(H2O2)" and "(H2O2)3" are formulas.
Return the count of all elements as a string in the following form: the first name (in sorted order), followed by its count (if that count is more than 1), followed by the second name (in sorted order), followed by its count (if that count is more than 1), and so on.

The test cases are generated so that all the values in the output fit in a 32-bit integer.

 

Example 1:

Input: formula = "H2O"
Output: "H2O"
Explanation: The count of elements are {'H': 2, 'O': 1}.
Example 2:

Input: formula = "Mg(OH)2"
Output: "H2MgO2"
Explanation: The count of elements are {'H': 2, 'Mg': 1, 'O': 2}.
Example 3:

Input: formula = "K4(ON(SO3)2)2"
Output: "K4N2O14S4"
Explanation: The count of elements are {'K': 4, 'N': 2, 'O': 14, 'S': 4}.
 

Other examples:

Input: formula = "Mg(H2O)N"
Output: "H2MgNO"

Constraints:

1 <= formula.length <= 1000
formula consists of English letters, digits, '(', and ')'.
formula is always valid.
Accepted
65,568
Submissions
120,478
''')