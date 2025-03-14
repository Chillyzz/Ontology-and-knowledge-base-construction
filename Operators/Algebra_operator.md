(共100个 Operator)

### Numbers

1. Get_Number_Floor: Get_Number_Floor({x: Real}) -> Integer  # Get_Number_Floor(3.8) = 4 (向上取整)

2. Get_Number_Ceil: Get_Number_Ceil({x: Real}) -> Integer  # Get_Number_Ceil(3.8) = 4 (向下取整)

3. Get_Number_Round: Get_Number_Round({x: Real}) -> Integer # Get_Number_Round(4.1) = 4 (最接近的整数)  

4. Abs: Abs({a: Real}) -> NonNegativeNumbers # Abs(-3.5) = 3,5 (取绝对值)

5. Log: Log({x: Real}, {y: Real}) -> Real # Log({2: Real}, {4: Real}) = 2.   (Lean中的 Real.log)

6. Factorial：Factorial({x: NaturalNumbers}) -> NaturalNumbers : The product of all positive integers less than or equal to a given positive integer \(n\) as \(n!\).  
    - *Example*: \(5! = 5 \times 4 \times 3 \times 2 \times 1 = 120\).

7. Get_Combination: Get_Combination({x: NaturalNumbers}, {y: NaturalNumbers}): The coefficient of the term in the expansion of \( (x + y)^n \), as \( \binom{n}{k} \).  
    - *Example*: \( Get_Combination(5, 2) = \binom{5}{2} = \frac{5!}{2!(5-2)!} = 10 \).

### Equation and Expression

1. Solve_equation: Solve_equation({x: Variable}, {P: Equation}) -> Set # 输入一个等式和对应变量, 返回解集(可扩展到多元, 但方程个数必须等于变量数)

2. Solve_inequation: Solve_inequation({x: Variable}, {P: Inequation}) -> Set # 输入一个不等式和对应变量, 返回解集 (可扩展到多元, 但方程个数必须等于变量数)

3. Get_Value_Expression: Get_Value_Expression({P: Expression}) -> Number # 输入一个表达式(不含未知变量), 求它的值(Query时使用的算子)

4. Get_Expression_Maximum: Get_Expression_Maximum(f: Expression) -> Number # 输入一个表达式, 返回可能的最大值

5. Get_Expression_Minimum: Get_Expression_Minimum(f: Expression) -> Number # 输入一个表达式, 返回可能的最小值

### Polynomial(多项式)

1. Get_PolyDegree: Get_PolyDegree(x: Polynomial) -> Number # 输入一个多项式, 返回它的最高次幂

2. Get_Polyroots: Get_Polyroots(x: Polynomial) -> Set # 输入一个多项式, 返回它的根的集合

3. Get_Term_Coefficient: Get_Term_Coefficient({x: Polynomial}, {y: PolynomialTerm}) -> Number # 输入一个多项式和对应的某一项, 返回该项的系数

4. Get_PolyTerm: Get_PolyTerm(x: Polynomial) -> Set # 输入一个多项式, 返回它的项的集合

5. Get_ConstantTerm: Get_ConstantTerm(x: Polynomial) -> Number # 输入一个多项式, 返回它的常数项

6. Is_PolyFactor: IsPolyFactor({A: Polynomial}, {B: Polynomial}) -> Boolean # 输入两个多项式, 判断 A 是不是 B 的因子

7. Is_IrreduciblePolynomial: Is_IrreduciblePolynomial({A: Polynomial}) -> Boolean # 输入一个多项式, 判断是否可约

8. Get_PolyCoefficient: Get_PolyCoefficient(x: Polynomial) -> Set # 输入一个多项式, 返回它的系数集合

9. Eval_Value_Polynomial: Eval_Value_Expression({P: Polynomial(a)}, {x: Prop(a)}) -> Number # 输入一个多项式和变量在某处的值, 返回对应的值

### Sequence(数列)

1. Get_Sequence_Terms: Get_Sequence_Terms({s: Sequence}, {n: Integers}) -> ElementType # 输入一个数列和序号, 返回对应的数列元素

2. Build_Sequence: Build_Sequence({n: Variable}, {p: Expression}) -> Sequence # 输入数列的通项公式, 返回对应的数列

3. Is_ArithmeticSequence: Is_ArithmeticSequence({s: Sequence}) -> Boolean # 输入一个数列, 判断是不是等差数列

4. Is_GeometricSequence: Is_GeometricSequence({s: Sequence}) -> Boolean # 输入一个数列, 判断是不是等比数列

5. Is_MonotonicSequence: Is_MonotonicSequence({s: Sequence}) -> Boolean # 输入一个数列, 判断是不是单调数列

6. Get_CommonDifference: Get_CommonDifference({s: ArithmeticSequence}) -> Number # 输入一个等差数列, 返回它的公差

7. Get_CommonRatio: Get_CommonRatio({s: GeometricSequence}) -> Number # 输入一个等比数列, 返回它的公比

8. Is_Finite_Sequence: Is_Finite({s: Sequence}) -> Boolean # 输入一个数列，判断是不是有限的

9. Is_Monotonic_Increasing_Sequence: Is_Monotonic_Increasing_Sequence({s: Sequence}) -> Boolean # 判断一个数列是不是单调递增的

10. Is_Monotonic_Decreasing_Sequence: Is_Monotonic_Decreasing_Sequence({s: Sequence}) -> Boolean # 判断一个数列是不是单调递减的

11. Get_Sequences_Length: Get_Sequences_Length({s: Sequence}) -> PositiveInteger # 计算一个数列的元素个数

12. Get_Sequences_Sum: Get_Sequences_Sum({s: Sequence}, {i: Integer}) -> Number # 计算数列的前n项和


### Function

1. Function_Domain: Function_Domain(f: Function) -> Set
    备注: 表示一个函数的定义域集合(无法计算, 只能 Query或赋值)

2. Get_Function_Range: Get_Function_Range(f: Function) -> Set
    备注: 输入一个函数, 返回一个集合(它的值域)

3. Get_Function_Maximum: Get_Function_Maximum(f: Function) -> Number
    备注: 输入一个函数, 返回一个数字(它的最大值)

4. Get_Function_Minimum: Get_Function_Minimum(f: Function) -> Number
    备注: 输入一个函数, 返回一个数字(它的最小值)
 
5. Get_Function_Symmetry: Get_Function_Symmetry(f: Function) -> String  
    备注: 输入一个函数, 判断该函数是否具有对称性。返回字符串 "symmetrical" 或 "asymmetrical"。  

6. Get_Function_Zeroes: Get_Function_Zeroes(f: Function) -> Set  
    备注: 输入一个函数, 返回该函数的零点集合，即使得函数值为零的输入值集合。  

7. Is_Increasing_Function: Is_Increasing_Function({f: Function}, {D: Interval}) -> Boolean
    备注: 输入一个函数 f 和一个区间 D; 判断函数 f 在区间 D 上是否是增函数

8. Is_Decreasing_Function: Is_Decreasing_Function({f: Function}, {D: Interval}) -> Boolean
    备注: 输入一个函数 f 和一个区间 D; 判断函数 f 在区间 D 上是否是减函数

9. Is_OddFunction: Is_OddFunction(f: Function) -> Boolean
    备注: 输入一个函数 f ; 判断函数 f 在定义域上是否是奇函数

10. Is_EvenFunction: Is_EvenFunction(f: Function) -> Boolean
    备注: 输入一个函数 f ; 判断函数 f 在定义域上是否是偶函数

11. Get_Function_Composition: Get_Function_Composition({f: Function}, {g: Function}) -> Function
    备注: 输入两个函数 f g; 返回它们的复合函数 f(g(x))

12. Is_Periodic_Function: Is_Periodic_Function(f: Function) -> Boolean
    备注: 输入一个函数 f ; 判断函数 f 在定义域上是否是周期函数

13. Get_Function_Minimalperiod: Get_Function_Minimalperiod(f: Function) -> Real
    备注: 输入一个函数 f ; 返回它的最小正周期

14. Get_Function_CriticalPoint: Get_Function_CriticalPoint(f: Function) -> Set
    备注: 输入一个函数 f ; 返回它零点的集合

15. Get_Inverse_Function: Get_Inverse_Function(f: Function) -> Function
    备注: 输入一个函数 f ; 返回它的反函数

16. Get_Function_IthComposition: Get_Function_IthComposition({f: Function}, {i: Integer}) -> Function
    备注: 输入一个函数 f 以及它的复合次数 i; 返回它的复合函数 f^{i}(x)

17. Get_Function_Value: Get_Function_Value({f: Function}, {x: Number}) -> Number
    备注: 输入一个函数 f 以及变量的值，返回函数对应的值

18. Is_Bijection: Is_Bijection(f: Function) -> Boolean  
    备注: 输入一个函数 f ; 若 f 是双射（即同时是单射和满射），返回 true，否则返回 false  

19. Is_Injection: Is_Injection(f: Function) -> Boolean  
    备注: 输入一个函数 f ; 若 f 是单射（即任意 x₁ ≠ x₂ 都满足 f(x₁) ≠ f(x₂)），返回 true，否则返回 false  

20. Is_Surjection: Is_Surjection(f: Function) -> Boolean  
    备注: 输入一个函数 f ; 若 f 是满射（即对于 f 的值域中的每个 y，都存在 x 使得 f(x) = y），返回 true，否则返回 false 

21. Get_Quadratic_Discriminant: Get_Quadratic_Discriminant({P: Quadratic}) -> Number 
    备注：输入一个二次方程, 返回它的判别式

### Set

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

24. Is_Set_BoundedFromAbove: Is_Set_BoundedFromAbove({A: Set}) -> Boolean
    备注: 判断集合是否有上界

25. Is_Set_Unbounded: Is_Set_Unbounded({A: Set}) -> Boolean
    备注: 判断集合是否为无界


### Probability (概率)

1. Probability: Probability({P: Event}) -> PositiveNumbers
    备注: 输入一个集合 Event, 返回一个正实数(对应的概率)

### Angle (三角函数)

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


### Vector (向量)

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



### Statistics & Probability (概率统计)

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



### Logic (逻辑相关)

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
















