from lc import *

# https://leetcode.com/problems/fruit-into-baskets/discuss/282633/Easy-and-short-O(N)-O(1)-Python-with-explanation

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        b1, b2, b1N, b2N, b2NCons, maxPick = None, None, 0, 0, 0, 0
        for fruit in fruits:
            if fruit == b2:
                b2N, b2NCons = b2N + 1, b2NCons + 1
            elif fruit == b1:
                b1, b2, b1N, b2N, b2NCons = b2, b1, b2N, b1N+1, 1
            else:
                b1, b2, b1N, b2N, b2NCons = b2, fruit, b2NCons, 1, 1
            maxPick = max(maxPick, b1N+b2N)
        return maxPick

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        a,b,c,d,e,f = [0]*6
        for x in fruits:
            a,b,c,d,e = (a,b,c,d+1,e+1) if x==b else (b,a,d,c+1,1) if x==a else (b,x,e,1,1)
            f = max(f,c+d)
        return f

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        a,b,c,d,e,f = [0]*6
        for x in fruits:
            a,b,c,d,e,f = (a,b,c,d+1,e+1,max(f,c+d+1)) if x==b else (b,a,d,c+1,1,max(f,d+c+1)) if x==a else (b,x,e,1,1,max(f,e+1))
        return f

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        return reduce(lambda p,x:(lambda a,b,c,d,e,f,x:(a,b,c,d+1,e+1,max(f,c+d+1)) if x==b else (b,a,d,c+1,1,max(f,d+c+1)) if x==a else (b,x,e,1,1,max(f,e+1)))(*p,x),fruits,[0]*6)[-1]

# https://leetcode.com/problems/fruit-into-baskets/discuss/170740/JavaC%2B%2BPython-Sliding-Window-for-K-Elements

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        c, i = Counter(), 0
        for x in fruits:
            c[x] += 1
            if len(c) > 2:
                c[fruits[i]] -= 1
                if c[fruits[i]] == 0:
                    del c[fruits[i]]
                i += 1
        return len(fruits) - i

class Solution:
    def totalFruit(self, f: List[int]) -> int:
        return (c:=Counter(),i:=0,[(c.update({x}),len(c)>2 and (k:=f[i],i:=i+1,c.update({k:-1}),c[k]==0 and c.pop(k))) for x in f]) and len(f)-i

# POTD 2025-08-04

class Solution:
    def totalFruit(self, f: List[int]) -> int:
        c,i=Counter(),0;[(c.update({x}),2<len(c)and(k:=f[i],i:=i+1,c.update({k:-1}),0==c[k]and c.pop(k)))for x in f];return len(f)-i

test('''
904. Fruit Into Baskets
Medium

2076

155

Add to List

Share
You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer array fruits where fruits[i] is the type of fruit the ith tree produces.

You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:

You only have two baskets, and each basket can only hold a single type of fruit. There is no limit on the amount of fruit each basket can hold.
Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.
Once you reach a tree with fruit that cannot fit in your baskets, you must stop.
Given the integer array fruits, return the maximum number of fruits you can pick.

 

Example 1:

Input: fruits = [1,2,1]
Output: 3
Explanation: We can pick from all 3 trees.
Example 2:

Input: fruits = [0,1,2,2]
Output: 3
Explanation: We can pick from trees [1,2,2].
If we had started at the first tree, we would only pick from trees [0,1].
Example 3:

Input: fruits = [1,2,3,2,2]
Output: 4
Explanation: We can pick from trees [2,3,2,2].
If we had started at the first tree, we would only pick from trees [1,2].
 

Example 4:
Input: fruits = [3,3,3,1,2,1,1,2,3,3,4]
Output: 5

Constraints:

1 <= fruits.length <= 10^5
0 <= fruits[i] < fruits.length
''')
