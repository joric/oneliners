from lc import *

# https://leetcode.com/problems/string-compression/discuss/1050976/A-two-line-Python3-groupby-solution

class Solution:
    def compress(self, chars: List[str]) -> int:
        return reduce(lambda i,c:(lambda s:setitem(chars,slice(i,i+len(s)), s) or i+len(s))(c[0]+str(('',c[1])[c[1]>1])),((c,sum(1 for _ in g)) for c,g in groupby(chars)),0)

class Solution:
    def compress(self, chars: List[str]) -> int:
        chars[:] = ''.join((lambda c,x:(c,c+str(x))[x>1])(c,len(list(g))) for c,g in groupby(chars))

# https://leetcode.com/problems/string-compression/solutions/92562/1-liner-by-stefanpochmann-tkst/

class Solution:
    def compress(self, c: List[str]) -> int:
        c[:]=re.sub(r'(?<=(.))\1+',lambda m:str(1+len(m.group())),''.join(c))

test('''
443. String Compression
Medium

2609

4697

Add to List

Share
Given an array of characters chars, compress it using the following algorithm:

Begin with an empty string s. For each group of consecutive repeating characters in chars:

If the group's length is 1, append the character to s.
Otherwise, append the character followed by the group's length.
The compressed string s should not be returned separately, but instead, be stored in the input character array chars. Note that group lengths that are 10 or longer will be split into multiple characters in chars.

After you are done modifying the input array, return the new length of the array.

You must write an algorithm that uses only constant extra space.

 

Example 1:

Input: chars = ["a","a","b","b","c","c","c"]
Output: ["a","2","b","2","c","3"]

//Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".
Example 2:

Input: chars = ["a"]
Output: ["a"]

//Output: Return 1, and the first character of the input array should be: ["a"]
Explanation: The only group is "a", which remains uncompressed since it's a single character.
Example 3:

Input: chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
Output: ["a","b","1","2"]

//Output: Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].
Explanation: The groups are "a" and "bbbbbbbbbbbb". This compresses to "ab12".
 

Constraints:

1 <= chars.length <= 2000
chars[i] is a lowercase English letter, uppercase English letter, digit, or symbol.

''', check=lambda res,exp,nums:nums[:res]==exp if res else nums==exp)
