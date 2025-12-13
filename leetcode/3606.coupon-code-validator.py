from lc import *

# https://leetcode.com/problems/coupon-code-validator/solutions/6984863/python-one-line-solution-by-redberry33-6pdl/?envType=daily-question&envId=2025-12-13

class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        return [finalItem[0] for finalItem in sorted([item for item in list(zip(code,businessLine,isActive)) if item[2] and re.fullmatch(r"[a-zA-Z0-9_]+", item[0]) and item[1] in ["electronics", "grocery", "pharmacy", "restaurant"]], key=lambda x: (x[1], x[0]))]

class Solution:
    def validateCoupons(self, c: List[str], b: List[str], a: List[bool]) -> List[str]:
        return[x for x,y,_ in sorted(((x,y,z)for x,y,z in zip(c,b,a)if z and re.fullmatch(r'\w+',x)and y[0]in'egpr'),key=lambda t:(t[1],t[0]))]

class Solution:
    def validateCoupons(self, c: List[str], b: List[str], a: List[bool]) -> List[str]:
        return[x for _,x in sorted((y,x)for x,y,z in zip(c,b,a)if z and re.fullmatch(r'\w+',x)and y[0]in'egpr')]

class Solution:
    def validateCoupons(self, c: List[str], b: List[str], a: List[bool]) -> List[str]:
        return[x for _,x in sorted((y,x)for x,y,z in zip(c,b,a)if z and match(r'\w+$',x)and y[0]in'egpr')]

class Solution:
    def validateCoupons(self, c: List[str], b: List[str], a: List[bool]) -> List[str]:
        return[x for y,x,z in sorted(zip(b,c,a))if z and match(r'\w+$',x)and y[0]in'egpr']

class Solution:
    def validateCoupons(self, c: List[str], b: List[str], a: List[bool]) -> List[str]:
        return[y for x,y,z in sorted(zip(b,c,a))if z and match('\w+$',y)and x[0]in'egpr']

test('''
3606. Coupon Code Validator
Easy
Topics
premium lock icon
Companies
Hint
You are given three arrays of length n that describe the properties of n coupons: code, businessLine, and isActive. The ith coupon has:

code[i]: a string representing the coupon identifier.
businessLine[i]: a string denoting the business category of the coupon.
isActive[i]: a boolean indicating whether the coupon is currently active.
A coupon is considered valid if all of the following conditions hold:

code[i] is non-empty and consists only of alphanumeric characters (a-z, A-Z, 0-9) and underscores (_).
businessLine[i] is one of the following four categories: "electronics", "grocery", "pharmacy", "restaurant".
isActive[i] is true.
Return an array of the codes of all valid coupons, sorted first by their businessLine in the order: "electronics", "grocery", "pharmacy", "restaurant", and then by code in lexicographical (ascending) order within each category.

 

Example 1:

Input: code = ["SAVE20","","PHARMA5","SAVE@20"], businessLine = ["restaurant","grocery","pharmacy","restaurant"], isActive = [true,true,true,true]

Output: ["PHARMA5","SAVE20"]

Explanation:

First coupon is valid.
Second coupon has empty code (invalid).
Third coupon is valid.
Fourth coupon has special character @ (invalid).
Example 2:

Input: code = ["GROCERY15","ELECTRONICS_50","DISCOUNT10"], businessLine = ["grocery","electronics","invalid"], isActive = [false,true,true]

Output: ["ELECTRONICS_50"]

Explanation:

First coupon is inactive (invalid).
Second coupon is valid.
Third coupon has invalid business line (invalid).
 

Other examples:

Input: code = ["1OFw","0MvB"], businessLine = ["electronics","pharmacy"], isActive = [true,true]
Output: ["1OFw","0MvB"]

Constraints:

n == code.length == businessLine.length == isActive.length
1 <= n <= 100
0 <= code[i].length, businessLine[i].length <= 100
code[i] and businessLine[i] consist of printable ASCII characters.
isActive[i] is either true or false.
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
35,913/66.9K
Acceptance Rate
53.7%
Topics
Array
Hash Table
String
Sorting
Weekly Contest 457
icon
Companies
Hint 1
Filter out any coupon where isActive[i] is false, code[i] is empty or contains non‑alphanumeric/underscore chars, or businessLine[i] is not in the allowed set
Hint 2
Store each remaining coupon as a pair (businessLine[i], code[i])
Hint 3
Define a priority map, e.g. {"electronics":0, "grocery":1, "pharmacy":2, "restaurant":3}
Hint 4
Sort the list of pairs by (priority[businessLine], code) and return the code values in order
''')
