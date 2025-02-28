(共100个 Operator)

# Operator

#### Arithmetical Operation

1. Add: Add({x: Addtype}, {y: Addtype}) -> Addtype     # Add({3: Numbers} , {5:Numbers}) = 8.
    备注: Addtype作为一个集合会单独给出, 下同

2. Minus: Minus({x: Addtype}, {y: Addtype}) -> Addtype  # Minus({8: Numbers}, {5: Numbers}) = 3.

3. Multiply: Multiply({x: Addtype}, {y: Addtype}) -> Addtype  # Multiply({8: Numbers}, {5: Numbers}) = 40.

4. Divide: Divide({x: Addtype}, {y: Addtype}) -> Addtype  # Divide({8: Numbers}, {2: Numbers}) = 4.

5. Power: Power({x: Powertype}, {y: Powertype}) -> Powertype # Power({2: Numbers}, {4: Numbers}) = 16. 

6. Radical: Radical({x: Radicaltype}, {y: Radicaltype}) -> Radicaltype # Radical({x^2: Expression}, {2: Number}) = x.

7. Log: Logtype({x: Logtype}, {y: Logtype}) -> Logtype # Log({2: Number}, {4: Number}) = 2.

8. Equal: Equal({x: Concept}, {y: Concept}) -> Boolean # 比较任意两个 individual 是否相同

9. Sum: Sum({A(i): Expression}, {P(i): Proposition}) -> Expression  # 对所有满足命题 P(i) 的 i, 对 A(i)求值

10. Product: Product({i: Expression}, {x: Integer}, {y: Integer}) -> Number  # 对表达式 i, 从 i = x 开始到 i = y 求乘积




#### Numbers

1. Get_Reciprocal: Get_Reciprocal({x: Number}) -> Number #  Get_Reciprocal(4) = 1/4 (取倒数)

2. Get_Number_Floor: Get_Number_Floor({x: Real}) -> Integer  # Get_Number_Floor(3.8) = 4 (向上取整)

3. Get_Number_Ceil: Get_Number_Ceil({x: Real}) -> Integer  # Get_Number_Ceil(3.8) = 4 (向下取整)

4. Abs: Abs({a: Number}) -> NonNegativeNumbers # Abs(-3.5) = 3,5 (取绝对值)

5. Get_Repeating_Decimal: Get_Repeating_Decimal({x: Integer}, {y: Integer}) -> RationalNumbers (表达一个无限循环小数, x是整数部分, y是小数部分)


#### Compare Operation

1. Is_GreaterThan: Is_Greaterthan({a: Number}, {b: Number}) -> Boolean  # Is_Greaterthan({3: Number}, {5: Number}) -> False.
    备注: 判断 a > b 是否成立, 成立返回 True 反正 False, 下同

2. Is_LessThan: Is_Lessthan({a: Number}, {b: Number}) -> Boolean # Is_Lessthan({3: Number}, {5: Number}) -> True

3. Is_GreaterOrEqualThan: Is_GreaterOrEqualThan({a: Number}, {b: Number}) -> Boolean # Is_GreaterOrEqualThan({5: Number}, {5: Number}) -> True

4. Is_LessOrEqualThan: Is_LessOrEqualThan({a: Number}, {b: Number}) -> Boolean # Is_LessOrEqualThan({4: Number}, {5: Number}) -> True

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
    

#### Equation and Expression

1. Get_Variable_Type: Get_Variable_Type(x: Variable) -> Concept # 变量x为一个正整数, Get_Variable_Type(x) -> Integer
    备注: Get_Variable_Type函数的返回值类型应该单独注明

2. Solve_equation: Solve_equation({P: Equation}, {x: Variable}) -> Set # 输入一个等式和对应变量, 返回解集(可扩展到多元, 但方程个数必须等于变量数)

3. Solve_inequation: Solve_inequation({P: Inequation}, {x: Variable}) -> Set # 输入一个不等式和对应变量, 返回解集

4. Get_Value_Expression: Get_Value_Expression({P: Expression}) -> Number # 输入一个表达式(不含变量), 返回它简化后的值

5. Simplified_Expression: Simplified_Expression({P: Expression}, {x: Variable}) -> Expression # 输入一个表达式和变量, 返回化简后的表达式(合并同类项)

6. Get_Factors_Expression: Get_Factors_Expression({P: Polynomial}) -> Expression # 输入一个表达式, 做因式分解

7. Get_Variable_Value: Get_Variable_Value(x: Variable) -> Set # 输入一个变量, 获取它的取值范围

8. Get_PolyDegree: Get_PolyDegree(x: Polynomial) -> Number # 输入一个多项式, 返回它的最高次幂

9. Get_Polyroots: Get_Polyroots(x: Polynomial) -> Set # 输入一个多项式, 返回它的根的集合

10. Get_Term_Coefficient: Get_Term_Coefficient({x: Polynomial}, {y: PolynomialTerm}) -> Number # 输入一个多项式和对应的某一项, 返回该项的系数

11. Get_PolyTerm: Get_PolyTerm(x: Polynomial) -> Set # 输入一个多项式, 返回它的项的集合

12. Get_ConstantTerm: Get_ConstantTerm(x: Polynomial) -> Number # 输入一个多项式, 返回它的常数项

13. Is_PolyFactor: IsPolyFactor({A: Polynomial}, {B: Polynomial}) -> Boolean # 输入两个多项式, 判断 A 是不是 B 的因子

14. Is_IrreduciblePolynomial: Is_IrreduciblePolynomial({A: Polynomial}) -> Boolean # 输入一个多项式, 判断是否可约

15. Get_Variable_Expression_Value: Get_Variable_Expression_Value({P: Expression}, {x: Variable}) -> Number # 输入一个表达式和变量的值, 返回对应的值

16. Get_Quadratic_Discriminant: Get_Quadratic_Discriminant({P: Expression}) -> Number # 输入一个二次方程, 返回它的判别式

17. Get_Expression_Maximum: Get_Expression_Maximum(f: Expression) -> Number # 输入一个表达式, 返回可能的最大值

18. Get_Expression_Minimum: Get_Expression_Minimum(f: Expression) -> Number # 输入一个表达式, 返回可能的最小值

19. Get_PolyCoefficient: Get_PolyCoefficient(x: Polynomial) -> Set # 输入一个多项式, 返回它的系数集合

20. Get_Constant_Value: Get_Constant_Value(x: Constant) -> Number # 求解一个常数的值
 



#### Sequence(数列)

1. Get_Sequence_Terms: Get_Sequence_Terms({s: Sequence}, {n: Integers}) -> ElementType # 输入一个数列和序号, 返回对应的数列元素

2. Build_Sequence: Build_Sequence({n: Variable}, {p: Expression}) -> Sequence # 输入数列的通项公式, 返回对应的数列

3. Is_ArithmeticSequence: Is_ArithmeticSequence({s: Sequence}) -> Boolean # 输入一个数列, 判断是不是等差数列

4. Is_GeometricSequence: Is_GeometricSequence({s: Sequence}) -> Boolean # 输入一个数列, 判断是不是等比数列

5. Is_MonotonicSequence: Is_MonotonicSequence({s: Sequence}) -> Boolean # 输入一个数列, 判断是不是单调数列

6. Get_CommonDifference: Get_CommonDifference({s: ArithmeticSequence}) -> Number # 输入一个等差数列, 返回它的公差

7. Get_CommonRatio: Get_CommonRatio({s: GeometricSequence}) -> Number # 输入一个等比数列, 返回它的公比

8. Is_Finite: Is_Finite({s: Sequence}) -> Boolean # 输入一个数列，判断是不是有限的

9. Is_Monotonic_Increasing_Sequence: Is_Monotonic_Increasing_Sequence({s: Sequence}) -> Boolean # 判断一个数列是不是单调递增的

10. Is_Monotonic_Decreasing_Sequence: Is_Monotonic_Decreasing_Sequence({s: Sequence}) -> Boolean # 判断一个数列是不是单调递减的

11. Get_Sequences_Length: Get_Sequences_Length({s: Sequence}) -> PositiveInteger # 计算一个数列的元素个数

12. Get_Sequences_Sum: Get_Sequences_Sum({s: Sequence}, {i: Integer}) -> Number # 计算数列的前n项和






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

16. Is_OddFunction: Is_OddFunction(f: Function) -> Boolean
    备注: 输入一个函数 f ; 判断函数 f 在定义域上是否是奇函数

17. Is_EvenFunction: Is_EvenFunction(f: Function) -> Boolean
    备注: 输入一个函数 f ; 判断函数 f 在定义域上是否是偶函数

18. Get_Function_Composition: Get_Function_Composition({f: Function}, {g: Function}) -> Function
    备注: 输入两个函数 f g; 返回它们的复合函数 f(g(x))

19. Is_Periodic_Function: Is_Periodic_Function(f: Function) -> Boolean
    备注: 输入一个函数 f ; 判断函数 f 在定义域上是否是周期函数

20. Get_Function_Minimalperiod: Get_Function_Minimalperiod(f: Function) -> Real
    备注: 输入一个函数 f ; 返回它的最小正周期

21. Get_Function_CriticalPoint: Get_Function_CriticalPoint(f: Function) -> Set
    备注: 输入一个函数 f ; 返回它零点的集合

22. Get_Inverse_Function: Get_Inverse_Function(f: Function) -> Function
    备注: 输入一个函数 f ; 返回它的反函数

23. Get_Function_Expression: Get_Function_Expression(f: Function) -> Expression
    备注: 输入一个函数 f ; 返回它的表达式

24. Get_Function_IthComposition: Get_Function_IthComposition({f: Function}, {i: Integer}) -> Function
    备注: 输入一个函数 f 以及它的复合次数 i; 返回它的复合函数 f^{i}(x)

25. Get_Function_Value: Get_Function_Value({f: Function}, {x: Number}) -> Number
    备注: 输入一个函数 f 以及变量的值，返回函数对应的值

26. Build_Function: Build_Function({f: Expression}, {x: Variable}) -> Function
    备注: 输入一个表达式 f 以及变量, 返回由这个表达式对应的函数

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

13. Get_Set_Sum: Get_Set_Sum({A: Set}) -> Real
    备注: 输入一个集合, 返回这个集合中所有元素的和(首先得能求和?)

14. Build_Set: Build_Set({x: VariableType}, {P(x): Proposition}) -> Set
    备注: 输入变量 x 满足的条件, 返回 x 构成的集合

15. Get_Set_Maximum: Get_Set_Maximum({A: Set}) -> Real
    备注: 输入一个集合, 返回这个集合中元素的最大值

16. Get_Set_Minimum: Get_Set_Minimum({B: Set}) -> Real
    备注: 输入一个集合, 返回这个集合中元素的最小值

17. Check_Set_Type: Check_Set_Type({A: Set}, {B: Concept}) -> Boolean
    备注: 检查一个集合的元素是否都属于某个 Concept

18. Get_Set_Product: Get_Set_Product({A: Set}) -> Real
    备注: 输入一个集合, 返回这个集合中所有元素的乘积(首先得能求乘积?)

19. Elements_In_Set: Elements_In_Set({A: Individual}, {B: Set}) -> Boolean
    备注: 判断某个具体的 Individual 是否属于某个 Set

20. Get_Set_Means: Get_Set_Means({A: Set}) -> Real
    备注: 输入一个集合, 返回这个集合中所有元素的均值

21. Get_Set_Count: Get_Set_Count({A: Set}) -> Set
    备注: 输入一个集合, 返回这个集合中元素出现的频率

22. Get_Sorted_Set: Get_Sorted_Set({A: Set}) -> Set
    备注: 输入一个集合, 返回排序好后的集合

23. Get_SetElement_Index: Get_SetElement_Byindex({A: Set}, {i: Number}) -> Element
    备注: 输入一个(排序好的)集合, 返回对应指标的元素



#### Probability (概率)

1. Probability: Probability({P: Event}) -> PositiveNumbers
    备注: 输入一个集合 Event, 返回一个正实数(对应的概率)



#### Angle (三角函数)

1. Get_Angle_DegreeMeasure: Get_Angle_DegreeMeasure({A: Angle}) -> DegreeMeasure
    备注: 输入一个角A, 返回它的度数(角度制)

2. Get_Angle_RadianMeasure: Get_Angle_RadianMeasure({A: Angle}) -> RadianMeasure
    备注: 输入一个角A, 返回它的弧度(弧度制)

3. Change_Degree_To_Radian: Change_Degree_To_Radian({D: DegreeMeasure}) -> RadianMeasure
    备注: 输入一个度数(角度制), 返回它的弧度(弧度制)

4. Change_Radian_To_Degree: Change_Radian_To_Degree({R: RadianMeasure}) -> DegreeMeasure
    备注: 输入一个弧度(弧度制), 返回它的角度(角度制)

5. Sin: Sin({A: Angle}) -> Real
    备注: 输入一个角度, 返回对应的正弦值

6. Cos: Cos({A: Angle}) -> Real
    备注: 输入一个角度, 返回对应的余弦值

7. Tan: Tan({A: Angle}) -> Real
    备注: 输入一个角度, 返回对应的正切值

8. Cot: Cot({A: Angle}) -> Real
    备注: 输入一个角度, 返回对应的余切值


#### Vector (向量)

1. Build_Plane_Vector: Build_Plane_Vector({A: Point}, {B: Point}) -> Vector
    备注: 输入平面直角坐标系两个点, 返回对应的向量

2. Build_ThreeDimension_Vector: Build_ThreeDimension_Vector({A: Point}, {B: Point}, {C: Point}) -> Vector
    备注: 输入空间直角坐标系三个点, 返回对应的向量

3. Get_Vector_Length: Get_Vector_Length({A: Vector}) -> PositiveNumbers
    备注: 输入一个向量, 返回它对应的模长

4. Is_Vector_Equal: Is_Vector_Equal({A: Vector}, {B: Vector}) -> Boolean
    备注: 输入两个向量, 判断它们是否相等

5. Is_Vector_Parallel: Is_Vector_Parallel({A: Vector}, {B: Vector}) -> Boolean
    备注: 输入两个向量, 判断它们是否平行

6. Get_ScalarMul_Vector: Get_ScalarMul_Vector({c: Real}, {A: Vector}) -> Vector
    备注: 输入一个标量(实数)和一个向量, 返回它们数乘的结果

7. Get_InnerProduct_Vector: Get_VectorMul_Vector({A: Vector}, {B: Vector}) -> Real
    备注: 输入两个向量, 返回它们做内积的结果



#### Statistics & Probability (概率统计)

1. Get_Dataset_Range: Get_Dataset_Range({D: Dataset}) -> Real
    备注: 输入一个数据集, 返回它的极差

2. Get_Dataset_Mean: Get_Dataset_Mean({D: Dataset}) -> Real
    备注: 输入一个数据集, 返回它的均值

3. Get_Dataset_Median: Get_Dataset_Median({D: Dataset}) -> Real
    备注: 输入一个数据集, 返回它的中位数

4. Get_Dataset_Mode: Get_Dataset_Mode({D: Dataset}) -> Real
    备注: 输入一个数据集, 返回它的众数

5. Get_Dataset_StandardDeviation: Get_Dataset_StandardDeviation({D: Dataset}) -> Real
    备注: 输入一个数据集, 返回它的标准差

6. Get_Dataset_Variance: Get_Dataset_Variance({D: Dataset}) -> Real
    备注: 输入一个数据集, 返回它的方差

7. Probability: Probability({P: Event}) -> PositiveNumbers
    备注: 输入一个集合 Event, 返回一个正实数(对应的概率, 0到1)

8. Is_Event_Exclusive: Is_Event_Exclusive({A: Event}, {B: Event}) -> Boolean
    备注: 输入两个事件 A, B; 判断它们是否互斥



#### Logic (逻辑相关)

1. Negation: Negation({a: Proposition}) -> Proposition
    备注: 对原命题进行取反

2. Build_Universal_Proposition: Build_Universal_Proposition({a: Set}, {b: Proposition}) -> Proposition
    备注: \forall x\in 集合a, x都满足命题b

3. Build_Exist_Proposition: Build_Exist_Proposition({a: Set}, {b: Proposition}) -> Proposition
    备注: \exist x\in 集合a, x满足命题b

4. And: And({a: Proposition}, {b: Proposition}) -> Proposition
    备注: 命题A 且 命题 B

5. Or: Or({a: Proposition}, {b: Proposition}) -> Proposition
    备注: 命题A 或 命题 B

6. Implication: Implication({p: Proposition}, {q: Proposition}) -> Proposition
    备注: 命题 P 蕴含 命题 Q

7. Equivalence: Equivalence({p: Proposition}, {q: Proposition}) -> Proposition
    备注: 命题 P 和命题 Q 等价








