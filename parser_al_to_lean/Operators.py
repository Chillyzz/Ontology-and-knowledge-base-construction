def operator_to_lean(operator, *args):
    """
    根据不同的Operator ID执行相应的转换
    
    参数:
    operator (str): 操作符ID
    *args: 可变参数，根据不同的operator接收不同参数
    
    返回:
    str: 转换后的结果字符串
    """
    if operator == "Solve_inequation":
            if len(args) != 2:
                return "Solve_inequation operator requires exactly 2 arguments (declaration, term)"
            declaration, term = args
            # declartion, term 还需要再一次解析，此处先假设已经转换完成
            return f"{{ {declaration} | {term} }}"
    elif operator == "Abs":
        if len(args) != 1:
            return "Abs operator requires exactly 1 argument: term"
        term = args[0]
        return f"(|{term}|)"
    
    elif operator == "Sqrt":
        if len(args) != 1:
            return "Sqrt operator requires exactly 1 argument: term"
        term = args[0]
        return f"(Real.sqrt ({term}))"
    
    elif operator == "Get_Number_Floor":
        if len(args) != 1:
            return "Get_Number_Floor operator requires exactly 1 argument: x"
        x = args[0]
        return f"⌊({x}: Real)⌋"
    
    elif operator == "Get_Number_Ceil":
        if len(args) != 1:
            return "Get_Number_Ceil operator requires exactly 1 argument: x"
        x = args[0]
        return f"⌈({x}: Real)⌉"
    
    elif operator == "Get_Number_Round":
        if len(args) != 1:
            return "Get_Number_Round operator requires exactly 1 argument: x"
        x = args[0]
        return f"round (({x}: Real))"
    
    elif operator == "Log":
        if len(args) != 2:
            return "Log operator requires exactly 2 arguments: x, y"
        x, y = args
        return f"Real.logb {x} {y}"
    
    elif operator == "NaturalLog":
        if len(args) != 1:
            return "NaturalLog operator requires exactly 1 argument: x"
        x = args[0]
        return f"Real.log {x}"
    
    elif operator == "Factorial":
        if len(args) != 1:
            return "Factorial operator requires exactly 1 argument: x"
        x = args[0]
        return f"Nat.factorial {x}"
    
    elif operator == "Get_Combination":
        if len(args) != 2:
            return "Get_Combination operator requires exactly 2 arguments: x, y"
        x, y = args
        return f"{x}.choose {y}"
    
    elif operator == "Get_Reciprocal":
        if len(args) != 1:
            return "Get_Reciprocal operator requires exactly 1 argument: x"
        x = args[0]
        return f"{x}⁻¹"
    
    elif operator == "Get_Sum":
        if len(args) != 3:
            return "Get_Sum operator requires exactly 2 arguments: S, L"
        S, i, L = args
        return f"(∑ {i} ∈ {S}, {L})"
    
    elif operator == "Get_Prod":
        if len(args) != 3:
            return "Get_Prod operator requires exactly 2 arguments: S, L"
        S, i, L = args
        return f"(∏ {i} ∈ {S}, {L})"
    
    elif operator == "Exp":
        if len(args) != 1:
            return "Exp operator requires exactly 1 argument: x"
        x = args[0]
        return f"exp {x}"
    
    elif operator == "Cos":
        if len(args) != 1:
            return "Exp operator requires exactly 1 argument: x"
        x = args[0]
        return f"Real.cos ({x})"
    
    elif operator == "Sin":
        if len(args) != 1:
            return "Exp operator requires exactly 1 argument: x"
        x = args[0]
        return f"Real.sin ({x})"
    
    elif operator == "Get_PolyDegree":
        if len(args) != 1:
            return "Get_PolyDegree operator requires exactly 1 argument: x"
        x = args[0]
        return f"{x}.natDegree"
    
    elif operator == "Get_Polyroots":
        if len(args) != 1:
            return "Get_Polyroots operator requires exactly 1 argument: x"
        x = args[0]
        return f"{x}.roots"
    
    elif operator == "Get_Term_Coefficient":
        if len(args) != 2:
            return "Get_Term_Coefficient operator requires exactly 2 arguments: x, y"
        x, y = args
        return f"{x}.coeff {y}"
    
    elif operator == "Get_PolyTerm":
        if len(args) != 1:
            return "Get_PolyTerm operator requires exactly 1 argument: x"
        x = args[0]
        return f"monomial 2 ({x}.coeff 2)"
    
    elif operator == "Get_ConstantTerm":
        if len(args) != 1:
            return "Get_ConstantTerm operator requires exactly 1 argument: x"
        x = args[0]
        return f"{x}.coeff 0"
    
    elif operator == "Is_PolyFactor":
        if len(args) != 2:
            return "Is_PolyFactor operator requires exactly 2 arguments: A, B"
        A, B = args
        return f"{A} ∣ {B}"
    
    elif operator == "Is_IrreduciblePolynomial":
        if len(args) != 1:
            return "Is_IrreduciblePolynomial operator requires exactly 1 argument: A"
        A = args[0]
        return f"Irreducible {A}"
    
    elif operator == "Get_PolyCoefficient":
        if len(args) != 1:
            return "Get_PolyCoefficient operator requires exactly 1 argument: x"
        x = args[0]
        return f"{x}.coeffs"
    
    elif operator == "Eval_Value_Polynomial":
        if len(args) != 2:
            return "Eval_Value_Polynomial operator requires exactly 2 arguments: P, x"
        P, x = args
        return f"eval {x} {P}"
    
    elif operator == "Solve_equation":
        if len(args) != 2:
            return "Solve_equation operator requires exactly 2 arguments: x, P"
        x, P = args
        return f"{{ {x} | {P} }}"
    
    elif operator == "Is_Polynomial_Root":
        if len(args) != 2:
            return "Is_Polynomial_Root operator requires exactly 2 arguments: P, x"
        P, x = args
        return f"IsRoot {P} {x}"
    
    elif operator == "Get_Polynomial_Composition":
        if len(args) != 2:
            return "Get_Polynomial_Composition operator requires exactly 2 arguments: f, g"
        f, g = args
        return f"comp {f} {g}"
    
    elif operator == "Get_Polynomial_Leading_Coefficient":
        if len(args) != 1:
            return "Get_Polynomial_Leading_Coefficient operator requires exactly 1 argument: x"
        x = args[0]
        return f"{x}.leadingCoeff"
    
    elif operator == "Get_Sequence_Terms":
        if len(args) != 2:
            return "Get_Sequence_Terms operator requires exactly 2 arguments: s, n"
        s, n = args
        return f"{s} {n}"
    
    elif operator == "Get_Sequences_Sum":
        if len(args) != 2:
            return "Get_Sequences_Sum operator requires exactly 2 arguments: s, i"
        s, i = args
        return f"∑ n ∈ Finset.Icc 1 {i}, {s} n"
    
    elif operator == "Is_ArithmeticSequence":
        if len(args) != 1:
            return "Is_ArithmeticSequence operator requires exactly 1 argument: s"
        s = args[0]
        return f"∃ d : ℝ, ∀ n : ℕ, {s} (n + 1) - {s} n = d"
    
    elif operator == "Is_GeometricSequence":
        if len(args) != 1:
            return "Is_GeometricSequence operator requires exactly 1 argument: s"
        s = args[0]
        return f"∃ q : ℝ, ∀ n : ℕ, {s} (n + 1) / {s} n = q"
    
    elif operator == "Is_MonotonicSequence":
        if len(args) != 1:
            return "Is_MonotonicSequence operator requires exactly 1 argument: s"
        s = args[0]
        return f"Monotone {s} ∨ Antitone {s}"
    
    elif operator == "Get_CommonDifference":
        if len(args) != 1:
            return "Get_CommonDifference operator requires exactly 1 argument: s"
        s = args[0]
        return f"{s}.d"
    
    elif operator == "Get_CommonRatio":
        if len(args) != 1:
            return "Get_CommonRatio operator requires exactly 1 argument: s"
        s = args[0]
        return f"{s}.q"
    
    elif operator == "Is_Monotonic_Increasing_Sequence":
        if len(args) != 1:
            return "Is_Monotonic_Increasing_Sequence operator requires exactly 1 argument: s"
        s = args[0]
        return f"StrictMonoOn {s}"
    
    elif operator == "Is_Monotonic_Decreasing_Sequence":
        if len(args) != 1:
            return "Is_Monotonic_Decreasing_Sequence operator requires exactly 1 argument: s"
        s = args[0]
        return f"StrictAntiOn {s}"
    
    elif operator == "Get_FiniteSequences_Length":
        if len(args) != 1:
            return "Get_FiniteSequences_Length operator requires exactly 1 argument: s"
        s = args[0]
        return f"{s}.length"
    
    elif operator == "Get_Function_Expression":
        if len(args) != 1:
            return "Get_Function_Expression operator requires exactly 1 argument: f"
        f = args[0]
        return f"{f}"
    
    elif operator == "Get_Function_Range":
        if len(args) != 1:
            return "Get_Function_Range operator requires exactly 1 argument: f"
        f = args[0]
        return f"Set.range {f}"
    
    elif operator == "Get_Function_Maximum":
        if len(args) != 1:
            return "Get_Function_Maximum operator requires exactly 1 argument: f"
        f = args[0]
        return f"sSup (Set.range {f})"
    
    elif operator == "Get_Function_Minimum":
        if len(args) != 1:
            return "Get_Function_Minimum operator requires exactly 1 argument: f"
        f = args[0]
        return f"sInf (Set.range {f})"
    
    elif operator == "Get_Function_Zeroes":
        if len(args) != 1:
            return "Get_Function_Zeroes operator requires exactly 1 argument: f"
        f = args[0]
        return f"{{ x | {f} x = 0 }}"
    
    elif operator == "Get_Function_Composition":
        if len(args) != 2:
            return "Get_Function_Composition operator requires exactly 2 arguments: f, g"
        f, g = args
        return f"{f} ∘ {g}"
    
    elif operator == "Get_Function_Minimalperiod":
        if len(args) != 1:
            return "Get_Function_Minimalperiod operator requires exactly 1 argument: f"
        f = args[0]
        return f"sInf {{T: ℝ | T > 0 ∧ (∀ x, {f} (x + T) = {f} x)}}"
    
    elif operator == "Get_Inverse_Function":
        if len(args) != 1:
            return "Get_Inverse_Function operator requires exactly 1 argument: f"
        f = args[0]
        return f"{f}⁻¹"
    
    elif operator == "Get_Function_IthComposition":
        if len(args) != 2:
            return "Get_Function_IthComposition operator requires exactly 2 arguments: f, i"
        f, i = args
        return f"{f}^[{i}]"
    
    elif operator == "Get_Function_Value":
        if len(args) != 2:
            return "Get_Function_Value operator requires exactly 2 arguments: f, x"
        f, x = args
        return f"({f}) {x}"

    # 新增函数相关算子
    elif operator == "Is_Bijection":
        if len(args) != 1:
            return "Is_Bijection operator requires exactly 1 argument: f"
        f = args[0]
        return f"Function.Bijective {f}"
    
    elif operator == "Is_Injection":
        if len(args) != 1:
            return "Is_Injection operator requires exactly 1 argument: f"
        f = args[0]
        return f"Function.Injective {f}"
    
    elif operator == "Is_Surjection":
        if len(args) != 1:
            return "Is_Surjection operator requires exactly 1 argument: f"
        f = args[0]
        return f"Function.Surjective {f}"
    
    elif operator == "Get_QuadraticFunction_Discriminant":
        if len(args) != 1:
            return "Get_QuadraticFunction_Discriminant operator requires exactly 1 argument: A"
        A = args[0]
        return f"{A}.discriminant"
    
    # 集合相关算子
    elif operator == "Set_Union":
        if len(args) != 2:
            return "Error: Set_Union operator requires exactly 2 arguments: A, B"
        A, B = args
        return f"{A} ∪ {B}"

    elif operator == "Set_Intersection":
        if len(args) != 2:
            return "Error: Set_Intersection operator requires exactly 2 arguments: A, B"
        A, B = args
        return f"{A} ∩ {B}"

    elif operator == "Set_Difference":
        if len(args) != 2:
            return "Error: Set_Difference operator requires exactly 2 arguments: A, B"
        A, B = args
        return f"{A} \\ {B}"

    elif operator == "Set_SymmetricDifference":
        if len(args) != 2:
            return "Error: Set_SymmetricDifference operator requires exactly 2 arguments: A, B"
        A, B = args
        return f"symmDiff {A} {B}"

    elif operator == "Set_Subset":
        if len(args) != 2:
            return "Error: Set_Subset operator requires exactly 2 arguments: A, B"
        A, B = args
        return f"{A} ⊆ {B}"

    elif operator == "Set_ProperSubset":
        if len(args) != 2:
            return "Error: Set_ProperSubset operator requires exactly 2 arguments: A, B"
        A, B = args
        return f"{A} ⊂ {B}"

    elif operator == "Set_Superset":
        if len(args) != 2:
            return "Error: Set_Superset operator requires exactly 2 arguments: A, B"
        A, B = args
        return f"{A} ⊇ {B}"

    elif operator == "Set_ProperSuperset":
        if len(args) != 2:
            return "Error: Set_ProperSuperset operator requires exactly 2 arguments: A, B"
        A, B = args
        return f"{A} ⊃ {B}"

    elif operator == "Set_Cardinality":
        if len(args) != 1:
            return "Error: Set_Cardinality operator requires exactly 1 argument: A"
        A = args[0]
        return f"{A}.card"

    elif operator == "Set_PowerSet":
        if len(args) != 1:
            return "Error: Set_PowerSet operator requires exactly 1 argument: A"
        A = args[0]
        return f"𝒫 {A}"

    elif operator == "Set_Complement":
        if len(args) != 1:
            return "Error: Set_Complement operator requires exactly 1 argument: A"
        A = args[0]
        return f"{A}ᶜ"

    elif operator == "Set_Equality":
        if len(args) != 2:
            return "Error: Set_Equality operator requires exactly 2 arguments: A, B"
        A, B = args
        return f"{A} = {B}"

    elif operator == "Get_Set_Sum":
        if len(args) != 1:
            return "Error: Get_Set_Sum operator requires exactly 1 argument: A"
        A = args[0]
        return f"∑ i ∈ {A}.toFinset, i"

    elif operator == "Get_Set_Product":
        if len(args) != 1:
            return "Error: Get_Set_Product operator requires exactly 1 argument: A"
        A = args[0]
        return f"∏ i ∈ {A}, i"

    elif operator == "Build_Set":
        if len(args) != 2:
            return "Error: Build_Set operator requires exactly 2 arguments: x, P"
        x, P = args
        return f"{{{x} | {P}}}"

    elif operator == "Get_Set_Maximum":
        if len(args) != 1:
            return "Error: Get_Set_Maximum operator requires exactly 1 argument: A"
        A = args[0]
        return f"sSup {A}"

    elif operator == "Get_Set_Minimum":
        if len(args) != 1:
            return "Error: Get_Set_Minimum operator requires exactly 1 argument: A"
        A = args[0]
        return f"sInf {A}"

    elif operator == "Elements_In_Set":
        if len(args) != 2:
            return "Error: Elements_In_Set operator requires exactly 2 arguments: A, B"
        A, B = args
        return f"{A} ∈ {B}"

    elif operator == "Get_Set_Means":
        if len(args) != 1:
            return "Error: Get_Set_Means operator requires exactly 1 argument: s"
        s = args[0]
        return f"(∑ i ∈ {s}, i )/({s}.toFinset.card)"

    elif operator == "Is_Set_BoundedFromAbove":
        if len(args) != 1:
            return "Error: Is_Set_BoundedFromAbove operator requires exactly 1 argument: A"
        A = args[0]
        return f"Set.Bounded Nat.le {A}"

    elif operator == "Is_Set_Unbounded":
        if len(args) != 1:
            return "Error: Is_Set_Unbounded operator requires exactly 1 argument: A"
        A = args[0]
        return f"Set.Unbounded Nat.le {A}"

    elif operator == "Get_UniversalSet":
        if len(args) != 0:
            return "Error: Get_UniversalSet operator requires no arguments"
        return "Set.univ"

    # 区间相关算子
    elif operator == "Range":
        if len(args) != 2:
            return "Error: Range operator requires exactly 2 arguments: a, b"
        a, b = args
        return f"Finset.Icc {a} {b}"

    elif operator == "Get_Open_Interval":
        if len(args) != 2:
            return "Error: Get_Open_Interval operator requires exactly 2 arguments: a, b"
        a, b = args
        return f"Set.Ioo {a} {b}"

    elif operator == "Get_LeftClosedRightOpen_Interval":
        if len(args) != 2:
            return "Error: Get_LeftClosedRightOpen_Interval operator requires exactly 2 arguments: a, b"
        a, b = args
        return f"Set.Ico {a} {b}"

    elif operator == "Get_LeftOpenRightClosed_Interval":
        if len(args) != 2:
            return "Error: Get_LeftOpenRightClosed_Interval operator requires exactly 2 arguments: a, b"
        a, b = args
        return f"Set.Ioc {a} {b}"

    elif operator == "Get_Closed_Interval":
        if len(args) != 2:
            return "Error: Get_Closed_Interval operator requires exactly 2 arguments: a, b"
        a, b = args
        return f"Set.Icc {a} {b}"

    elif operator == "Get_RightOpen_Interval":
        if len(args) != 1:
            return "Error: Get_RightOpen_Interval operator requires exactly 1 argument: b"
        b = args[0]
        return f"Set.Iio {b}"

    elif operator == "Get_RightClosed_Interval":
        if len(args) != 1:
            return "Error: Get_RightClosed_Interval operator requires exactly 1 argument: b"
        b = args[0]
        return f"Set.Iic {b}"

    elif operator == "Get_LeftOpen_Interval":
        if len(args) != 1:
            return "Error: Get_LeftOpen_Interval operator requires exactly 1 argument: a"
        a = args[0]
        return f"Set.Ioi {a}"

    elif operator == "Get_LeftClosed_Interval":
        if len(args) != 1:
            return "Error: Get_LeftClosed_Interval operator requires exactly 1 argument: a"
        a = args[0]
        return f"Set.Ici {a}"

    # 数字处理相关算子
    elif operator == "Get_Digit":
        if len(args) == 1:
            n = args[0]
            return f"Nat.digits 10 {n}"
        elif len(args) == 2:
            base, n = args
            return f"Nat.digits {base} {n}"
        else:
            return "Error: Get_Digit operator requires 1 or 2 arguments: [base], n"

    elif operator == "Covert_Digit_To_Number":
        if len(args) == 1:
            L = args[0]
            return f"Nat.ofDigits 10 {L}"
        elif len(args) == 2:
            base, L = args
            return f"Nat.ofDigits {base} {L}"
        else:
            return "Error: Covert_Digit_To_Number operator requires 1 or 2 arguments: [base], L"
    
    elif operator == "Get_DigitCount":
        if len(args) == 1:
            n = args[0]
            return f"(Nat.digits 10 {n}).length"
        elif len(args) == 2:
            base, n = args
            return f"(Nat.digits {base} {n}).length"
        else:
            return "Error: Get_DigitCount operator requires 1 or 2 arguments: [base], n"
    
    elif operator == "Get_DigitProduct":
        if len(args) == 1:
            L = args[0]
            return f"List.foldl (λ (x:ℕ) (y:ℕ) => x * y) 1 {L}"
        elif len(args) == 2:
            base, n = args
            return f"List.foldl (λ (x:ℕ) (y:ℕ) => x * y) 1 (Nat.digits {base} {n})"
        else:
            return "Error: Get_DigitProduct operator requires 1 or 2 arguments: [base], n"
    
    elif operator == "Get_DigitSum":
        if len(args) == 1:
            L = args[0]
            return f"List.foldl (λ (x:ℕ) (y:ℕ) => x + y) 0 {L}"
        elif len(args) == 2:
            base, n = args
            return f"List.foldl (λ (x:ℕ) (y:ℕ) => x + y) 0 (Nat.digits {base} {n})"
        else:
            return "Error: Get_DigitSum operator requires 1 or 2 arguments: [base], n"
    
    elif operator == "Is_PandigitalNumber":
        if len(args) != 1:
            return "Error: Is_PandigitalNumber operator requires exactly 1 argument: L"
        L = args[0]
        return f"(∀ d : ℕ, d ∈ (Finset.range 10) → d ∈ {L})"
    
    elif operator == "Is_PalindromeNumber":
        if len(args) != 1:
            return "Error: Is_PalindromeNumber operator requires exactly 1 argument: L"
        L = args[0]
        return f"(Nat.digits 10 {L}).Palindrome"
    
    elif operator == "Get_Ones_Digit":
        if len(args) == 1:
            n = args[0]
            return f"Nat.ofDigits 10 [(Nat.digits 10 {n}).head!]"
        elif len(args) == 2:
            base, n = args
            return f"Nat.ofDigits {base} [(Nat.digits {base} {n}).head!]"
        else:
            return "Error: Get_Ones_Digit operator requires 1 or 2 arguments: [base], n"
    
    # 数论相关算子
    elif operator == "Is_Nat_Mod":
        if len(args) != 3:
            return "Error: Is_Nat_Mod operator requires exactly 3 arguments: a, b, n"
        a, b, n = args
        return f"({a} ≡ {b} [MOD {n}])"
    
    elif operator == "Get_InverseMod":
        if len(args) != 2:
            return "Error: Get_InverseMod operator requires exactly 2 arguments: a, m"
        a, m = args
        return f"∃ x : ℕ, {a} * x ≡ 1 [MOD {m}]"
    
    elif operator == "Get_FractionalPart":
        if len(args) != 1:
            return "Error: Get_FractionalPart operator requires exactly 1 argument: x"
        x = args[0]
        return f"Int.fract {x}"
    
    elif operator == "Get_IntegerPart":
        if len(args) != 1:
            return "Error: Get_IntegerPart operator requires exactly 1 argument: x"
        x = args[0]
        return f"Int.floor {x}"
    
    elif operator == "Get_LeastCommonDenominator":
        if len(args) != 2:
            return "Error: Get_LeastCommonDenominator operator requires exactly 2 arguments: q1, q2"
        q1, q2 = args
        return f"Nat.lcm {q1}.den {q2}.den"
    
    elif operator == "Get_Mediant":
        if len(args) != 2:
            return "Error: Get_Mediant operator requires exactly 2 arguments: q1, q2"
        q1, q2 = args
        return f"({q1}.num + {q2}.num) / ({q1}.den + {q2}.den)"
    
    elif operator == "UnitFraction":
        if len(args) != 1:
            return "Error: UnitFraction operator requires exactly 1 argument: q"
        q = args[0]
        return f"({q}.num = 1) ∧ ({q}.den > 0)"
    
    elif operator == "Is_ProperFraction":
        if len(args) != 1:
            return "Error: Is_ProperFraction operator requires exactly 1 argument: q"
        q = args[0]
        return f"{q}.num < {q}.den"
    
    elif operator == "Is_IrreducibleFraction":
        if len(args) != 1:
            return "Error: Is_IrreducibleFraction operator requires exactly 1 argument: q"
        q = args[0]
        return f"Int.gcd {q}.num {q}.den = 1"
    
    elif operator == "Is_Coprime":
        if len(args) != 2:
            return "Error: Is_Coprime operator requires exactly 2 arguments: m, n"
        m, n = args
        return f"Nat.Coprime {m} {n}"
    
    elif operator == "Is_Factor":
        if len(args) != 2:
            return "Error: Is_Factor operator requires exactly 2 arguments: a, b"
        a, b = args
        return f"{a} ∣ {b}"
    
    elif operator == "Get_GCD":
        if len(args) != 2:
            return "Error: Get_GCD operator requires exactly 2 arguments: a, b"
        a, b = args
        return f"Nat.gcd {a} {b}"
    
    elif operator == "Get_LCM":
        if len(args) != 2:
            return "Error: Get_LCM operator requires exactly 2 arguments: a, b"
        a, b = args
        return f"Nat.lcm {a} {b}"
    
    elif operator == "Is_PerfectSquare":
        if len(args) != 1:
            return "Error: Is_PerfectSquare operator requires exactly 1 argument: a"
        a = args[0]
        return f"IsSquare {a}"
    
    elif operator == "Get_Remainder":
        if len(args) != 2:
            return "Error: Get_Remainder operator requires exactly 2 arguments: a, b"
        a, b = args
        return f"{a} % {b}"
    
    elif operator == "Is_Prime":
        if len(args) != 1:
            return "Error: Is_Prime operator requires exactly 1 argument: a"
        a = args[0]
        return f"Prime {a}"
    
    elif operator == "Get_SumOfSquares":
        if len(args) != 1:
            return "Error: Get_SumOfSquares operator requires exactly 1 argument: n"
        n = args[0]
        return f"∑ i ∈ Set.Icc 1 {n}, i ^ 2"
    
    elif operator == "Is_Twin_Prime":
        if len(args) != 1:
            return "Error: Is_Twin_Prime operator requires exactly 1 argument: n"
        n = args[0]
        return f"Prime {n} ∧ (Prime ({n} + 2) ∨ Prime ({n} - 2))"
    
    elif operator == "Is_Factorial_Prime":
        if len(args) != 1:
            return "Error: Is_Factorial_Prime operator requires exactly 1 argument: N"
        N = args[0]
        return f"Prime {N} ∧ (∃ n, {N} = Nat.factorial n + 1 ∨ {N} = Nat.factorial n - 1)"
    
    elif operator == "Is_MersenneNumber":
        if len(args) != 1:
            return "Error: Is_MersenneNumber operator requires exactly 1 argument: N"
        N = args[0]
        return f"∃ n, {N} = 2 ^ n -1"
    
    elif operator == "Is_SinglyEvenNumber":
        if len(args) != 1:
            return "Error: Is_SinglyEvenNumber operator requires exactly 1 argument: N"
        N = args[0]
        return f"2 ∣ {N} ∧ ¬ (4 ∣ {N})"
    
    elif operator == "Order":
        if len(args) != 2:
            return "Error: Order operator requires exactly 2 arguments: a, N"
        a, N = args
        return f"nat.orderOf {a} {N}"

    elif operator == "Get_Lambda_Function":
        if len(args) != 2:
            return "Error: Get_Lambda_Function operator requires exactly 2 arguments: a, N"
        a, N = args
        return f"λ {a} => {N}"
    
    elif operator == "ForAll":
        if len(args) != 2:
            return "Error: Get_Lambda_Function operator requires exactly 2 arguments: a, N"
        a, N = args
        return f"∀ {a}, {N}"

    elif operator == "Exists":
        if len(args) != 2:
            return "Error: Get_Lambda_Function operator requires exactly 2 arguments: a, N"
        a, N = args
        return f"∃ {a}, {N}"
    else:
        return "Error:Unknown operator: {operator}"

# 示例使用
if __name__ == "__main__":
    # 测试新增算子
    print(operator_to_lean("Is_Bijection", "f"))  # Function.Bijective f
    print(operator_to_lean("Set_Union", "A", "B"))  # A ∪ B
    print(operator_to_lean("Get_Digit", "123"))  # Nat.digits 10 123
    print(operator_to_lean("Get_Digit", "16", "255"))  # Nat.digits 16 255
    print(operator_to_lean("Is_Prime", "7"))  # Prime 7
    print(operator_to_lean("Get_GCD", "12", "18"))  # Nat.gcd 12 18
    print(operator_to_lean("Get_Open_Interval", "1", "5"))  # Set.Ioo 1 5
    print(operator_to_lean("Solve_equation", "x : Real", "x + 1 = 0"))  # Set.Ioo 1 5