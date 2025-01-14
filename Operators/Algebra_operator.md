# Operator

#### Arithmetical Operation

1. Add: Add({x: Addtype}, {y: Addtype}) -> Addtype     # Add({3: Numbers} , {5:Numbers}) = 8.
备注: Addtype作为一个集合会单独给出, 下同

2. Minus: Minus({x: Addtype}, {y: Addtype}) -> Addtype  # Minus({8: Numbers}, {5: Numbers}) = 3.

3. Multiply: Multiply({x: Addtype}, {y: Addtype}) -> Addtype  # Multiply({8: Numbers}, {5: Numbers}) = 40.

4. Divide: Divide({x: Addtype}, {y: Addtype}) -> Addtype  # Divide({8: Numbers}, {2: Numbers}) = 4.

5. Power: Power({x: Powertype}, {y: Powertype}) -> Powertype # Power({2: Numbers}, {4: Numbers}) = 16. 


#### Compare Operation

1. Is_GreaterThan: Is_Greaterthan({a: Number}, {b: Number}) -> Boolean  # Is_Greaterthan({3: Number}, {5: Number}) -> False.
    备注: 判断 a > b 是否成立, 成立返回 True 反正 False, 下同

2. Is_LessThan: Is_Lessthan({a: Number}, {b: Number}) -> Boolean # Is_Lessthan({3: Number}, {5: Number}) -> True

3. Is_GreaterOrEqualThan: Is_GreaterOrEqualThan({a: Number}, {b: Number}) -> Boolean # Is_GreaterOrEqualThan({5: Number}, {5: Number}) -> True

4. Is_LessOrEqualThan: Is_LessOrEqualThan({a: Number}, {b: Number}) -> Boolean # Is_LessOrEqualThan({4: Number}, {5: Number}) -> True



#### Equation and Expression

1. Get_Variable_Type: Get_Variable_Type(x: Variable) -> Concept # 变量x为一个正整数, Get_Variable_Type(x) -> Integer
备注: Get_Variable_Type函数的返回值类型应该单独注明

2. Solve_equation: Solve_equation({P: Equation}, {x: Variable}) -> Set # 输入一个等式和对应变量, 返回解集

3. Solve_inequation: Solve_inequation({P: Inequation}, {x: Variable}) -> Set # 输入一个不等式和对应变量, 返回解集

4. Get_Value_Expression: Get_Value_Expression({P: Expression}, {x: Variable}) -> Number # 输入一个表达式和变量, 返回它的值




#### Function

1. Get_Function_Domain: Get_Function_Domain(f: Function) -> Set
    备注: 输入一个函数, 返回一个集合(它的定义域)

2. Get_Function_Range: Get_Function_Range(f: Function) -> Set
    备注: 输入一个函数, 返回一个集合(它的值域)

3. Get_Function_Maximum: Get_Function_Maximum(f: Function) -> Number
    备注: 输入一个函数, 返回一个数字(它的最大值)

4. Get_Function_Minimum: Get_Function_Minimum(f: Function) -> Number
    备注: 输入一个函数, 返回一个数字(它的最小值)

(暂定)
5. Get_Function_Continuity: Get_Function_Continuity({f: Function}, {D: Interval}) -> Boolean  
   备注: 输入一个函数, 判断该函数在给定的区间内是否连续。返回布尔值，`True`表示函数在定义域内连续，`False`表示不连续。  

6. Get_Function_Derivative: Get_Function_Derivative(f: Function) -> Function  
   备注: 输入一个函数, 返回该函数的导数（作为新的函数）。  

7. Get_Function_Integral: Get_Function_Integral(f: Function) -> Function  
   备注: 输入一个函数, 返回该函数的积分（作为新的函数）。  

8. Get_Function_InflectionPoints: Get_Function_InflectionPoints(f: Function) -> Set  
   备注: 输入一个函数, 返回该函数的拐点集合。  

9. Get_Function_Asymptotes: Get_Function_Asymptotes(f: Function) -> Set  
   备注: 输入一个函数, 返回该函数的渐近线集合。  
 
10. Get_Function_Symmetry: Get_Function_Symmetry(f: Function) -> String  
    备注: 输入一个函数, 判断该函数是否具有对称性。返回字符串 "symmetrical" 或 "asymmetrical"。  

11. Get_Function_Zeroes: Get_Function_Zeroes(f: Function) -> Set  
    备注: 输入一个函数, 返回该函数的零点集合，即使得函数值为零的输入值集合。  

13. Get_Function_TangentLine: Get_Function_TangentLine(f: Function, x: Number) -> Function  
    备注: 输入一个函数 \( f \) 和一个数字 \( x \), 返回在点 \( x \) 处的切线方程。返回一个新的函数表示切线。 

14. Is_Increasing_Function: Is_Increasing_Function({f: Function}, {D: Interval}) -> Boolean
    备注: 输入一个函数 f 和一个区间 D; 判断函数 f 在区间 D 上是否是增函数

15. Is_Decreasing_Function: Is_Decreasing_Function({f: Function}, {D: Interval}) -> Boolean
    备注: 输入一个函数 f 和一个区间 D; 判断函数 f 在区间 D 上是否是减函数



#### Set

1. Set_Union: Set_Union({A: Set}, {B: Set}) -> Set
    备注: 输入两个集合, 返回它们的并集( A \cup B)

2. Set_Intersection: Set_Intersection({A: Set}, {B: Set}) -> Set
    备注: 输入两个集合, 返回它们的交集( A \cap B)

3. Set_Difference: Set_Difference({A: Set}, {B: Set}) -> Set 
    备注: 输入两个集合, 返回它们的差集

4. Set_SymmetricDifference: Set_SymmetricDifference({A: Set}, {B: Set}) -> Set  
   备注: 输入两个集合, 返回它们的对称差集 (\( A \Delta B \))  

5. Set_Subset: Set_Subset({A: Set}, {B: Set}) -> Boolean  
   备注: 输入两个集合, 判断集合 \( A \) 是否为集合 \( B \) 的子集 (\( A \subseteq B \))  

6. Set_ProperSubset: Set_ProperSubset({A: Set}, {B: Set}) -> Boolean  
   备注: 输入两个集合, 判断集合 \( A \) 是否为集合 \( B \) 的真子集 (\( A \subset B \))  

7. Set_Superset: Set_Superset({A: Set}, {B: Set}) -> Boolean  
   备注: 输入两个集合, 判断集合 \( A \) 是否为集合 \( B \) 的超集 (\( A \supseteq B \))  

8. Set_ProperSuperset: Set_ProperSuperset({A: Set}, {B: Set}) -> Boolean  
   备注: 输入两个集合, 判断集合 \( A \) 是否为集合 \( B \) 的真超集 (\( A \supset B \))  

9. Set_Cardinality: Set_Cardinality({A: Set}) -> Number  
   备注: 输入一个集合, 返回该集合的基数 (\( |A| \))  

10. Set_PowerSet: Set_PowerSet({A: Set}) -> Set  
    备注: 输入一个集合, 返回该集合的幂集 (\( \mathcal{P}(A) \)) 

11. Set_Complement: Set_Complement({A: Set}, {U: Set}) -> Set 
    备注: 输入一个集合 \( A \) 和全集 \( U \), 返回集合 \( A \) 相对于全集 \( U \) 的补集; 公式表示为：\( A' = U \setminus A \)。  

12. Set_Equality: Set_Equality({A: Set}, {B: Set}) -> Boolean  
    备注: 输入两个集合, 判断它们是否相等 (\( A = B \)); 如果两个集合的元素完全相同且没有重复元素, 则它们相等。  







