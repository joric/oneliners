from lc import *

# https://leetcode.com/problems/all-oone-data-structure/discuss/1243531/Python-solution-beats-97.93

class AllOne:
    def __init__(self):
        self.myDict={}
    def inc(self, key: str) -> None:
        if key in self.myDict:
            self.myDict[key]=self.myDict[key]+1
        else:
            self.myDict[key]=1
    def dec(self, key: str) -> None:
        if self.myDict[key]>1:
            self.myDict[key]=self.myDict[key]-1
        else:
            self.myDict.pop(key)
    def getMaxKey(self) -> str:
        if len(self.myDict.values())==0:
            return ""
        else:
            maxVal=max(self.myDict.values())
            for key in self.myDict.keys():
                if self.myDict[key]==maxVal:
                    return key
    def getMinKey(self) -> str:
        if len(self.myDict.values())==0:
            return ""
        else:
            minVal=min(self.myDict.values())
            for key in self.myDict.keys():
                if self.myDict[key]==minVal:
                    return key

class AllOne(dict):
    def inc(s, k: str) -> None:
        setitem(s,k,1+s.get(k,0))
    def dec(s, k: str) -> None:
        setitem(s,k,s[k]-1)if s[k]>1 else s.pop(k)
    def g(s,p):
        return next((k for k in s.keys()if s[k]==m),m:=p(s.values(),default=''))
    def getMaxKey(s) -> str:
        return s.g(max)
    def getMinKey(s) -> str:
        return s.g(min)

class AllOne(Counter):
    def inc(s, k: str) -> None:
        s.update([k])
    def dec(s, k: str) -> None:
        isub(s,Counter([k]))
    def g(s,p):
        return p(s.keys(),key=s.get,default='')
    def getMaxKey(s) -> str:
        return s.g(max)
    def getMinKey(s) -> str:
        return s.g(min)

# MRO resolution issue
'''
AllOne=type('',(Counter,),{
    'inc':lambda s,k:s.update([k]),
    'dec':lambda s,k:isub(s,Counter([k])),
    'g':lambda s,p:p(s.keys(),key=s.get,default=''),
    'getMaxKey':lambda s:s.g(max),
    'getMinKey':lambda s:s.g(min),
})
'''

# this works
c,g=Counter,lambda s,p:p(s.keys(),key=s.get,default='');c.inc=lambda s,k:s.update([k]);c.dec=lambda s,k:isub(s,Counter([k]))and None;c.getMaxKey=lambda s:g(s,max);c.getMinKey=lambda s:g(s,min);AllOne=c

test('''
432. All O`one Data Structure
Hard

1587

176

Add to List

Share
Design a data structure to store the strings' count with the ability to return the strings with minimum and maximum counts.

Implement the AllOne class:

AllOne() Initializes the object of the data structure.
inc(String key) Increments the count of the string key by 1. If key does not exist in the data structure, insert it with count 1.
dec(String key) Decrements the count of the string key by 1. If the count of key is 0 after the decrement, remove it from the data structure. It is guaranteed that key exists in the data structure before the decrement.
getMaxKey() Returns one of the keys with the maximal count. If no element exists, return an empty string "".
getMinKey() Returns one of the keys with the minimum count. If no element exists, return an empty string "".
Note that each function must run in O(1) average time complexity.

 

Example 1:

Input
["AllOne", "inc", "inc", "getMaxKey", "getMinKey", "inc", "getMaxKey", "getMinKey"]
[[], ["hello"], ["hello"], [], [], ["leet"], [], []]
Output
[null, null, null, "hello", "hello", null, "hello", "leet"]

Explanation
AllOne allOne = new AllOne();
allOne.inc("hello");
allOne.inc("hello");
allOne.getMaxKey(); // return "hello"
allOne.getMinKey(); // return "hello"
allOne.inc("leet");
allOne.getMaxKey(); // return "hello"
allOne.getMinKey(); // return "leet"
 

Other examples:

Input
["AllOne","inc","inc","inc","inc","getMaxKey","inc","inc","inc","dec","inc","inc","inc","getMaxKey"]
[[],["hello"],["goodbye"],["hello"],["hello"],[],["leet"],["code"],["leet"],["hello"],["leet"],["code"],["code"],[]]
Output
[null,null,null,null,null,"hello",null,null,null,null,null,null,null,"leet"]

Input
["AllOne","inc","inc","inc","inc","inc","inc","dec", "dec","getMinKey","dec","getMaxKey","getMinKey"]
[[],["a"],["b"],["b"],["c"],["c"],["c"],["b"],["b"],[],["a"],[],[]]
Output
[null,null,null,null,null,null,null,null,null,"a",null,"c","c"]

Constraints:

1 <= key.length <= 10
key consists of lowercase English letters.
It is guaranteed that for each call to dec, key is existing in the data structure.
At most 5 * 104 calls will be made to inc, dec, getMaxKey, and getMinKey.
Accepted
87,190
Submissions
234,304
''', AllOne)
