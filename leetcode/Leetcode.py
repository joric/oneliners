#!/usr/bin/env python3

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
from heapq import *
from bisect import *
from random import *
from re import *
import collections
import bisect

class TreeNode(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

    def __repr__(root):
        q, res = [],[]
        q.append(root)
        while len(q):
            nodes = len(q)
            for _ in range(nodes):
                root = q.pop(0)
                res.append(root and root.val)
                if root:
                    q.append(root.left)
                    q.append(root.right)
        while res and res[-1] is None:
            res.pop()
        return str(res)

    def __eq__(a, b):
        return str(a)==str(b)

    def parse(x):
        nodes = [None if val==None else TreeNode(val) for val in x]
        kids = nodes[::-1]
        root = kids.pop()
        for node in nodes:
            if node:
                if kids: node.left  = kids.pop()
                if kids: node.right = kids.pop()
        return root

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        out = []
        while self:
            out.append(self.val)
            self = self.next
        return str(out)

    def __eq__(a, b):
        return str(a)==str(b)

    def parse(val):
        if len(val)==0:
            return None
        sub_nodes = ListNode.parse(val[1:])
        list_node = ListNode(val[0], sub_nodes)
        return list_node

def test(classname, text, init=None, check=None):
    import re

    def vp(s):
        return eval(s.replace('null','None').replace('true','True').replace('false','False'))

    def vc(func, vname, val):
        is_seq = lambda v: type(v) in (dict, tuple, set, Generator)
        to_list = lambda v: v if not is_seq(v) else [to_list(x) for x in v]
        tname = str(get_type_hints(func).get(vname, None))
        if 'ListNode' in tname and type(val)!=ListNode:
            val = ListNode.parse(val)
        elif 'TreeNode' in tname and type(val)!=TreeNode:
            val = TreeNode.parse(val)
        elif 'List' in tname or is_seq(val):
            val = to_list(val)
        return val

    def print_res(passed, res, expected, *args):
        c = lambda c,t,w=60: '\x1b[{1}m{2}\x1b[0m'.format(s:=str(t), 30+c, s[:w]+'...' if len(s)>=w else s)
        e = 2 if passed else 1
        print('%s args %s result %s expected %s' % (c(e,'PASSED' if passed else 'FAILED'), c(e,args), c(e,res), c(e,expected)))

    if not check:
        def check(res, expected, *args):
            return res==expected

    # Solution tests

    tests = []
    for s in text.splitlines():
        if s.startswith('Input:'):
            tests.append([[],[]])
            if m:=re.split(r'[\, ]*\w+ = ',s):
                for i in range(1, len(m)):
                    tests[-1][0].append(vp(m[i]))
        elif s.startswith('Output:'):
            tests[-1][1] = vp(s[8:])

    for args, expected in tests:
        func = getattr(classname(), dir(classname)[-1])
        argc = func.__code__.co_argcount - 1

        if init:
            (init)(*args[argc:])

        args = args[:argc]

        for i in range(argc):
            args[i] = vc(func, func.__code__.co_varnames[i+1], args[i])

        res = func(*args)
        res = vc(func, 'return', res)

        if type(expected) != type(res):
            res, expected = map(str, (res, expected))

        print_res(check(res, expected, *args), res, expected, *args)

    # Class implementation tests

    param = []
    state = 0
    for s in text.splitlines():
        if s=='Input':
            state = 1
        elif state == 1:
            param.append([[],[],[]])
            param[-1][0] = vp(s)
            state = 2
        elif state == 2:
            param[-1][1] = vp(s)
            state = 0
        elif s=='Output':
            state = 3
        elif state == 3:
            param[-1][2] = vp(s)
            state = 0

    for calls, args, expected in param:
        passed = True
        res = [None]
        instance = None
        for i in range(len(calls)):
            if calls[i] == type(classname()).__name__:
                instance = classname()
            else:
                func = getattr(instance, calls[i])
                r = func(*args[i])
                if type(r) is float:
                    r = round(r,5)
                res.append(r)

        passed = res == expected
        print_res(passed, res, expected, args)

