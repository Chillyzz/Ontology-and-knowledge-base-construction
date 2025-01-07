from typing import List, Tuple
from sympy import Symbol
import sympy as sp
import re

from .evaluate import parse_annotation
from .evaluatep import cmp_question

## ===== Functions for Logical comparison =====  
def remove_parentheses(expression:str) -> str:
    """remove parentheses of both side"""
    return re.sub(r'^\((.*)\)$', r'\1', expression)

def check_string_equal(string1:str, string2:str) -> bool:
    """
    Check if two strings are equal, regardless of whether the letters are of different capital and extra spaces.
    """
    str1_no_spaces = string1.replace(" ", "")
    str2_no_spaces = string2.replace(" ", "")
    return str1_no_spaces.lower() == str2_no_spaces.lower()

def check_simple_expression_equal(expr1:str, expr2:str) -> bool:
    """
    Check if two simple expressions without = are equal, regardless of the order of the variables.
    """
    if '?' in expr1 or '?' in expr2:
        return check_string_equal(expr1, expr2)

    expr1_sympy = sp.sympify(expr1.lower())
    expr2_sympy = sp.sympify(expr2.lower())
    
    simplified_expr1 = sp.simplify(expr1_sympy)
    simplified_expr2 = sp.simplify(expr2_sympy)

    return simplified_expr1 == simplified_expr2 
  
def check_expression_equal(expr1:str, expr2:str) -> bool:
    """
    Check if two expressions are equal, regardless of the order of the variables.
    """
    exp1 = remove_parentheses(expr1)
    exp2 = remove_parentheses(expr2)
    l_exp1 = exp1[:get_equation_type(exp1)].strip() if get_equation_type(exp1) != -1 else exp1
    l_exp2 = exp2[:get_equation_type(exp2)].strip() if get_equation_type(exp2) != -1 else exp2
    r_exp1 = exp1[get_equation_type(exp1)+1:].strip() if get_equation_type(exp1) != -1 else exp1
    r_exp2 = exp2[get_equation_type(exp2)+1:].strip() if get_equation_type(exp2) != -1 else exp2
    
    if check_simple_expression_equal(l_exp1, l_exp2) and check_simple_expression_equal(r_exp1, r_exp2):
        return True
    elif check_simple_expression_equal(l_exp1, r_exp2) and check_simple_expression_equal(r_exp1, l_exp2):
        return True
    return False



class TreeNode:
    def __init__(self, data, location = 0):
        self.data = data
        self.children = []
        self.location = location

    def add_child(self, child_node):
        self.children.append(child_node)

    def remove_child(self, child_node):
        self.children = [child for child in self.children if child is not child_node]

    def traverse(self):
        print(self.data)
        if len(self.children) > 0:
            for child in self.children:
                child.traverse()

class DisjointSet:
    def __init__(self):
        self.parent = []
        self.rank = []
        self.ele = []

    def ind(self, index):
        """return the element of a given index"""
        return self.ele[index]

    def store(self, element):
        """return the index of an element"""
        for i in range(len(self.ele)):
            if self.ele[i] == element or is_equal_tree(self.ele[i], element,None,None):
                return i
        return -1

    def add(self, element):
        """add new element"""
        index = len(self.parent)
        self.parent.append(index)
        self.rank.append(0)
        self.ele.append(element)
        return index

    def find_head(self, element):
        """return the root element"""
        tmp = self.store(element)
        if tmp == -1:
            return element
        else:
            return self.ind(self.find_ind(tmp))

    def find_ind(self, index):
        """return the root index of the element"""
        x = index
        if self.parent[x] != x:
            self.parent[x] = self.find_ind(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        """union"""
        rootX = self.find_ind(self.store(x))
        rootY = self.find_ind(self.store(y))

        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1

    def add_annotation(self, annotation:list):
        """
        add annotation to trees
        """
        for i in range(len(annotation)):
            if (tmp := get_colon_place(annotation[i])) != -1:
                a = maketree(annotation[i].split(':')[0].strip())
                #b = maketree(annotation[i].split(':')[1].strip())
                self.add(a)
                #self.add(b)
                #self.union(a, b)
            elif (tmp := get_equation_type(annotation[i])) != -1:
                a = maketree(annotation[i][:tmp].strip())
                b = maketree(annotation[i][tmp+1:].strip())
                self.add(a)
                self.add(b)
                self.union(b, a)
            else:
                pass

    def find_child(self, element) -> list:
        """
        find all children of a node
        """
        index = self.store(element)
        if index == -1:
            return []
        res = []
        for i in range(len(self.parent)):
            if self.find_ind(i) == index:
                res.append(self.ind(i))
        return res

def is_equal_tree(node1, node2, ds1, ds2):
    """whether 2 trees have same head and logical equal child"""
    if not check_string_equal(node1.data,node2.data):
        return False
    node1.children.sort(key=lambda x: x.location)
    node2.children.sort(key=lambda x: x.location)
    if len(node1.children) != len(node2.children):
        return False
    for i in range(len(node1.children)):
        if not is_logical_equal(node1.children[i], node2.children[i], ds1, ds2):
            return False
    return True

def is_logical_equal(node1:TreeNode, node2:TreeNode,ds1:DisjointSet,ds2:DisjointSet):
    """
    whether 2 trees logically equal
    """
    node1.children.sort(key=lambda x: x.location)
    node2.children.sort(key=lambda x: x.location)
    if not check_string_equal(node1.data,node2.data):
        if ds1 == None or ds2 == None:
            return False
        list1 = [node1] + ds1.find_child(ds1.find_head(node1))
        list2 = [node2] + ds2.find_child(ds2.find_head(node2))
        for i in list1:
            for j in list2:
                if ds1 != None and ds2 != None and is_equal_tree(i, j, ds1, ds2):
                    return True
        return False
    if len(node1.children) != len(node2.children):
        return False
    for i in range(len(node1.children)):
        if not is_logical_equal(node1.children[i], node2.children[i],ds1,ds2):
            return False
    return True

def get_equation_type(string:str):
    """
    find the center equation place, otherwise return -1
    """
    loc,tmp = 0,0
    while loc < len(string):
        if string[loc] == '(':
            tmp += 1
        elif string[loc] == '=' and tmp <= 0:
            return loc
        elif string[loc] == ')':
            tmp -= 1
        loc += 1
    return -1

def get_colon_place(string:str):
    """
    find the center equation place, otherwise return -1
    """
    loc,tmp = 0,0
    while loc < len(string):
        if string[loc] == '(':
            tmp += 1
        elif string[loc] == ':' and tmp <= 0:
            return loc
        elif string[loc] == ')':
            tmp -= 1
        loc += 1
    return -1


def maketree(string:str , location = 0):
    """
    return tree of a parse
    """
    left = string.find('(')
    right = string.rfind(')')
    if left == -1 or right == -1:
        return TreeNode(string.strip() , location=location)
    root = TreeNode(string[:left].strip() , location=location)
    level = 0
    tmp = 0
    for i in range(left+1, right):
        if string[i] == '(':
            level += 1
        elif string[i] == ')':
            level -= 1
        elif string[i] == ',' and level == 0:
            root.add_child(maketree(string[left+1:i],tmp))
            left = i
            tmp += 1
    root.add_child(maketree(string[left+1:right],tmp))
    root.children.sort(key=lambda x: x.location)
    return root

## ===== Sentence Counter =====

def cnt_sentences(annotation, include_dec = True):
    """
    Count the number of sentences in an annotation.
    """
    (vars, facts, queries), _, _ = parse_annotation(annotation)
    cnt = len(facts) + len(queries)
    if include_dec:
        cnt += len(vars)
    return cnt

## ===== Algorithm for diff ======

def align2diff(
        best_alignments: List[List[Tuple[int, int]]], 
        filtered: Tuple[List[str], List[str]]
    ) -> str:
    """
    Generate a diff log for two annotations, based on the return value
    from `cmp_question`. Return a human-readable diff string.

    Only pick the first element in `best_alignment`.
    """
    assert len(best_alignments) > 0, "Empty alignment in diff!"

    filtered1, filtered2 = filtered
    # where 1 is gold, 2 is predict
    ds2 = DisjointSet()
    ds2.add_annotation(filtered2)
    ds1 = DisjointSet()
    ds1.add_annotation(filtered1)

    idx1, idx2 = map(lambda x: list(range(len(x))), filtered)

    alignment = best_alignments[0]
    for align1, align2 in alignment:
        if align1 in idx1: idx1.remove(align1)
        if align2 in idx2: idx2.remove(align2)

    # start add new thing  
    for i in alignment:
        if (a:= get_colon_place(filtered1[i[0]])) != -1:
           if (b:= get_colon_place(filtered2[i[1]])) != -1:
              tmp1 = maketree(filtered1[i[0]][:a].strip())
              tmp2 = maketree(filtered2[i[1]][:b].strip())
              ds1.add(tmp2)
              ds1.union(tmp1, tmp2)


    to_remove = []
    for i in idx1:
        gold = filtered1[i]
        if (tmp := get_equation_type(gold)) == -1: # we only check the parse with equation
            to_remove.append(i)
            continue
        l_gold = gold[:tmp].strip() if tmp != -1 else gold
        r_gold = gold[tmp+1:].strip() if tmp != -1 else gold

        flag = False
        for j in idx2:
            pre = filtered2[j]
            l_pre = pre[:get_equation_type(pre)].strip() if get_equation_type(pre) != -1 else pre
            r_pre = pre[get_equation_type(pre)+1:].strip() if get_equation_type(pre) != -1 else pre
            
            if is_logical_equal(maketree(l_gold), maketree(l_pre), ds1, ds2):
                if "expression" in r_pre.lower():
                    if check_expression_equal(r_gold,r_pre):
                        flag = True
                        break
                elif check_string_equal(r_gold,r_pre):
                    flag = True
                    break
        if flag:
            to_remove.append(i)
    
    for i in to_remove:
        idx1.remove(i)

    # end
    diff_string = ""
    if len(idx1) == 0:
        return diff_string
    if idx1 and idx2:
        diff_string += '\n'.join(f"< {s}" for s in map(lambda x: filtered1[x], idx1))
        diff_string += '\n---\n'
        diff_string += '\n'.join(f"> {s}" for s in map(lambda x: filtered2[x], idx2))
    elif idx1:
        diff_string += '\n'.join(f"< {s}" for s in map(lambda x: filtered1[x], idx1))
    elif idx2:
        diff_string += '\n'.join(f"> {s}" for s in map(lambda x: filtered2[x], idx2))

    return diff_string

def diff(
        annotation1: str, 
        annotation2: str, 
        include_dec: bool = True,
        verbose: bool = False, 
        max_workers: int = None,
        speed_up: bool = True
    ) -> str:
    """
    Generate a diff log for two annotations. Return a human-readable diff string.
    """
    _, aligns, filtered = cmp_question(annotation1, annotation2, include_dec, verbose, max_workers, speed_up)
    diff_log: str = align2diff(aligns, filtered)
    return diff_log


## ===== Filter annotations =====

def filter_annotation(annotation: str) -> str:
    """
    Filter out invalid sentences in an annotation. Usually embedded
    after the model predictions.
    """
    ## remove invalid sentences
    (vars, facts, queries), to_filter, alignment = parse_annotation(annotation)

    ### we allow unused variabels. e.g. if the question mentioned O is the Origin, then 'O: Origin' should appear.
    
    ### we should only remove variables that appear multiple times
    ### this might fail on some special cases, e.g. 'P, Q: Point', 'P: Circle' will retain both.
    filtered = []
    for idx in set(alignment['vars'].values()):
        filtered.append(to_filter[idx])

    ## remove same facts
    for idx in set(alignment['facts'].values()):
        filtered.append(to_filter[idx])

    for expr in queries:
        idx = alignment['queries'][expr]
        filtered.append(to_filter[idx])

    return '\n'.join(filtered) if filtered else ''
    

def filter_annotation_aggressive(annotation: str) -> str:
    """
    Similar to `filter_annotation`, but have more aggressive strategies. May
    change the annotations to (most likely) equivlent expressions.

    TODO: The correctness of this function requires further testing. WIP.
    """
    ## remove invalid sentences
    (vars, facts, queries), to_filter, alignment = parse_annotation(annotation)

    ## check used variables
    ## TODO: deal with the undeclared variables. remove facts/queries or add declarations, or do nothing?
    used_vars = set()
    for expr in facts + queries:
        used_vars = used_vars.union(expr.free_symbols)
    unused_vars = set(vars).difference(used_vars)
    undeclared_vars = used_vars.difference(set(vars).union({Symbol('x'), Symbol('y')}))

    declared_and_used_vars = set(vars).intersection(used_vars)
    filtered = [f"{v}: {v.type}" for v in declared_and_used_vars]

    filtered.extend(list(set(str(s) for s in facts)))
    filtered.extend([f'{expr} = ?' for expr in queries])

    return '\n'.join(filtered) if filtered else ''