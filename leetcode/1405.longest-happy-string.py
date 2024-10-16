from lc import *

# https://leetcode.com/problems/longest-happy-string/discuss/3387714/Python-3-oror-6-lines-zip-strings-with-explanation-oror-TS%3A-99-99

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        (i,x), (j,y), (k,z) = sorted(((a,'a'),(b,'b'),(c,'c')))
        j+= i
        if k >= 2*j: r = ''.join([z,z,y]*j+[z] *min((k-2*j),2))
        elif k >= j: r = ''.join(chain(*zip([z*2]*(k-j)+ [z]*(2*j-k),[y]*(j))))
        else         : r = ''.join(chain(*zip([y*2]*(j-k)+ [y]*(2*k-j),[z]*(k))))
        return r.replace(y,x,i)

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        (i,x),(j,y),(k,z)=sorted(((a,'a'),(b,'b'),(c,'c')))
        j+=i
        v = [z,z,y]*j+[z]*min((k-2*j),2)
        w = chain(*zip([z*2]*(k-j)+[z]*(2*j-k),[y]*(j)))
        t = chain(*zip([y*2]*(j-k)+[y]*(2*k-j),[z]*(k)))
        return''.join((v,(w,t)[k<j])[k<2*j]).replace(y,x,i)

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        (i,x),(j,y),(k,z)=sorted(((a,'a'),(b,'b'),(c,'c')));j+=i;return''.join(([z,z,y]*j+[z]*min((k-2*j),2),(chain(*zip([z*2]*(k-j)+[z]*(2*j-k),[y]*(j))),chain(*zip([y*2]*(j-k)+[y]*(2*k-j),[z]*(k))))[k<j])[k<2*j]).replace(y,x,i)

# https://leetcode.com/problems/longest-happy-string/discuss/569902/Simple-and-short-python-code(16-ms-faster-than-92.72)

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        r,d='',{'a':a,'b':b,'c':c}
        for i in range(a+b+c):
            if d[t:=max(d,key=(lambda x:d[x]*(-1,1)[x!=r[-1]],d.get)[i<2 or r[-1]!=r[-2]])]:
                setitem(d,t,d[t]-1)
                r += t
            else:
                break
        return r

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        r,d='',{'a':a,'b':b,'c':c};all(d[t:=max(d,key=(lambda x:d[x]*(-1,1)[x!=t],d.get)[i<2 or t!=r[-2]])]and(setitem(d,t,d[t]-1),r:=r+t)for i in range(a+b+c));return r

# https://leetcode.com/problems/longest-happy-string/discuss/564277/C%2B%2BJava-a-greater-b-greater-c

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        return(f:=lambda a,b,c,x,y,z:[q:=a-(p:=min(2,a))>=b]and(f(b,a,c,y,x,z)if a<b else f(a,c,b,x,z,y)if b<c else x*p+y*q+f(a-p,b-q,c,x,y,z)if b else x*p))(a,b,c,*'abc')

# updated 2024-10-16 (POTD)

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        r,d='',{'a':a,'b':b,'c':c};all(d[t:=max(d,key=(lambda x:d[x]*(-1,1)[x!=t],d.get)[i<2 or t!=r[-2]])]and[exec('d[t]-=1'),r:=r+t]for i in range(a+b+c));return r

test('''
A string s is called happy if it satisfies the following conditions:

s only contains the letters 'a', 'b', and 'c'.
s does not contain any of "aaa", "bbb", or "ccc" as a substring.
s contains at most a occurrences of the letter 'a'.
s contains at most b occurrences of the letter 'b'.
s contains at most c occurrences of the letter 'c'.
Given three integers a, b, and c, return the longest possible happy string. If there are multiple longest happy strings, return any of them. If there is no such string, return the empty string "".

A substring is a contiguous sequence of characters within a string.

 

Example 1:

Input: a = 1, b = 1, c = 7
Output: "ccaccbcc"
Explanation: "ccbccacc" would also be a correct answer.
Example 2:

Input: a = 7, b = 1, c = 0
Output: "aabaa"
Explanation: It is the only correct answer in this case.

Constraints:

0 <= a, b, c <= 100
a + b + c > 0
Accepted
88,094
Submissions
153,131
''' #, check=lambda s,e,a,b,c: all(x not in s for x in ["aaa", "bbb", "ccc"])and s.count('a')<=a and s.count('b')<=b and s.count('c')<=c
)
