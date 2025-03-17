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

默认的运算符

加减乘除乘方开方；大于小于大于等于小于等于

有限集合无限集合如何互相转换

暂时没有能力做单位转换的工作

知识方程的规范，Query是结论未知；Proof是结论已知

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