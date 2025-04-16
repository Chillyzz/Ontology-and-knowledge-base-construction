def declaration_to_lean(declaration):
    """
    将Declaration转换为Lean代码格式
    
    参数:
    declaration (tuple): 包含variable和ConceptID的元组 (variable, concept_id)
    
    返回:
    str: 转换后的Lean代码声明
    """
    if len(declaration) != 2:
        raise ValueError("Declaration must be a tuple of (variable, concept_id)")
    
    variable, concept_id = declaration
    
    # 根据不同的ConceptID进行匹配
    if concept_id == "Real":
        return f"({variable} : ℝ)"
    elif concept_id == "NonNegativeNumbers":
        return f"({variable} : NNReal)"  # 或用 {x : ℝ // x ≥ 0}
    elif concept_id == "NegativeNumbers":
        return f"({variable} : ℝ) (h_{variable} : {variable} < 0)"
    elif concept_id == "PositiveNumbers":
        return f"({variable} : ℝ) (h_{variable} : {variable} > 0)"
    elif concept_id == "AlgebraicNumbers":
        return f"({variable} : ℝ) (h_{variable} : IsAlgebraic ℝ {variable})"
    elif concept_id == "IrrationalNumbers":
        return f"({variable} : ℝ) (h_{variable} : Irrational {variable})"
    elif concept_id == "TranscendentalNumbers":
        return f"({variable} : ℝ) (h_{variable} : Transcendental ℝ {variable})"
    elif concept_id == "Integers":
        return f"({variable} : ℤ)"
    elif concept_id == "OddNumbers":
        return f"({variable} : ℤ) (h_{variable} : Odd {variable})"
    elif concept_id == "EvenNumbers":
        return f"({variable} : ℤ) (h_{variable} : Even {variable})"
    elif concept_id == "NonNegativeIntegers":
        return f"({variable} : ℤ) (h_{variable} : {variable} ≥ 0)"
    elif concept_id == "NegativeIntegers":
        return f"({variable} : ℤ) (h_{variable} : {variable} < 0)"
    elif concept_id == "PositiveIntegers":
        return f"({variable} : ℕ)"
    elif concept_id == "PrimeNumbers":
        return f"({variable} : ℕ) (h_{variable} : Nat.Prime {variable})"
    elif concept_id == "CompositeNumbers":
        return f"({variable} : ℕ) (h_{variable} : {variable} > 1 ∧ ¬ Nat.Prime {variable})"
    elif concept_id == "RationalNumbers":
        return f"({variable} : ℚ)"
    elif concept_id == "ComplexNumbers":
        return f"({variable} : ℂ)"
    elif concept_id == "ImaginaryNumbers":
        return f"(h_{variable} : IsPureImaginary {variable})"
    elif concept_id == "Function":
        return f"({variable} : ℝ → ℝ)"
    elif concept_id == "QuadraticFunction":
        return (
            f"({variable}: ℝ → ℝ)"
            f"({variable}_a {variable}_b {variable}_c : ℝ) "
            f"({variable}_a_nonzero : {variable}_a ≠ 0) "
            f"({variable}_discriminant : ℝ) "
            f"({variable}_discriminant_rule: {variable}_discriminant = {variable}_b^2 - 4 * {variable}_a * {variable}_c) "
            f"({variable}_func : {variable} = λ x => {variable}_a * x^2 + {variable}_b * x + {variable}_c)"
        )
    elif concept_id == "CubicFunction":
        return (
            f"({variable}: ℝ → ℝ) "
            f"({variable}_a {variable}_b {variable}_c {variable}_d : ℝ) "
            f"({variable}_a_nonzero : {variable}_a ≠ 0) "
            f"({variable}_discriminant : ℝ) "
            f"({variable}_discriminant_rule: {variable}_discriminant = {variable}_b^2 - 3 * {variable}_a * {variable}_c) "
            f"({variable}_func : {variable} = λ x => {variable}_a * x^3 + {variable}_b * x^2 + {variable}_c * x + {variable}_d)"
        )
    elif concept_id == "ConstantFunction":
        return f"({variable} : ℝ → ℝ) (h_{variable} : ∃ c, ∀ x, {variable} x = c)"
    elif concept_id == "IdentityFunction":
        return f"({variable} : ℝ → ℝ) (h_{variable} : ∀ x, {variable} x = x)"
    elif concept_id == "PeriodicFunction":
        return f"({variable} : ℝ → ℝ) (h_{variable} : Periodic {variable} 1)"
    elif concept_id == "IncreasingFunction":
        return f"({variable} : ℝ → ℝ) (h_{variable} : Monotone {variable})"
    elif concept_id == "DecreasingFunction":
        return f"({variable} : ℝ → ℝ) (h_{variable} : Antitone {variable})"
    elif concept_id == "OddFunction":
        return f"({variable} : ℝ → ℝ) (h_{variable} : Function.Odd {variable})"
    elif concept_id == "EvenFunction":
        return f"({variable} : ℝ → ℝ) (h_{variable} : Function.Even {variable})"
    elif concept_id == "Sequence":
        return f"({variable} : ℕ → ℝ)"
    elif concept_id == "ArithmeticSequence":
        return (
            f"({variable}: ℕ → ℝ) "
            f"({variable}_d : ℝ) "
            f"({variable}_property : ∀ n : ℕ, {variable} (n + 1) - {variable} n = {variable}_d)"
        )
    elif concept_id == "GeometricSequence":
        return (
            f"({variable}: ℕ → ℝ) "
            f"({variable}_q : ℝ) "
            f"({variable}_property : ∀ n : ℕ, {variable} (n + 1) / {variable} n = {variable}_q)"
        )
    elif concept_id == "HarmonicSequence":
        return f"({variable} : ℕ → ℚ) (h_{variable} : ∀ n, {variable} n = 1 / n)"
    elif concept_id == "ConvergentSequence":
        return f"({variable} : ℕ → ℝ) (h_{variable} : ∃ L, Tendsto {variable} atTop (𝓝 L))"
    elif concept_id == "DivergentSequence":
        return f"({variable} : ℕ → ℝ) (h_{variable} : ¬ ∃ L, Tendsto {variable} atTop (𝓝 L))"
    elif concept_id == "Polynomial":
        return f"({variable} : Polynomial ℝ)"
    elif concept_id == "Monomial":
        return f"({variable} : Polynomial ℝ) (h_{variable} : {variable}.support.card ≤ 1)"
    elif concept_id == "IrreduciblePolynomial":
        return f"({variable} : Polynomial ℝ) (h_{variable} : Irreducible {variable})"
    elif concept_id == "QuadraticPolynomial":
        return (
            f"({variable} : Polynomial ℝ) "
            f"({variable}_degree : {variable}.natDegree = 2) "
            f"({variable}_leading_nonzero : {variable}.leadingCoeff ≠ 0) "
            f"({variable}_discriminant : ℝ) "
            f"({variable}_discriminant_def : {variable}_discriminant = {variable}.coeff 1 ^ 2 - 4 * {variable}.coeff 2 * {variable}.coeff 0)"
        )
    elif concept_id == "CubicPolynomial":
        return (
            f"({variable} : Polynomial ℝ) "
            f"({variable}_degree : {variable}.natDegree = 3) "
            f"({variable}_leading_nonzero : {variable}.leadingCoeff ≠ 0) "
            f"({variable}_discriminant : ℝ) "
            f"({variable}_discriminant_def : {variable}_discriminant = {variable}.coeff 2 ^ 2 - 3 * {variable}.coeff 3 * {variable}.coeff 1)"
    )
    else:
        # 默认处理，直接使用ConceptID作为类型
        return f"({variable} : {concept_id})"
    

print(declaration_to_lean(("x", "Real"))) 
# 输出: (x : ℝ)

print(declaration_to_lean(("f", "OddFunction")))
# 输出: (f : ℝ → ℝ) (h_f : Function.Odd f)

print(declaration_to_lean(("seq", "ArithmeticSequence")))
# 输出: (seq : ArithmeticSequence)


print(declaration_to_lean(("AA", "QuadraticFunction")))
print(declaration_to_lean(("AB", "QuadraticPolynomial")))