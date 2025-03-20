(代数 + 数论大约135个 Operator 可用)

### Numbers

1. Get_Number_Floor: Get_Number_Floor({x: Real}) -> Integer  # Get_Number_Floor(3.8) = 3 (向下取整)

2. Get_Number_Ceil: Get_Number_Ceil({x: Real}) -> Integer  # Get_Number_Ceil(3.8) = 4 (向上取整)

3. Get_Number_Round: Get_Number_Round({x: Real}) -> Integer # Get_Number_Round(4.1) = 4 (最接近的整数)  

4. Abs: Abs({a: Real}) -> NonNegativeNumbers # Abs(-3.5) = 3,5 (取绝对值)

5. Log: Log({x: Real}, {y: Real}) -> Real # Log({2: Real}, {4: Real}) = 2.   (Lean中的 Real.logb)

6. NaturalLog: NaturalLog({x: Real}) -> Real # Log(e^2) = 2.   (Lean中的 Real.log)

7. Factorial：Factorial({x: NaturalNumbers}) -> NaturalNumbers : The product of all positive integers less than or equal to a given positive integer \(n\) as \(n!\).  
    - *Example*: \(5! = 5 \times 4 \times 3 \times 2 \times 1 = 120\).

8. Get_Combination: Get_Combination({x: NaturalNumbers}, {y: NaturalNumbers}): The coefficient of the term in the expansion of \( (x + y)^n \), as \( \binom{n}{k} \).  
    - *Example*: \( Get_Combination(5, 2) = \binom{5}{2} = \frac{5!}{2!(5-2)!} = 10 \).

9. Get_Reciprocal: Get_Reciprocal({x: Real}) -> Real:  A number that, when multiplied by the original number, results in 1.  
    *Example:* The reciprocal of \(4\) is \(\frac{1}{4}\).

10. Get_Sum({S: Finset}, {L: LamdaExpression}) -> ℝ     # Get_Sum (Set.Icc 1 10).toFinset (λ x : ℕ => x ^ 2 + 1)

11. Get_Prod({S: Finset}, {L: LamdaExpression}) -> ℝ    # Get_Prod (Set.Icc 1 10).toFinset (λ x : ℕ => x ^ 2 + 1)

12. Exp: Exp({x: Real}) -> Real     # Exp(e ^ 2) = 2

### Equation and Expression

1. Solve_equation: Solve_equation({x: Variable}, {P: Equation}) -> Set # 输入一个等式和对应变量, 返回解集(可扩展到多元, 但方程个数必须等于变量数)

2. Solve_inequation: Solve_inequation({x: Variable}, {P: Inequation}) -> Set # 输入一个不等式和对应变量, 返回解集 (可扩展到多元, 但方程个数必须等于变量数)

3. Get_Value_Expression: Get_Value_Expression({P: Expression}) -> Number # 输入一个表达式(不含未知变量), 求它的值(Query时使用的算子)


### Polynomial(多项式)

1. Get_PolyDegree: Get_PolyDegree(x: Polynomial) -> Number # 输入一个多项式, 返回它的最高次幂

2. Get_Polyroots: Get_Polyroots(x: Polynomial) -> Set # 输入一个多项式, 返回它的根的集合

3. Get_Term_Coefficient: Get_Term_Coefficient({x: Polynomial}, {y: NaturalNumber}) -> Real # 输入一个多项式和对应的项次数, 返回该项的系数

4. Get_PolyTerm: Get_PolyTerm(x: Polynomial) -> Set # 输入一个多项式, 返回它的项的集合

5. Get_ConstantTerm: Get_ConstantTerm(x: Polynomial) -> Number # 输入一个多项式, 返回它的常数项

6. Is_PolyFactor: IsPolyFactor({A: Polynomial}, {B: Polynomial}) -> Boolean # 输入两个多项式, 判断 A 是不是 B 的因子

7. Is_IrreduciblePolynomial: Is_IrreduciblePolynomial({A: Polynomial}) -> Boolean # 输入一个多项式, 判断是否可约

8. Get_PolyCoefficient: Get_PolyCoefficient(x: Polynomial) -> Set # 输入一个多项式, 返回它的系数集合

9. Eval_Value_Polynomial: Eval_Value_Expression({P: Polynomial}, {x: Number}) -> Number # 输入一个多项式和变量在某处的值, 返回对应的值

10. Solve_equation: Solve_equation({x: Variable}, {P: Equation}) -> Set # 输入一个等式和对应变量, 返回解集(可扩展到多元, 但方程个数必须等于变量数)

11. Solve_inequation: Solve_inequation({x: Variable}, {P: Inequation}) -> Set # 输入一个不等式和对应变量, 返回解集 (可扩展到多元, 但方程个数必须等于变量数)

12. Is_Polynomial_Root: Is_Polynomial_Root({P: Polynomial}, {x: Number}) -> Boolean # 判断 x 是不是多项式 P 的根

13. Get_Polynomial_Composition: Get_Polynomial_Composition({f: Polynomial}, {g: Polynomial}) -> Polynomial

14. Get_Polynomial_Leading_Coefficient: Get_Polynomial_Leading_Coefficient(x: Polynomial) -> Number # 输入一个多项式, 返回最高项系数

### Sequence(数列)

-- 1. Get_Sequence_Terms: Get_Sequence_Terms({s: Sequence}, {n: Integers}) -> ElementType
--    获取数列的第 `n` 项

-- 2. Get_Sequence_Sum: Get_Sequences_Sum({s: Sequence}, {i: Integer}) -> Number
--    获取数列前 `i` 项的和

-- 3. Is_ArithmeticSequence: Is_ArithmeticSequence({s: Sequence}) -> Boolean
--    判断数列是否为等差数列

-- 4. Is_GeometricSequence: Is_GeometricSequence({s: Sequence}) -> Boolean
--    判断数列是否为等比数列

-- 5. Is_MonotonicSequence: Is_MonotonicSequence({s: Sequence}) -> Boolean
--    判断数列是否为单调数列

-- 6. Get_CommonDifference: Get_CommonDifference({s: ArithmeticSequence}) -> Number
--    获取等差数列的公差

-- 7. Get_CommonRatio: Get_CommonRatio({s: GeometricSequence}) -> Number
--    获取等比数列的公比

-- 8. Is_Monotonic_Increasing_Sequence: Is_Monotonic_Increasing_Sequence({s: Sequence}) -> Boolean
--    判断数列是否为单调递增数列

-- 9. Is_Monotonic_Decreasing_Sequence: Is_Monotonic_Decreasing_Sequence({s: Sequence}) -> Boolean
--    判断数列是否为单调递减数列

-- 10. Get_FiniteSequences_Length: Get_FiniteSequences_Length({s: Sequence}) -> PositiveInteger
--     获取有限数列的长度

-- 11. Get_Sequence_Infinite_Sum: Get_Sequence_Infinite_Sum({s: Sequence}) -> Real
--     获取数列的无限求和

### Function

-- 1. Get_Function_Range: Get_Function_Range(f: Function) -> Set

-- 2. Get_Function_Maximum: Get_Function_Maximum(f: Function) -> Number

-- 3. Get_Function_Minimum: Get_Function_Minimum(f: Function) -> Number

-- 4. Get_Function_Symmetry: Get_Function_Symmetry(f: Function) -> String

-- 5. Get_Function_Zeroes: Get_Function_Zeroes(f: Function) -> Set

-- 6. Get_Function_Composition: Get_Function_Composition({f: Function}, {g: Function}) -> Function

-- 7. Get_Function_Minimalperiod: Get_Function_Minimalperiod(f: Function) -> Real

-- 8. Get_Inverse_Function: Get_Inverse_Function(f: Function) -> Function

-- 9. Get_Function_IthComposition: Get_Function_IthComposition({f: Function}, {i: Integer}) -> Function

-- 10. Get_Function_Value: Get_Function_Value({f: Function}, {x: Number}) -> Number

-- 11. Is_Bijection: Is_Bijection(f: Function) -> Boolean

-- 12. Is_Injection: Is_Injection(f: Function) -> Boolean

-- 13. Is_Surjection: Is_Surjection(f: Function) -> Boolean

-- 14. Get_QuadraticFunction_Discriminant: Get_QuadraticFunction_Discriminant(f: QuadraticFunction) -> Real # 求二次函数的判别式

-- 15. Get_Function_Expression: Get_Function_Expression(f: Function) -> Expression # 获取函数的表达式

-- 16. Get_StepFunction_Expression: Get_StepFunction_Expression({f: Function}, {P: Proposition}) -> Expression

-- 17. Is_Function_Root: Is_Function_Root({P: Function}, {x: Number}) -> Boolean # 判断 x 是不是多项式 P 的根

-- 18. Get_Function_InDomain_Range: Get_Function_InDomain_Range({f: Function}, {A: Set}) -> Set # 求函数在集合A下的像 B


### Set

-- 1. Set_Union: Set_Union({A: Set}, {B: Set}) -> Set  

-- 2. Set_Intersection: Set_Intersection({A: Set}, {B: Set}) -> Set  

-- 3. Set_Difference: Set_Difference({A: Set}, {B: Set}) -> Set  

-- 4. Set_SymmetricDifference: Set_SymmetricDifference({A: Set}, {B: Set}) -> Set  

-- 5. Set_Subset: Set_Subset({A: Set}, {B: Set}) -> Boolean  

-- 6. Set_ProperSubset: Set_ProperSubset({A: Set}, {B: Set}) -> Boolean  

-- 7. Set_Superset: Set_Superset({A: Set}, {B: Set}) -> Boolean  

-- 8. Set_ProperSuperset: Set_ProperSuperset({A: Set}, {B: Set}) -> Boolean  

-- 9. Set_Cardinality: Set_Cardinality({A: Set}) -> Number  

-- 10. Set_PowerSet: Set_PowerSet({A: Set}) -> Set  

-- 11. Set_Complement: Set_Complement({A: Set}, {U: Set}) -> Set  

-- 12. Set_Equality: Set_Equality({A: Set}, {B: Set}) -> Boolean  

-- 13. Get_Set_Sum: Get_Set_Sum({A: Set}) -> Real  

-- 14. Get_Set_Product: Get_Set_Product({A: Set}) -> Real  

-- 15. Build_Set: Build_Set({x: VariableType}, {P(x): Proposition}) -> Set  

-- 16. Get_Set_Maximum: Get_Set_Maximum({A: Set}) -> Real  

-- 17. Get_Set_Minimum: Get_Set_Minimum({B: Set}) -> Real  

-- 18. Elements_In_Set: Elements_In_Set({A: Individual}, {B: Set}) -> Boolean  

-- 19. Get_Set_Means: Get_Set_Means({A: Set}) -> Real  

-- 20. Is_Set_BoundedFromAbove: Is_Set_BoundedFromAbove({A: Set}) -> Boolean  

-- 21. Is_Set_Unbounded: Is_Set_Unbounded({A: Set}) -> Boolean  

-- 22. Get_UniversalSet: Get_UniversalSet({A: Concept}) -> Set # The set that contains all the elements under consideration for a particular context.  

-- 23. Get_Set_Inf  

-- 24. Get_Set_Sup  

-- 25. Range: Range({a: NaturalNumber}, {b: NaturalNumber}) -> FiniteSet         #备注: Range(a, b) = {a, a + 1, ... , b} ⊆ ℕ; a < b 时合法; 用于求和时书写对应集合  

-- 26. Get_Open_Interval(a: Number, b: Number) -> Interval  

-- 27. Get_LeftClosedRightOpen_Interval(a: Number, b: Number) -> Interval  

-- 28. Get_LeftOpenRightClosed_Interval(a: Number, b: Number) -> Interval  

-- 29. Get_Closed_Interval(a: Number, b: Number) -> Interval  

-- 30. Get_RightOpen_Interval(b: Number) -> Interval  

-- 31. Get_RightClosed_Interval(b: Number) -> Interval  

-- 32. Get_LeftOpen_Interval(a: Number) -> Interval  

-- 33. Get_LeftClosed_Interval(a: Number) -> Interval  



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

8. Build_UniqueExist_Proposition: Build_UniqueExist_Proposition({a: Set}, {b: Proposition}) -> Proposition
    备注: 存在唯一 x\in 集合a, x满足命题b


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



### Probability (概率)

1. Probability: Probability({P: Event}) -> PositiveNumbers
    备注: 输入一个集合 Event, 返回一个正实数(对应的概率)

