# file: build_tree.py
import warnings

from antlr4 import InputStream, CommonTokenStream
from AssertionalLogicLexer import AssertionalLogicLexer
from AssertionalLogicParser import AssertionalLogicParser
from AssertionalLogicVisitor import AssertionalLogicVisitor

from Declartion import declaration_to_lean
from Operators import operator_to_lean
from utils import Node, extract_declarations, extract_assertions


def parse_program_string(input_text: str) -> Node:
    """
    解析完整 program JSON 字符串，返回自定义 Node 树。
    """
    try:
        input_stream = InputStream(input_text)
        lexer = AssertionalLogicLexer(input_stream)
        tokens = CommonTokenStream(lexer)
        parser = AssertionalLogicParser(tokens)
        tree = parser.program()

        visitor = BuildTreeVisitor()
        return visitor.visit(tree)
    except Exception as e:
        raise RuntimeError(f"[ParseError] 解析 program 失败: {e}")


def parse_declarations_string(decl_str: str) -> Node:
    """
    只解析 Declarations 部分。
    输入例："x: Real; y: Integer;"
    """
    try:
        full_text = f"{decl_str}\n"
        input_stream = InputStream(full_text)
        lexer = AssertionalLogicLexer(input_stream)
        tokens = CommonTokenStream(lexer)
        parser = AssertionalLogicParser(tokens)
        tree = parser.declarationList()

        visitor = BuildTreeVisitor()
        return visitor.visit(tree)
    except Exception as e:
        raise RuntimeError(f"[ParseError] 解析 Declarations 失败: {e}")


def parse_facts_string(fact_str: str) -> Node:
    """
    只解析 Facts 部分。
    输入例："Abs(x - 2) = 3; x + 1 = 5;"
    """
    try:
        full_text = f"{fact_str}\n"
        input_stream = InputStream(full_text)
        lexer = AssertionalLogicLexer(input_stream)
        tokens = CommonTokenStream(lexer)
        parser = AssertionalLogicParser(tokens)
        tree = parser.assertionList()

        visitor = BuildTreeVisitor()
        return visitor.visit(tree)
    except Exception as e:
        raise RuntimeError(f"[ParseError] 解析 Facts 失败: {e}")


def parse_query_string(query_str: str) -> Node:
    """
    只解析 Query 部分。
    输入例："x = ?"
    """
    try:
        full_text = f"{query_str}\n"
        input_stream = InputStream(full_text)
        lexer = AssertionalLogicLexer(input_stream)
        tokens = CommonTokenStream(lexer)
        parser = AssertionalLogicParser(tokens)
        tree = parser.queryList()

        visitor = BuildTreeVisitor()
        return visitor.visit(tree)
    except Exception as e:
        raise RuntimeError(f"[ParseError] 解析 Query 失败: {e}")


class BuildTreeVisitor(AssertionalLogicVisitor):
    """把 ParseTree 转成我们想要的 Node 树"""

    def visitProgram(self, ctx:AssertionalLogicParser.ProgramContext):
        root = Node("program")
        # 三个部分：Declarations, Facts, Query
        # 按照语法，program -> declarationList assertionList queryList
        decls = self.visit(ctx.declarationList()) if ctx.declarationList() else []
        facts = self.visit(ctx.assertionList()) if ctx.assertionList() else []
        queries = self.visit(ctx.queryList()) if ctx.queryList() else []
        root.add_child(decls)
        root.add_child(facts)
        root.add_child(queries)
        return root

    def visitDeclarationList(self, ctx:AssertionalLogicParser.DeclarationListContext):
        node = Node("Declarations")
        # 遍历declarationList, 将每个declaration添加为孩子节点
        for decl in ctx.declaration():
            node.add_child(self.visit(decl))
        return node

    def visitDeclaration(self, ctx:AssertionalLogicParser.DeclarationContext):
        # declaration: variable ':' conceptID ';'
        var_name = ctx.variable().getText()       # 获取variable_name = 'x'
        type_name = ctx.conceptID().getText()     # 获取variable_type = 'Real'
        
        # 转lean
        lean_declaration = declaration_to_lean((var_name, type_name))
        decl_node = Node("declaration", lean_declaration)

        # 知识方程节点
        # decl_node = Node("declaration")
        # decl_node.add_child(Node("variable", var_name))
        # decl_node.add_child(Node(":", ":"))
        # decl_node.add_child(Node("conceptID", type_name))
        return decl_node

    def visitAssertionList(self, ctx: AssertionalLogicParser.AssertionListContext):
        node = Node("Facts")
        # for asrt in ctx.assertion():
        #     node.add_child(self.visit(asrt))
        for child in ctx.children:
            if child.getText() == ';':
                continue
            # assertion部分
            if isinstance(child, AssertionalLogicParser.AssertionContext):
                node.add_child(self.visitAssertion(child))
            # 单独的term
            elif isinstance(child, AssertionalLogicParser.TermContext):
                # 把 term 作为 assertion 包装起来
                term_node = Node("assertion")
                # term_node.add_child(self.visitArithmeticOpTerm(child))
                term_node.add_child(self.visit(child))
                node.add_child(term_node)
            else:
                warnings.warn(
                    f"未识别的 assertion 子节点类型: {type(child)}，文本内容为：'{child.getText()}'. ",
                    UserWarning
                )
        return node

    def visitAssertion(self, ctx:AssertionalLogicParser.AssertionContext):
        # assertion: term '=' term ';'?
        asrt_node = Node("assertion")
        left = self.visit(ctx.term(0))   
        right = self.visit(ctx.term(1))  
        eq = Node("OP", "=") 
        asrt_node.add_child(left)
        asrt_node.add_child(eq)
        asrt_node.add_child(right)
        return asrt_node

    def visitQueryList(self, ctx:AssertionalLogicParser.QueryListContext):
        node = Node("Query")
        for q in ctx.assertion():
            node.add_child(self.visit(q))
        return node

    # 根据语法，继续重写 visitAtomicIndividual、visitOperatorID、visitTerms 等
    def visitParenTerm(self, ctx):
        parenterm_node = Node("term")
        parenterm_node.add_child(Node("OP", "("))
        parenterm_node.add_child(self.visit(ctx.term()))
        parenterm_node.add_child(Node("OP", ")"))
        return parenterm_node
    
    def visitArithmeticOpTerm(self, ctx):
        arithmeticOpTerm_node = Node("term")
        left = self.visit(ctx.term(0))  # 左侧的 term
        right = self.visit(ctx.term(1))  # 右侧的 term
        op = ctx.op.text  # 运算符（比如 +, -, =, < 等）
        arithmeticOpTerm_node.add_child(left)
        arithmeticOpTerm_node.add_child(Node("OP", op))
        arithmeticOpTerm_node.add_child(right)
        return arithmeticOpTerm_node
    
    def visitBinaryOpTerm(self, ctx):
        binaryOpTerm_node = Node("term")
        left = self.visit(ctx.term(0))  # 左侧的 term
        right = self.visit(ctx.term(1))  # 右侧的 term
        op = ctx.op.text  # 运算符（比如 *, /, % 等）
        binaryOpTerm_node.add_child(left)
        binaryOpTerm_node.add_child(Node("OP", op))
        binaryOpTerm_node.add_child(right)
        return binaryOpTerm_node
    
    def visitOperatorTerm(self, ctx):
        # terms: (declaration | term) (',' term )*
        op = ctx.operatorID().getText()
        OperatorTerm_node = Node(op)
        for term in ctx.termList().term():
            OperatorTerm_node.add_child(self.visit(term))
        # 转lean
        operator_node_children = OperatorTerm_node.get_subtree_semantics()
        lean_operator = operator_to_lean(op, *operator_node_children)
        new_operator_node = Node(op, lean_operator)
        return new_operator_node

    def visitLogicOpTerm(self, ctx):
        LogicOpTerm_node = Node("term")
        op = ctx.op.text  # 获取操作符（'∧' 或 '∨'）
        LogicOpTerm_node.add_child(self.visit(ctx.term(0)))
        LogicOpTerm_node.add_child(Node("OP", op))
        LogicOpTerm_node.add_child(self.visit(ctx.term(1)))
        return LogicOpTerm_node

    def visitSetTerm(self, ctx):
        seterm_node = Node("term")
        values = []
        # 正确访问 termList() 里的 term() 方法（返回 List）
        for term in ctx.termList().term():
            child_node = self.visit(term)
            if child_node.children and child_node.children[0].value:
                values.append(child_node.children[0].value)
            else:
                print("Warning: unexpected child_node structure:", child_node)
                values.append("unknown")
        seterm_node.add_child(Node("setterm", "{" + ", ".join(values) + "}"))
        return seterm_node
    
    def visitSetOpTerm(self, ctx):
        setopterm_node = Node("term")
        # 访问左边的 term
        left = self.visit(ctx.term(0))
        # 访问操作符
        op = ctx.op.text  # 比如 '∈', '∪', '⊆'
        op_node = Node("OP", op)
        # 访问右边的 term
        right = self.visit(ctx.term(1))
        # 按顺序添加子节点
        setopterm_node.add_child(left)
        setopterm_node.add_child(op_node)
        setopterm_node.add_child(right)
        return setopterm_node
    
    def visitTupleTerm(self, ctx):
        tuple_node = Node("term")
        var_names = []
        common_type = None
        # 遍历每一个 term 子节点
        for term_ctx in ctx.term():
            child_node = self.visit(term_ctx)
            if child_node.children:
                decl_text = child_node.children[0].value.strip("() ")
                if ":" in decl_text:
                    var, typ = map(str.strip, decl_text.split(":"))
                    var_names.append(f"{var}: {typ}")
                    if common_type is None:
                        common_type = typ
                    elif common_type != typ:
                        raise ValueError("Inconsistent types in tuple declaration") 
                else:
                    var_names.append(decl_text)
                
        # 将收集的值合并为一个字符串 "(m, n)"
        tuple_node.add_child(Node("tupleterm", f"({', '.join(var_names)})"))  # 合并为 tuple 形式的字符串
        return tuple_node

    def visitAtomicTerm(self, ctx):
        atom_node = Node("term")
        atom_ctx = ctx.atomicIndividual()
        if atom_ctx.variableID():
            atom_node.add_child(Node("atomicIndividual", atom_ctx.variableID().getText()))   # 访问变量名
            return atom_node  
        elif atom_ctx.constant():
            atom_node.add_child(Node("atomicIndividual", atom_ctx.constant().getText()))   # 访问常量值
            return atom_node
        elif atom_ctx.declaration():
            decl_ctx = atom_ctx.declaration()
            var_name = decl_ctx.variable().getText()
            concept_name = decl_ctx.conceptID().getText()
            # decl_node = Node("declaration")
            # decl_node.add_child(Node("variable", var))
            # decl_node.add_child(Node("concept", concept))
            # 转lean
            lean_declaration = declaration_to_lean((var_name, concept_name))
            decl_node = Node("declaration", lean_declaration)
            atom_node.add_child(decl_node)
            return atom_node
        elif atom_ctx.getText() == "?":
            atom_node.add_child(Node("atomicIndividual", "sorry"))
            return atom_node
        return atom_node.add_child(Node("atomicIndividual", "None"))


if __name__ == "__main__":
    # 1. 读入你的例子文件
    decl_str = "a: Real; b: Real; h: Real; k: Real"
    facts_str = "Is_Odd_Number(a)"
    query_str = "(a, c, b) = ?"

    print(">>> Declarations")
    decl_tree = parse_declarations_string(decl_str)
    print(decl_tree)
    lean_decl = extract_declarations(decl_tree)

    print(">>> Facts")
    facts_tree = parse_facts_string(facts_str)
    print(facts_tree)
    lean_fact = extract_assertions(facts_tree, 1)

    print(">>> Query")
    query_tree = parse_query_string(query_str)
    print(query_tree)
    lean_query = extract_assertions(query_tree, 2)

    print(f"theorem xx {lean_decl} \n {lean_fact} \n: {lean_query} := by sorry")

    # input_stream = InputStream(s)

    # # 2. 词法/语法分析
    # lexer = AssertionalLogicLexer(input_stream)
    # tokens = CommonTokenStream(lexer)
    # parser = AssertionalLogicParser(tokens)
    # tree = parser.program()

    # # 打印树
    # print(tree.toStringTree(recog=parser))

    # # 3. 访问构建自定义树
    # visitor = BuildTreeVisitor()
    # my_tree = visitor.visit(tree)

    # # 4. 打印
    # print(my_tree)
