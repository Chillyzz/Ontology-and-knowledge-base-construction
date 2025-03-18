目前无法表示的几个

1. 因式分解
2. 化简表达式（化简的题目 1. 有答案后直接证明 原式 = 答案； 2. 用 Sorry代替）

3. Get_Value_Expression: Get_Value_Expression({P: Expression}) -> Number # 输入一个表达式(不含变量), 返回它简化后的值

4. Simplified_Expression: Simplified_Expression({P: Expression}, {x: Variable}) -> Expression # 输入一个表达式和变量, 返回化简后的表达式(合并同类项)

5. Get_Factors_Expression: Get_Factors_Expression({P: Polynomial}) -> Expression # 输入一个表达式, 做因式分解

3. 无限循环小数 （OK吗？）    2. RepatingDecimals \\in Decimals: Numbers like $0.4\\overline{4}$ (无法表示); 小数的某些性质，数位也未必能表示

6. Get_Repeating_Decimal: Get_Repeating_Decimal({x: Integer}, {y: Integer}) -> RationalNumbers (表达一个无限循环小数, x是整数部分, y是小数部分)

小数部分（例如小数点后几位这种，直接扔掉；表示不了一点）

推理时用的算子

1. Get_Reciprocal: Get_Reciprocal({x: Number}) -> Number #  Get_Reciprocal(4) = 1/4 (取倒数) [ 不单独建模，在解题时自动推理 ]

数列

13. ExplicitFormula: ExplicitFormula({s: Sequence}) -> Expression #直接计算数列的通项公式  
    *Example:* A: Sequence, ExplicitFormula(A) = 2n + 1

数列的长度问题

二次函数 -- 15. Get_Quadratic_Discriminant: Get_Quadratic_Discriminant({P: Quadratic}) -> Number
-- 8. Get_Function_CriticalPoint: Get_Function_CriticalPoint(f: Function) -> Set

求表达式最大值最小值（转成函数）

4. Get_Expression_Maximum: Get_Expression_Maximum(f: Expression) -> Number # 输入一个表达式, 返回可能的最大值

5. Get_Expression_Minimum: Get_Expression_Minimum(f: Expression) -> Number # 输入一个表达式, 返回可能的最小值

有序集合（List？）

-- 22. Get_Sorted_Set: Get_Sorted_Set({A: Set}) -> Set 

函数定义域的问题 (不进行单独建模，或者说无法单独建模；根据题目条件去做)

1. Function_Domain: Function_Domain(f: Function) -> Set
    备注: 表示一个函数的定义域集合(无法计算, 只能 Query或赋值)

{
    "problem": "Compute the domain of the real-valued function \\[f(x)=\\sqrt{1-\\sqrt{2-\\sqrt{x}}}.\\]",
    "level": "Level 5",
    "type": "Algebra",
    "solution": "For the contents of the innermost square root to be nonnegative, we must have $x\\geq 0$.  To satisfy the middle square root, we must have  $$2-\\sqrt{x}\\geq 0\\Rightarrow 4\\geq x.$$ Finally, the outermost square root requires $$1-\\sqrt{2-\\sqrt{x}}\\geq 0.$$ This gives us $$1\\geq 2-\\sqrt{x}\\Rightarrow x\\geq 1.$$ Combining our inequalities, we get ${1\\leq x\\leq 4}$, or $x \\in \\boxed{[1, 4]}$ in interval notation.",
    "Declarations": "",
    "Facts": "",
    "Query": "",
    "Proof": ""
},

默认的运算符

加减乘除乘方开方；大于小于大于等于小于等于

有限集合无限集合如何互相转换

暂时没有能力做单位转换的工作

知识方程的规范，Query是结论未知；Proof是结论已知


    {
        "problem": "Suppose the roots of the polynomial $x^2 - mx + n$ are positive prime integers (not necessarily distinct). Given that $m < 20,$ how many possible values of $n$ are there?",
        "level": "Level 5",
        "type": "Algebra",
        "solution": "Let $p$ and $q$ be the prime roots. Then, we know that $m = p+q$ and $n = pq$. Since $m < 20$, the primes $p$ and $q$ must both be less than $20$.\n\nThe primes less than $20$ are $2,$ $3,$ $5,$ $7,$ $11,$ $13,$ $17,$ $19.$ Now we list all possible pairs $(p, q)$ such that $p + q < 20$, remembering to also include the cases in which $p=q$: \\[\\begin{aligned} & (2,2),(2,3),(2,5),(2,7),(2,11),(2,13),(2,17) \\\\\n&(3,3),(3,5),(3,7),(3,11),(3,13) \\\\\n&(5,5),(5,7),(5,11),(5,13) \\\\\n&(7,7),(7,11) \\end{aligned}\\]There are $7 + 5 + 4 + 2 = 18$ pairs in total. Each pair produces a value for $n$, and furthermore, these values are all distinct, because every positive integer has a unique prime factorization. Therefore, there are $\\boxed{18}$ possible values for $n$.",
        "Declarations": "p: PrimeNumbers; q: PrimeNumbers; m: Real; n: Real; P: Polynomial",
        "Facts": "P = x^2 - m *x + n; Is_Root(P, p) = True; Is_Root(P, q) = True; p + q < 20",
        "Query": "Set_Cardinality(Build_Set(n, Exist((p, q),  Is_Prime(p) ∧ Is_Prime(q) ∧ p + q < 20 ) ))",
        "Proof": ""
    },

关于集合的问题，规范（不报错）

多项式和函数的歧义

多项式和函数和集合的类型问题

阶梯函数

解析几何题目做不了

    {
        "problem": "Let $P=(a,b)$ be the point of intersection of the line $y=2x-10$ and the line through $(7,8)$ and $(9,0)$.  Compute $a+b$.",
        "level": "Level 4",
        "type": "Algebra",
        "solution": "The slope of the line through $(7,8)$ and $(9,0)$ is $\\frac{8-0}{7-9}=\\frac{8}{-2}=-4$.  Thus, the line has equation $y=-4x+b$ for some $b$.  Since $B(9,0)$ lies on this line, we have $0=-4(9)+b \\Rightarrow b=36$, and thus the equation of the line is $y=-4x+36$.\n\nTo determine the point of intersection between the lines having equations $y=-4x+36$ and $y=2x-10$, we set the two expressions for $y$ equal to each other and solve for $x$.  We have $-4x+36=2x-10 \\Rightarrow x = \\frac{23}{3}$.  It follows that  $y=2x-10=2\\left(\\frac{23}{3}\\right)-10 = \\frac{46}{3}-\\frac{30}{3}=\\frac{16}{3}$.\n\nThus, $P=(\\frac{23}{3},\\frac{16}{3})$ and $a+b=\\frac{23}{3}+\\frac{16}{3}=\\frac{39}{3}=\\boxed{13}$.",
        "Declarations": "",
        "Facts": "",
        "Query": "",
        "Proof": ""
    },

变量的定义，变量不能在declaration中声明？ 变量用于 集合、不等式、方程等等

    {
        "problem": "The graphs of two linear functions, $f(x)$ and $g(x)$, are shown here on one set of axes: [asy]\nsize(150);\nreal ticklen=3;\nreal tickspace=2;\n\nreal ticklength=0.1cm;\nreal axisarrowsize=0.14cm;\npen axispen=black+1.3bp;\nreal vectorarrowsize=0.2cm;\nreal tickdown=-0.5;\nreal tickdownlength=-0.15inch;\nreal tickdownbase=0.3;\nreal wholetickdown=tickdown;\nvoid rr_cartesian_axes(real xleft, real xright, real ybottom, real ytop, real xstep=1, real ystep=1, bool useticks=false, bool complexplane=false, bool usegrid=true) {\n\nimport graph;\n\nreal i;\n\nif(complexplane) {\n\nlabel(\"$\\textnormal{Re}$\",(xright,0),SE);\n\nlabel(\"$\\textnormal{Im}$\",(0,ytop),NW);\n\n} else {\n\nlabel(\"$x$\",(xright+0.4,-0.5));\n\nlabel(\"$y$\",(-0.5,ytop+0.2));\n\n}\n\nylimits(ybottom,ytop);\n\nxlimits( xleft, xright);\n\nreal[] TicksArrx,TicksArry;\n\nfor(i=xleft+xstep; i<xright; i+=xstep) {\n\nif(abs(i) >0.1) {\n\nTicksArrx.push(i);\n\n}\n\n}\n\nfor(i=ybottom+ystep; i<ytop; i+=ystep) {\n\nif(abs(i) >0.1) {\n\nTicksArry.push(i);\n\n}\n\n}\n\nif(usegrid) {\n\nxaxis(BottomTop(extend=false), Ticks(\"%\", TicksArrx ,pTick=gray(0.22),extend=true),p=invisible);//,above=true);\n\nyaxis(LeftRight(extend=false),Ticks(\"%\", TicksArry ,pTick=gray(0.22),extend=true), p=invisible);//,Arrows);\n\n}\n\nif(useticks) {\n\nxequals(0, ymin=ybottom, ymax=ytop, p=axispen, Ticks(\"%\",TicksArry , pTick=black+0.8bp,Size=ticklength), above=true, Arrows(size=axisarrowsize));\n\nyequals(0, xmin=xleft, xmax=xright, p=axispen, Ticks(\"%\",TicksArrx , pTick=black+0.8bp,Size=ticklength), above=true, Arrows(size=axisarrowsize));\n\n} else {\n\nxequals(0, ymin=ybottom, ymax=ytop, p=axispen, above=true, Arrows(size=axisarrowsize));\n\nyequals(0, xmin=xleft, xmax=xright, p=axispen, above=true, Arrows(size=axisarrowsize));\n\n}\n};\nrr_cartesian_axes(-5,5,-5,5);\nreal f(real x) {return (4-x)/2;}\nreal g(real x) {return 2x-4;}\ndraw(graph(f,-5,5,operator ..), blue+1.25);\ndraw(graph(g,-1/2,9/2,operator ..), orange+1.25);\ndraw((-3,-6)--(-1,-6),blue+1.25); label(\"$y=f(x)$\",(-1,-6),E);\ndraw((-3,-7)--(-1,-7),orange+1.25); label(\"$y=g(x)$\",(-1,-7),E);\n[/asy] Each small box in the grid is $1$ unit by $1$ unit.\n\nEvaluate $f(g(1))\\cdot g(f(1))$.",
        "level": "Level 4",
        "type": "Algebra",
        "solution": "The point $(1,-2)$ is on the graph of $y=g(x)$, and the point $(-2,3)$ is on the graph of $y=f(x)$, so $$f(g(1)) = f(-2) = 3.$$ The point $(1,1.5)$ is on the graph of $y=f(x)$, and the point $(1.5,-1)$ is on the graph of $y=g(x)$, so $$g(f(1)) = g(1.5) = -1.$$ Thus, $$f(g(1))\\cdot g(f(1)) = (3)(-1) = \\boxed{-3}.$$",
        "Declarations": "",
        "Facts": "",
        "Query": "",
        "Proof": ""
    },

#### Arithmetical Operation(更新，基本算数运算符的算子取消；加减乘除乘方取消)

1. Add: Add({x: Addtype}, {y: Addtype}) -> Addtype     # Add({3: Numbers} , {5:Numbers}) = 8.
    备注: Addtype作为一个集合会单独给出, 下同

2. Minus: Minus({x: Addtype}, {y: Addtype}) -> Addtype  # Minus({8: Numbers}, {5: Numbers}) = 3.

3. Multiply: Multiply({x: Addtype}, {y: Addtype}) -> Addtype  # Multiply({8: Numbers}, {5: Numbers}) = 40.

4. Divide: Divide({x: Addtype}, {y: Addtype}) -> Addtype  # Divide({8: Numbers}, {2: Numbers}) = 4.

5. Power: Power({x: Powertype}, {y: Powertype}) -> Powertype # Power({2: Numbers}, {4: Numbers}) = 16. 

6. Radical: Radical({x: Radicaltype}, {y: Radicaltype}) -> Radicaltype # Radical({x^2: Expression}, {2: Number}) = x. (开方就是n分之一次方)

1. Is_GreaterThan: Is_Greaterthan({a: Number}, {b: Number}) -> Boolean  # Is_Greaterthan({3: Number}, {5: Number}) -> False.
    备注: 判断 a > b 是否成立, 成立返回 True 反正 False, 下同

2. Is_LessThan: Is_Lessthan({a: Number}, {b: Number}) -> Boolean # Is_Lessthan({3: Number}, {5: Number}) -> True

3. Is_GreaterOrEqualThan: Is_GreaterOrEqualThan({a: Number}, {b: Number}) -> Boolean # Is_GreaterOrEqualThan({5: Number}, {5: Number}) -> True

4. Is_LessOrEqualThan: Is_LessOrEqualThan({a: Number}, {b: Number}) -> Boolean # Is_LessOrEqualThan({4: Number}, {5: Number}) -> True
    (大于、小于、大于等于、小于等于)


某些涉及函数图像的算子

8. Get_Function_InflectionPoints: Get_Function_InflectionPoints(f: Function) -> Set  
   备注: 输入一个函数, 返回该函数的拐点集合。  

9. Get_Function_Asymptotes: Get_Function_Asymptotes(f: Function) -> Set  
   备注: 输入一个函数, 返回该函数的渐近线集合。 

13. Get_Function_TangentLine: Get_Function_TangentLine(f: Function, x: Number) -> Function  
    备注: 输入一个函数 \( f \) 和一个数字 \( x \), 返回在点 \( x \) 处的切线方程。返回一个新的函数表示切线。 

1. Get_Function_Domain: Get_Function_Domain(f: Function) -> Set
    备注: 输入一个函数, 返回一个集合(它的定义域) -- 无法定义定义域。

导数、积分暂不考虑

6. Get_Function_Derivative: Get_Function_Derivative(f: Function) -> Function  
   备注: 输入一个函数, 返回该函数的导数（作为新的函数）。  

7. Get_Function_Integral: Get_Function_Integral(f: Function) -> Function  
   备注: 输入一个函数, 返回该函数的积分（作为新的函数）。  


连续性

(暂定)
5. Get_Function_Continuity: Get_Function_Continuity({f: Function}, {D: Interval}) -> Boolean  
   备注: 输入一个函数, 判断该函数在给定的区间内是否连续。返回布尔值，`True`表示函数在定义域内连续，`False`表示不连续。 

冗余的算子

23. Get_Function_Expression: Get_Function_Expression(f: Function) -> Expression
    备注: 输入一个函数 f ; 返回它的表达式

26. Build_Function: Build_Function({f: Expression}, {x: Variable}) -> Function
    备注: 输入一个表达式 f 以及变量, 返回由这个表达式对应的函数

单独建模

#### Compare Operation

5. Get_LessThan_Inequation: Get_LessThan_Inequation({p: Expression}, {q: Expression}) -> Inequation
    备注: 输入两个Expression, 用小于号链接得到一个不等式

6. Get_GreaterThan_Inequation: Get_GreaterThan_Inequation({p: Expression}, {q: Expression}) -> Inequation 
    备注: 输入两个Expression, 用大于号链接得到一个不等式

7. Get_Equation: Get_Equation({p: Expression}, {q: Expression}) -> Equation
    备注: 输入两个Expression, 用等号链接得到一个等式

8. Get_LessOrEqualThan_Inequation: Get_LessOrEqualThan_Inequation({p: Expression}, {q: Expression}) -> Inequation
    备注: 输入两个Expression, 用小于等于号链接得到一个不等式

9. Get_GreaterOrEqualThan_Inequation: Get_GreaterOrEqualThan_Inequation({p: Expression}, {q: Expression}) -> Inequation
    备注: 输入两个Expression, 用大于等于号链接得到一个不等式