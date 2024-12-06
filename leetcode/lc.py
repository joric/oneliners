# coding: utf-8
from string import *
from re import *
from datetime import *
from collections import *
from heapq import *
from bisect import *
from copy import *
from math import *
from random import *
from statistics import *
from itertools import *
from functools import *
from operator import *
from io import *
from sys import *
from json import *
from builtins import *

import string
import re
import datetime
import collections
import heapq
import bisect
import copy
import math
import random
import statistics
import itertools
import functools
import operator
import io
import sys
import json

from typing import *

class TreeNode:
    def __init__(self, x=0, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

    @staticmethod
    def dump(root):
        q = []
        res = []
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
        return res

    @staticmethod
    def serialize(root):
        return str(TreeNode.dump(root)).replace('None','null') if root else'[]'

    @staticmethod
    def deserialize(str):
        return TreeNode.parse(json.loads(str))

    @staticmethod
    def _array_to_tree_node(arr):
        return TreeNode.parse(arr)

    def _tree_node_to_array(self):
        return TreeNode.dump(self)

    def __repr__(self):
        return(f:=lambda x:x and f'TreeNode{{val: {x.val}, left: {f(x.left)}, right: {f(x.right)}}}'or 'None')(self)

    def __eq__(self, other):
        return self is other

    def __hash__(self):
        return hash(str(self))

    def parse(arr):
        if not arr:
            return None
        if type(arr) is int:
            return TreeNode(arr)
        nodes = [None if x is None else TreeNode(x) for x in arr]
        kids = nodes[::-1]
        root = kids and kids.pop()
        for node in nodes:
            if node:
                if kids:
                    node.left = kids.pop()
                if kids:
                    node.right = kids.pop()
        return root

class ListNode:
    def __init__(self, val=0, next=None):
        if type(val) is str: # see add-two-numbers, linked-list-cycle-ii
            try:
                self.__dict__ = ListNode.parse(json.loads('['+val+']')).__dict__
                return
            except:
                pass
        self.val = val
        self.next = next

    def dump(self):
        if self.has_cycle():
            return 'Error - Found cycle in the ListNode'
        out = []
        while self:
            out.append(self.val)
            self = self.next
        return out

    @staticmethod
    def serialize(root):
        return str(root.dump()).replace('None','null') if root else '[]';

    @staticmethod
    def deserialize(str):
        return ListNode.parse(json.loads(str))

    @staticmethod
    def _array_to_list_node(arr):
        return ListNode.parse(arr)

    def _list_node_to_array(self):
        return ListNode.dump(self)

    def __repr__(self):
        if self.has_cycle():
            return 'Error - Found cycle in the ListNode'
        return(f:=lambda x:x and f'ListNode{{val: {x.val}, next: {f(x.next)}}}'or 'None')(self)

    def __eq__(a, b):
        return a is b

    def parse(val):
        if not val:
            return None
        if type(val)==ListNode:
            return val
        val = [*val]
        sub_nodes = ListNode.parse(val[1:])
        list_node = ListNode(val[0], sub_nodes)
        return list_node

    def has_cycle(head):
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                break
        if not fast or not fast.next:
            return None
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow

cnames = []

# use test(```leetcode description```) to run latest Solution
# note only the last solution is tested (classname override), but you can use empty test() between solutions

def test(text=None, classname=None, check=None, init=None, custom=None, cast=None, sort=None, inplace=None):
    import importlib
    if not text:
        cname = classname or importlib.import_module('__main__').Solution
        cnames.append(cname)
        return

    def vc(func, name, v):
        tname = get_type_hints(func).get(name, None)

        if cast: # see 191.number-of-1-bits.py
            v = cast(name, v)
        else:
            wrapper = ''
            if '__args__' in dir(tname) and len(tname.__args__)>1:
                tname, wrapper = tname.__args__
            try:
                if 'deserialize' in dir(tname):
                    f = getattr(tname,'deserialize')
                    return f(v)
                v = json.loads(v)
                x = tname(v)
                if type(x) is float:
                    return round(x,5)
                return x
            except Exception as e:
                pass

        is_gen = lambda v: hasattr(v,'__iter__') and not hasattr(v,'__len__')
        is_iter = lambda v: type(v) in (tuple, set, list, dict,deque) or is_gen(v)
        to_list = lambda v: v if not is_iter(v) else [to_list(x) for x in v]

        hint = str(tname)
        if type(v) is str:
            return v # see linked-list-cycle-ii
        # unwrap some vars
        if 'List[lc.ListNode]' in hint or 'List[typing.Optional[lc.ListNode]]' in hint:
            return [ListNode.parse(x) for x in v]
        if 'List[lc.TreeNode]' in hint or 'List[typing.Optional[lc.TreeNode]]' in hint:
            return [TreeNode.parse(x) if type(x) is list else x for x in v]
        elif 'ListNode' in hint and type(v)!=ListNode:
            return ListNode.parse(v)
        elif 'TreeNode' in hint and type(v)!=TreeNode:
            return TreeNode.parse(v)
        elif type(v)==type({}.values()):
            return list(v)
        elif 'List' in hint or is_iter(v):
            return list(v) if type(v) is str else to_list(v)
        elif type(v) is float:
            return round(v, 5)
        elif type(v) is bool and hint==str(int):
            return v
        if t:=next((t for t in (str,bool,int) if hint==str(t)), None):
            return t(v) if v is not None else None if t is not bool else False
        return v

    def default_cast(args):
        out = []
        for x in args:
            try:
                x = json.loads(x)
            except:
                try:
                    x = int(x)
                except:
                    try:
                        x = float(x)
                    except:
                        pass
            out.append(x)
        return out

    def vcast(func, args, init=None):
        func = func.__wrapped__ if hasattr (func, '__wrapped__') else func
        if not hasattr(func,'__code__'):
            args = default_cast(args)
            return args, args, args

        # determine 'self', need for "minustwoliners" (unreliable)
        d = 0
        v = func.__code__.co_varnames
        if len(v)>0 and (v[0]=='self' or v[0]=='s'):
            d = 1

        argc = func.__code__.co_argcount - d
        orig = args

        if init:
            # init function (if exists) supposed to have all input vars, annotated
            args = [vc(init, init.__code__.co_varnames[i], x) for i,x in enumerate(args)]
        else:
            args = [vc(func, func.__code__.co_varnames[i+d], x) for i,x in enumerate(args[:argc])]

        return args[:argc], args, orig[:argc]

    def print_res(passed, res, expected, *args):
        g = lambda t:str(t.serialize(t) if type(t) is ListNode or type(t) is TreeNode  else t)
        c = lambda c,t,w=50: '\x1b[{1}m{2}\x1b[0m'.format(s:=g(t), 30+c, s[:w]+'...' if len(s)>=w else s)
        e = 2 if passed else 1
        print('%s args %s result %s expected %s' % (c(e,'PASSED' if passed else 'FAILED'), c(e,args), c(e,res), c(e,expected)))

    main = importlib.import_module('__main__')

    if not check and 'check' in dir(main):
        check  = main.check

    if not check:
        def check(res, expected, *args):
            t = type(res)
            if sort:
                return sorted(res or [])==sorted(expected or [])
            if inplace:
                a = args[0]
                if 'Node' in str(type(a)):
                    e = type(a).deserialize(expected)
                    return type(a).serialize(a)==type(a).serialize(e)
                if expected == '[]': expected = None # 114.flatten-binary-tree-to-linked-list.py
                return (a or [])==(expected or [])
            elif 'Node' in str(t):
                return t.serialize(res)==t.serialize(expected)
            elif res is None and expected is not None:
                return False
            elif t is list:
                return str(res)==str(expected)
            elif t is Counter:
                return set(res.keys())==set(expected)
            elif 'numpy.ndarray' in str(t):
                return all(x==y for x,y in zip(res,expected))
            elif type(expected) is list: # letter-combinations-of-a-phone-number
                return list(res)==expected
            elif type(expected) is str:
                return str(res)==expected
            else:
                return res==expected

    custom_class_tests = classname is not None and 'Launcher' not in str(classname) and custom!=False

    if not classname and 'Solution' in dir(main):
        classname = main.Solution

    if not init and 'init' in dir(main):
        init = main.init

    if 'Launcher' in dir(main):
        classname = main.Launcher

    cnames.append(classname)

    # Solution tests

    tests = []
    p,t = '',0
    def split_vars(s, prepend=', '):
        out = []
        if m:=re.split(r'\, [a-zA-Z_]+\d* =\s*', prepend+s):
            for i in range(len(m)):
                if m[i]:
                    out.append(m[i])
        return out

    exitcode = 0

    if not custom_class_tests:
        for s in text.splitlines():
            if s.startswith('Input:'):
                t = 1
                tests.append({'input':[],'output':[]})
                p += s[7:]
            elif s.startswith('Output:'):
                tests[-1]['input'] = split_vars(p)
                p,t = s[8:],2
            elif t==2 and(s=='' or any(s.startswith(t) for t in ('Exampl','Explan','Operat','Note','#'))):
                tests[-1]['output'] = split_vars(p, '')
                p,t = '',0
            elif t != 0:
                p += s

    for cname in cnames:
        passed, total = 0, len(tests)

        for t in tests:

            args = t['input']
            expected = t['output']

            func = getattr(cname(), [*filter(lambda s:not s.startswith('__'),dir(cname))][-1])

            args, iargs, orig = vcast(func, args, init)

            if init:
                init(*iargs)

            res = vc(func, 'return', func(*args))

            if len(expected)==1:
                expected = expected[0]

            if not inplace:
                expected = vc(func, 'return', expected)

            # leetcode does not convert bool result to int result since Aug 2023
            ok = False if type(res) in (float,bool) and type(expected)==int else check(res, expected, *args)

            if type(ok) is tuple: # see linked-list-cycle-ii (substitutes res with custom res)
                ok, res = ok[:2]

            print_res(ok, res, expected, *orig)
            passed += int(ok)

            exitcode |= 0 if ok else 1

        #if total: print('Passed %d/%d tests.' % (passed, total))

    # Custom class tests

    # NB! new test system seems incompatible,
    # i.e. "Input" has semicolon now.
    # so I detect by classname
    # also a case when Input/Output use a separate line

    param = []
    t = 0

    def vp(s):
        try:
            return json.loads(s)
        except Exception as e:
            return s

    if custom_class_tests:
        for s in text.splitlines():
            if s.startswith('Input'):
                param.append([[],[],[]])
                t = 1
                if len(s.rstrip(': '))>5:
                    param[-1][0] = vp(s[6:])
                    t = 2
            elif t == 1:
                param[-1][0] = vp(s)
                t = 2
            elif t == 2:
                param[-1][1] = vp(s)
                t = 0
            elif s.startswith('Output'):
                t = 3
                if len(s.rstrip(': '))>6:
                    param[-1][2] = vp(s[7:])
                    t = 0
            elif t == 3:
                param[-1][2] = vp(s)
                t = 0

    for methods, arglist, expected in param:
        results = []
        for name,args in zip(methods,arglist):
            if name not in dir(classname):
                func = getattr(classname, '__init__')
                args, iargs, orig = vcast(func, args, init)
                instance = classname(*args)
                results.append(None)
            else:
                func = getattr(instance, name)
                args, iargs, orig = vcast(func, args)
                res = vc(func, 'return', func(*args))
                results.append(res)

        ok = check(results,expected,*methods)
        print_res(ok, results, expected, methods, arglist)

        exitcode |= 0 if ok else 1

    exitcode and exit(exitcode)

import warnings
warnings.filterwarnings('ignore') 

if __name__ == "__main__":
    import os
    files = filter(lambda s:re.search(r'^([\d]+)\..*\.py$',s), os.listdir('.'))
    files = sorted(files, key=lambda s:[int(c) if c.isdigit() else c for c in re.split(r'(\d+)',s)])
    #sys.stdout = open(os.devnull, 'w')

    import subprocess

    for i, filename in enumerate(files):
        id = int(re.search(r'^([\d]+)', filename)[0])

        if id<88: continue
        #if i<=88: continue

        #print(f'[{i}/{len(files)}] \x1b[96m{filename}\x1b[0m')
        sys.stderr.write(f'\r[{i}/{len(files)}] {i*100//len(files)}%')

        with open(os.devnull, 'wb') as devnull:

            process = subprocess.Popen(['py', filename], stderr=subprocess.PIPE, stdout=subprocess.PIPE)
            stdout, stderr = process.communicate()
            exitcode = process.wait()

            if exitcode:
                #sys.stdout = sys.__stdout__
                #print(stdout, stderr, exitcode)

                print(f'\rTest failed in {filename}')

                sys.stdout.buffer.write(stdout)
                sys.stderr.buffer.write(stderr)

                exit(exitcode)
    print('\r\x1b[32mTests passed.')
