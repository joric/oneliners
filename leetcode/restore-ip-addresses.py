from lc import *

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        return [".".join((s[:a],s[a:b],s[b:c],s[c:])) for a in range(1,4) for b in range(a+1,a+4) for c in range(b+1,b+4) if 0<len(s)-c<4 and all(int(x)<256 and str(int(x))==x for x in (s[:a],s[a:b],s[b:c],s[c:]))]

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        return [s[:i]+"."+s[i:j]+"."+s[j:k]+"."+s[k:] for i,j,k in combinations(range(1,len(s)),3) if (f:=lambda s:0<=int(s)<256 and str(int(s))==s)(s[:i]) and f(s[i:j]) and f(s[j:k]) and f(s[k:])]

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        return ('.'.join(m.groups()) for m in (re.fullmatch(p, s) for p in map(''.join,product(*[('(.)','([^0].)','(1..|2[0-4].|25[0-5])')]*4))) if m)

test('''

93. Restore IP Addresses
Medium

3348

668

Add to List

Share
A valid IP address consists of exactly four integers separated by single dots. Each integer is between 0 and 255 (inclusive) and cannot have leading zeros.

For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses, but "0.011.255.245", "192.168.1.312" and "192.168@1.1" are invalid IP addresses.
Given a string s containing only digits, return all possible valid IP addresses that can be formed by inserting dots into s. You are not allowed to reorder or remove any digits in s. You may return the valid IP addresses in any order.

 

Example 1:

Input: s = "25525511135"
Output: ["255.255.11.135","255.255.111.35"]
Example 2:

Input: s = "0000"
Output: ["0.0.0.0"]
Example 3:

Input: s = "101023"
Output: ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
 

Constraints:

1 <= s.length <= 20
s consists of digits only.

''')


