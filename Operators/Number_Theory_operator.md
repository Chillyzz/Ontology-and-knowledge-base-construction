(Operator 数论部分 35个)

### Numbers_Property

1. Is_Odd_Number: Is_Odd_Number(a: Integer) -> Boolean
   备注: 判断 a 是不是奇数

2. Is_Even_Number: Is_Even_Number(a: Integer) -> Boolean
   备注: 判断 a 是不是偶数

3. Is_Prime_Number: Is_Prime_Number(a: Integer) -> Boolean
   备注: 判断 a 是不是素数

4. Is_Composite: Is_Composite(x: Integer) -> Boolean  
   备注: 判断 `x` 是否为合数  
   - 若 `x` 是合数（大于 1 且不是素数的数），返回 `True`，否则返回 `False`。  
   - 例：`Is_Composite(10) = True`


### Fractions

-- 1. Get_FractionalPart: Get_FractionalPart(x: Real) -> Real

-- 2. Get_IntegerPart: Get_IntegerPart(x: Real) -> Integer

-- 3. Get_LeastCommonDenominator: Get_LeastCommonDenominator(f1: RationalNumbers, f2: RationalNumbers) -> Integer

-- 4. Get_Mediant: Get_Mediant(q1: RationalNumbers, q2: RationalNumbers) -> RationalNumbers

-- 5. UnitFraction: UnitFraction(q: RationalNumbers) -> Prop

-- 6. Is_ProperFraction: Is_ProperFraction(q: RationalNumbers) -> Prop

-- 7. Is_IrreducibleFraction: Is_IrreducibleFraction(q: RationalNumbers) -> Prop



### Primes

-- 1. Is_Coprime: Is_Coprime({m: NaturalNumber}, {n: NaturalNumber}) -> Prop

-- 2. Is_Factor: Is_Factor({a: NaturalNumber}, {b: NaturalNumber}) -> Prop

-- 3. Get_GCD: Get_GCD({a: NaturalNumber}, {b: NaturalNumber}) -> NaturalNumber

-- 4. Get_LCM: Get_LCM({a: NaturalNumber}, {b: NaturalNumber}) -> NaturalNumber

-- 5. Is_PerfectSquare: Is_PerfectSquare(a: NaturalNumber) -> Prop

-- 6. Get_Remainder: Get_Remainder({a: NaturalNumber}, {b: NaturalNumber}) -> NaturalNumber

-- 7. Is_Prime: Is_Prime(a: NaturalNumber) -> Prop

-- 8. Get_SumOfSquares: Get_SumOfSquares(n: Integer) -> Integer

-- 9. Is_Twin_Prime: Is_Twin_Prime(p: Prime) -> Boolean

-- 10. Is_Factorial_Prime: Is_Factorial_Prime(p: Prime) -> Boolean

-- 11. Is_MersenneNumber: Is_MersenneNumber(N: NaturalNumber) -> Boolean

-- 12. Is_SinglyEvenNumber: Is_SinglyEvenNumber(N: NaturalNumber) -> Boolean

-- 13. Order: Order(a: NaturalNumber, N: NaturalNumber) -> Number


### Mod

   1. Get_Mod_Nat: Get_Mod_Nat(n: NaturalNumber, m: NaturalNumber) -> NaturalNumber

   2. Get_Z_Mod: Get_Z_Mod(n: Integer) -> Ring (超纲了)

   3. Is_Nat_Mod: Is_Nat_Mod(a: NaturalNumber, b: NaturalNumber, n: NaturalNumber) -> Boolean


### Digits

-- 1. Get_Digit: [(Optional)Base: NaturalNumber](n: NaturalNumber) -> List

-- 2. Covert_Digit_To_Number: [(Optional)Base: NaturalNumber](L: List) -> NaturalNumber

-- 3. Get_DigitCount: [(Optional)Base: NaturalNumber](n: Integer) -> Integer

-- 4. Get_DigitProduct: [(Optional)Base: NaturalNumber](n: Integer) -> Integer

-- 5. Get_DigitSum: [(Optional)Base: NaturalNumber](n: Integer) -> Integer

-- 6. Is_PandigitalNumber: Is_PandigitalNumber(L: List) -> Boolean

-- 7. Is_PalindromeNumber: Is_PalindromeNumber(L: List) -> Boolean

-- 8. Get_Ones_Digit: [(Optional)Base: NaturalNumber]Get_Ones_Digit({n: Integer}) -> Integer
