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
''')
