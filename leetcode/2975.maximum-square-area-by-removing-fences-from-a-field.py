from lc import *

# Q2. weekly-contest-377

# https://leetcode.com/problems/maximum-square-area-by-removing-fences-from-a-field/discuss/4449554/Simple-5-liner-Python-solution.-Find-difference

class Solution:
    def maximizeSquareArea(self, m: int, n: int, h_fences: List[int], v_fences: List[int]) -> int:
        h = sorted(h_fences + [1, m])
        v = sorted(v_fences + [1, n])
        dh = {h[i] - h[j] for i in range(len(h) - 1, 0, -1) for j in range(i)}
        dv = [v[i] - v[j] for i in range(len(v) - 1, 0, -1) for j in range(i)]
        ans = next((x for x in sorted(dv, reverse=True) if x in dh), -1)
        return ans ** 2 % (10**9 + 7) if ans != -1 else -1

# megurine (9th place)

class Solution:
    def maximizeSquareArea(self, m: int, n: int, a: List[int], b: List[int]) -> int:
        a = sorted(a+[1,m])
        b = sorted(b+[1,n])
        s = {abs(x-y) for x,y in combinations(a,2)}
        r = -1
        for x,y in combinations(b,2):
            c = abs(x-y)
            if c in s:
                r = max(c*c,r)
        return r % int(10**9+7) if r>0 else -1

class Solution:
    def maximizeSquareArea(self, m: int, n: int, a: List[int], b: List[int]) -> int:
        a,b=starmap(lambda v,t:{abs(x-y)for x,y in combinations(sorted(v+[1,t]),2)},((a,m),(b,n)));return b&a and max(b&a)**2%(10**9+7)or-1

# POTD 2026-01-16

class Solution:
    def maximizeSquareArea(self, m: int, n: int, a: List[int], b: List[int]) -> int:
        g=lambda v,t:{abs(x-y)for x,y in combinations(v+[1,t],2)};return(s:=g(a,m)&g(b,n))and max(s)**2%(10**9+7)or-1

class Solution:
    def maximizeSquareArea(self, m: int, n: int, a: List[int], b: List[int]) -> int:
        return max(and_(*[{abs(x-y)for x,y in combinations(v+[1,t],2)}for v,t in((a,m),(b,n))])|{0})**2%(10**9+7)or-1

class Solution:
    def maximizeSquareArea(self, m: int, n: int, a: List[int], b: List[int]) -> int:
        return max(and_(*[{abs(x-y)for x,y in combinations(k,2)}for k in(a+[1,m],b+[1,n])])|{0})**2%(10**9+7)or-1

class Solution:
    def maximizeSquareArea(self, m: int, n: int, a: List[int], b: List[int]) -> int:
        g=lambda v,t:{abs(x-y)for x,y in combinations(v+[1,t],2)};return max(g(a,m)&g(b,n)|{0})**2%(10**9+7)or-1

test('''
2975. Maximum Square Area by Removing Fences From a Field
User Accepted:2702
User Tried:6669
Total Accepted:2832
Total Submissions:23329
Difficulty:Medium
There is a large (m - 1) x (n - 1) rectangular field with corners at (1, 1) and (m, n) containing some horizontal and vertical fences given in arrays hFences and vFences respectively.

Horizontal fences are from the coordinates (hFences[i], 1) to (hFences[i], n) and vertical fences are from the coordinates (1, vFences[i]) to (m, vFences[i]).

Return the maximum area of a square field that can be formed by removing some fences (possibly none) or -1 if it is impossible to make a square field.

Since the answer may be large, return it modulo 109 + 7.

Note: The field is surrounded by two horizontal fences from the coordinates (1, 1) to (1, n) and (m, 1) to (m, n) and two vertical fences from the coordinates (1, 1) to (m, 1) and (1, n) to (m, n). These fences cannot be removed.

 

Example 1:



Input: m = 4, n = 3, hFences = [2,3], vFences = [2]
Output: 4
Explanation: Removing the horizontal fence at 2 and the vertical fence at 2 will give a square field of area 4.
Example 2:



Input: m = 6, n = 7, hFences = [2], vFences = [4]
Output: -1
Explanation: It can be proved that there is no way to create a square field by removing fences.

Example 3:
//Input: m = 160741, n = 111780, hFences = [78613,81826,110102,64828,124712,55384,7799,148552,89664,59549,694,16991,144819,86925,22889,150526,82079,64899,19595,155670,20718,78207,82556,44955,90901,32144,159075,139671,72015,78,118528,154071,63607,85673,160284,47934,96423,141987,134527,141893,40635,38673,155983,15778,109522,48843,83637,117702,126560,140940,126591,113993,53579,156704,82864,119405,127217,70546,41030,61966,114415,60,145211,32739,15522,840,59838,129924,142926,31555,117917,140567,72865,67282,54706,8959,110612,27433,152391,154534,134163,135853,13107,41084,48888,100147,137330,102747,106055,8118,53156,160495,58812,154742,80,9802,159662,20960,119037,17974,135446,26389,115019,56329,112484,11188,19288,8345,6957,70819,78295,158727,116821,140135,148859,17182,69750,154083,116846,132437,24314,66379,117578,42608,116317,140425,12721,21157,45983,120883,48005,96180,6122,61290,35803,79739,129030,125549,62831,48261,12540,29294,141203,36699,120854,86316,133604,105512,43215,131914,147315,62912,20277,121818,20990,79674,134615,69591,20893,154054,157457,139384,156387,31517,102403,56477,128658,78656,131041,104904,156985,44700,52337,123187,8671,74609,33063,124990,129947,13783,126451,150,23085,95684,25958,133659,67036,147991,51883,73561,95374,63709,88642,59317,88243,98730,57371,53561,37937,113168,34108,139149,5407,8029,116784,83695,117560,154885,136664,73875,43833,85860,31577,32956,51290,123916,153450,136759,15002,74359,26566,117204,137315,103275,134416,6855,22336,123335,46881,27319,34219,103216,89938,113343,96651,88976,44421,51210,56605,58453,140653,47143,159545,128842,64296,14351,150938,73642,80560], vFences = [100643,63096,21350,93743,12551,43306,90803,85174,24983,61244,53308,30443,44835,10752,6477,69326,8136,77941,38563,75698,28382,78298,100368,48360,89485,81869,70318,74543,59380,81596,31664,81719,74572,8268,40161,35085,88534,91756,4214,73649,110472,80015,95309,88284,110404,99064,20405,80082,56032,28301,28753,75004,89200,26040,15582,97489,102710,41422,82961,18995,109033,95640,62808,82060,76036,103970,107943,42832,14616,19430,102116,76477,11368,68432,89965,86502,41540,87663,92031,61089,63132,9236,88516,50368,67352,3265,61832,102,61965,10116,35418,54770,11258,64930,99269,93259,6029,22579,40937,28881,37035,51373,104436,85549,61323,73290,39229,23798,48712,44717,102423,85181,63586,68531,33982,40863,978,91569,45856,30870,106946,10748,88803,105088,92531,23463,50765,6260,6094,87001,7550,102568,2548,55151,18735,34589,528,67192,43022,24032,99113,56641,42219,82307,85331,54036,19967,105109,54464,39527,57681,15030,68007,106219,59013,70256,13852,68504,67586,12866,88058,86674,98026,110004,16061,80512,14258,96027,85618,1687,83198,58353,32371,19221,85797,37718,101382,87296,3533,87634,5245,107399,28021,109067,353,76709,12452,81526,57118,97405,97417,103690,76573,27834,24718,10323,14773,92407,18365,46967,90229,65205,36817,83831,82891,5894,27527,53866,85838,57660,27030,5673,94440,90461,59550,79176,75314,36768,14754,52745,23287,71314,52234,84236,8444,109507,75026,106738,62733,31450,55806,53568,49512,28851,64020,19433,107390,82039,102482,66827,51387,40783,43509,12726,63800,24800,20608,31222,71270,20224,77709,91076,75163,3089,50606,83454,110133,62826,90081,101909,94822,51053,63743,56722,63753,55349,102253,53428,97531,68825,108306,66138,49137,14988,3478,57236,101248,20602,100127,48318,10438,6434,32577,86167,26513,73827,24439,108966,68546,25047,48900,18367,36667,92078,88469,5836,96355,71684,61926,108736,79910,53265,48078,10830,8349,38344,61135,63323,110252,40477,12181,28875,48412,43868,66653,47705,71943,28968,12636,69434,24570,13353,41335,60472,71227,73473,3326,28035,40359,9120,91920,85307,8458,109712,49556,30894,11606,17637,23016,50426,48349,77732,94639,27863,51684]
//Output: 181536816


Constraints:

3 <= m, n <= 10^9
1 <= hFences.length, vFences.length <= 600
1 < hFences[i] < m
1 < vFences[i] < n
hFences and vFences are unique.
''')
