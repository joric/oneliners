#!/usr/bin/env python3

from typing import *
from collections import *
from functools import *
from heapq import *
from itertools import *
from math import *
from bisect import *
from random import *
from re import *
from operator import *
import bisect
import collections
import heapq
import itertools
import importlib
import json
import re
import os

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

    def parse(val):
        if not val:
            return None
        nodes = [None if x is None else TreeNode(x) for x in val]
        kids = nodes[::-1]
        root = kids and kids.pop()
        for node in nodes:
            if node:
                if kids:
                    node.left  = kids.pop()
                if kids:
                    node.right = kids.pop()
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
        if not val:
            return None
        sub_nodes = ListNode.parse(val[1:])
        list_node = ListNode(val[0], sub_nodes)
        return list_node

def test(text, classname=None, check=None, init=None):
    def vp(s):
        try:
            return json.loads(s)
        except:
            return s

    def vc(func, name, v):
        is_gen = lambda v: hasattr(v,'__iter__') and not hasattr(v,'__len__')
        is_iter = lambda v: type(v) in (tuple, set) or is_gen(v)
        to_list = lambda v: v if not is_iter(v) else [to_list(x) for x in v]
        hint = str(get_type_hints(func).get(name, None))
        if 'ListNode' in hint and type(v)!=ListNode:
            return ListNode.parse(v)
        elif 'TreeNode' in hint and type(v)!=TreeNode:
            return TreeNode.parse(v)
        elif 'List' in hint or is_iter(v):
            return to_list(v)
        elif type(v) is float:
            return round(v, 5)
        if t:=next((t for t in (str,int,bool) if hint==str(t)), None):
            return t(v) if v is not None else None if t is not bool else False
        return v

    def vcast(func, args, init=None):
        func = func.__wrapped__ if hasattr (func, '__wrapped__') else func
        d = 1 if 'self' in func.__code__.co_varnames else 0
        argc = func.__code__.co_argcount - d
        args, iargs = args[:argc], args[argc:]
        args = [vc(func, func.__code__.co_varnames[i+d], x) for i,x in enumerate(args)]
        if init:
            iargs = [vc(init, init.__code__.co_varnames[i], x) for i,x in enumerate(iargs)]
        return args, iargs

    def print_res(passed, res, expected, *args):
        c = lambda c,t,w=60: '\x1b[{1}m{2}\x1b[0m'.format(s:=str(t), 30+c, s[:w]+'...' if len(s)>=w else s)
        e = 2 if passed else 1
        print('%s args %s result %s expected %s' % (c(e,'PASSED' if passed else 'FAILED'), c(e,args), c(e,res), c(e,expected)))

    if not check:
        def check(res, expected, *args):
            return res==expected

    if not classname:
        classname = importlib.import_module('__main__').Solution

    # Solution tests

    tests = []
    p,t = '',0
    def split_vars(s):
        out = []
        if m:=re.split(r'[\, ]*\w+\s*=\s*',s):
            for i in range(len(m)):
                if m[i]:
                    out.append(m[i])
        return out


    for s in text.splitlines():
        if s.startswith('Input:'):
            t = 1
            tests.append({'input':[],'output':[]})
            p += s[7:]
        elif s.startswith('Output:'):
            tests[-1]['input'] = split_vars(p)
            tests[-1]['output'] = split_vars(s[8:])
            p,t = '',0
        elif t == 1:
            p += s

    for t in tests:
        args = tuple(map(vp, t['input']))
        expected = tuple(map(vp, t['output']))
        if len(expected)==1:
            expected = expected[0]

        func = getattr(classname(), dir(classname)[-1])
        args, iargs = vcast(func, args, init)

        if init:
            init(*iargs)


        res = vc(func, 'return', func(*args))
        passed = check(res, expected, *args)
        print_res(passed, res, expected, *args)

    # Custom class tests

    param = []
    t = 0
    for s in text.splitlines():
        if s=='Input':
            t = 1
        elif t == 1:
            param.append([[],[],[]])
            param[-1][0] = vp(s)
            t = 2
        elif t == 2:
            param[-1][1] = vp(s)
            t = 0
        elif s=='Output':
            t = 3
        elif t == 3:
            param[-1][2] = vp(s)
            t = 0

    for methods, arglist, expected in param:
        results = []
        for name,args in zip(methods,arglist):
            if name == classname.__name__:
                func = getattr(classname, '__init__')
                args, _ = vcast(func, args)
                instance = classname(*args)
                results.append(None)
            else:
                func = getattr(instance, name)
                args, _ = vcast(func, args)
                res = vc(func, 'return', func(*args))
                results.append(res)

        passed = results == expected
        print_res(passed, results, expected, arglist)

