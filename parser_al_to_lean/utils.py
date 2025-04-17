class Node:
    def __init__(self, name, value=None):
        self.name = name
        self.value = value      # 对于叶子节点可以存原文
        self.children = []      # 子节点列表

    def add_child(self, node):
        self.children.append(node)

    def _repr(self, level=0):  # 内部方法：递归打印
        indent = "  " * level
        if self.value is not None:
            return f"{indent}{self.name}: {self.value!r}\n"
        else:
            s = f"{indent}{self.name}\n"
            for c in self.children:
                s += c._repr(level + 1)
            return s

    def __repr__(self):  # 官方支持的 __repr__ 方法
        return self._repr()  # 调用上面支持缩进的版本
    
    # 打印子树的叶子节点，还原原始语义
    def get_semantic_string(self):
        """
        获取以该节点为根的整棵子树的语义字符串。
        """
        if not self.children:
            return str(self.value) if self.value is not None else ""
        else:
            return " ".join(child.get_semantic_string() for child in self.children)

    def get_subtree_semantics(self):
        """
        获取每个子节点对应的语义字符串，用于表示当前节点的语义组成。
        例如对 Solve_equation 返回 ['y: Real', 'Abs(y - 5) - 4 = 0']
        """
        result = []
        for child in self.children:
            if child.name == "declaration":
                result.append(child.value)
            else:
                result.append(child.get_semantic_string())
        return result


def get_leaf_values(node):
    """
    递归获取一个节点下所有叶子节点的 value，按从左到右顺序拼接。
    """
    if not node.children and node.value is not None:
        return [node.value.strip()]
    values = []
    for child in node.children:
        values.extend(get_leaf_values(child))
    return values


def extract_declarations(declarations_node):
    """
    从 Declarations 节点中提取所有 declaration 的叶子节点，并拼接为一个字符串。
    """
    declarations = []
    for child in declarations_node.children:
        if child.name != "declaration":
            continue
        # 获取当前 declaration 的所有叶子 value
        leaf_values = get_leaf_values(child)
        declarations.append("".join(leaf_values))
    return " ".join(declarations)

def extract_assertions(assertions_node, choose):
    """
    遍历Facts节点，输出lean的格式
    choose = 1: 传入的是facts节点，返回时需加上h1这样的字眼
    choose = 2: 传入的是query节点，返回时不做处理
    """
    all_assertions = []
    for child in assertions_node.children:
        if child.name != "assertion":
            continue
        # 假设 assertion 节点结构固定：term, OP, term
        if len(child.children) == 3:
            # term '=' term
            left_term = child.children[0]
            op_node = child.children[1]
            right_term = child.children[2]
            left_expr = " ".join(get_leaf_values(left_term))
            right_expr = " ".join(get_leaf_values(right_term))
            expr = f"{left_expr} {op_node.value} {right_expr}"
        # 单独的 term
        elif len(child.children) == 1:
            term_node = child.children[0]
            expr = " ".join(get_leaf_values(term_node))
        else:
            raise ValueError(f"Unexpected number of children in assertion node: {len(child.children)}")
        all_assertions.append(expr)

    # 统一添加 h1, h2, ...
    if choose == 1:
        final_output = []
        for i, assertion in enumerate(all_assertions):
            final_output.append(f"(h{i+1} : {assertion})")
        return " ".join(final_output)
    else:
        return " ".join(all_assertions)
    

if __name__ == "__main__":
    # test
    program_node = Node("program")
    declarations_node = Node("DeclarationList")
    facts_node = Node("FactList")
    query_node = Node("QueryList")
    program_node.add_child(declarations_node)
    program_node.add_child(facts_node)
    program_node.add_child(query_node)

    dec_1 = Node("declaration", "(a: N)")
    dec_2 = Node("declaration", "(b: N)")
    dec_3 = Node("declaration", "(c: N)")
    declarations_node.add_child(dec_1)
    declarations_node.add_child(dec_2)
    declarations_node.add_child(dec_3)

    assert1 = Node("assertion")
    facts_node.add_child(assert1)
    term1 = Node("term")
    term11 = Node("term")
    term12 = Node("term", "*")
    term13 = Node("term", "3")
    term111 = Node("term", "m")
    term112 = Node("term", "+")
    term113 = Node("term", "n")
    term1.add_child(term11)
    term1.add_child(term12)
    term1.add_child(term13)
    term11.add_child(term111)
    term11.add_child(term112)
    term11.add_child(term113)
    
    assert1.add_child(term1)
    assert1.add_child(Node("OP", "="))
    assert1.add_child(Node("term", "3"))

    print(extract_declarations(declarations_node))
    print(extract_assertions(facts_node, choose=1))
