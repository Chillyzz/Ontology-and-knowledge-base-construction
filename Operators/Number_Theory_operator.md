(Operator 数论部分 26个)

### Numbers

1. Get_LeastCommonDenominator: Get_LeastCommonDenominator(f1: Fraction, f2: Fraction) -> Integer  
   备注: 获取两个或多个分数的最小公分母  
   - 返回两个或多个分数的分母的最小公倍数。  
   - 例：`Get_LeastCommonDenominator(1/4, 1/6) = 12`

2. Get_LeastCommonMultiple: Get_LeastCommonMultiple(a: Integer, b: Integer) -> Integer  
   备注: 获取两个或多个数的最小公倍数  
   - 返回两个或多个数的最小正整数倍。  
   - 例：`Get_LeastCommonMultiple(6, 8) = 24`

3. Get_DigitCount: Get_DigitCount(n: Integer) -> Integer  
   备注: 获取一个数的数字个数  
   - 返回一个数字的总位数。  
   - 例：`Get_DigitCount(12345) = 5`

4. Get_FractionalPart: Get_FractionalPart(x: Real) -> Real  
   备注: 获取一个数的小数部分  
   - 返回数字的小数部分。  
   - 例：`Get_FractionalPart(12.34) = 0.34`

5. Get_IntegerPart: Get_IntegerPart(x: Real) -> Integer  
   备注: 获取一个数的整数部分  
   - 返回数字的小数点左边部分。  
   - 例：`Get_IntegerPart(12.34) = 12`

6. Get_Mantissa: Get_Mantissa(x: Real) -> Real  
   备注: 获取一个数的尾数  
   - 对于实数 `x`，尾数定义为 \( x - \lfloor x \rfloor \)。  
   - 例：`Get_Mantissa(3.14159) = 0.14159`

7. Get_OddPart: Get_OddPart(n: Integer) -> Integer  
   备注: 获取一个数的最大奇因子  
   - 返回一个数的最大奇因子。  
   - 例：`Get_OddPart(24) = 3`（因为 \( 24 = 3 \times 2^3 \)）

8. Get_GreatestCommonDivisor: Get_GreatestCommonDivisor(a: Integer, b: Integer) -> Integer  
   备注: 获取两个或多个数的最大公约数  
   - 返回两个或多个数的最大公约数。  
   - 例：`Get_GreatestCommonDivisor(18, 24) = 6`

9. Get_DigitProduct: Get_DigitProduct(n: Integer) -> Integer  
   备注: 获取一个数的数字积  
   - 返回一个数字中所有数字的乘积。  
   - 例：`Get_DigitProduct(234) = 24`（因为 \( 2 \times 3 \times 4 = 24 \)）

10. Get_DigitSum: Get_DigitSum(n: Integer) -> Integer  
    备注: 获取一个数的数字和  
    - 返回一个数字中所有数字的和。  
    - 例：`Get_DigitSum(234) = 9`（因为 \( 2 + 3 + 4 = 9 \)）

11. Get_DigitalRoot: Get_DigitalRoot(n: Integer) -> Integer  
    备注: 获取一个数的数字根  
    - 通过反复将数字的各位数相加直到只剩下一个数字，得到数字根。  
    - 例：`Get_DigitalRoot(987) = 6`（因为 \( 9 + 8 + 7 = 24 \)，然后 \( 2 + 4 = 6 \)）

12. Get_PandigitalNumber: Get_PandigitalNumber(n: Integer) -> Boolean  
    备注: 判断一个数是否为全数字  
    - 若该数包含所有的 0 到 9 的数字且每个数字出现一次，则返回 `True`。  
    - 例：`Get_PandigitalNumber(9876543210) = True`

13. Get_Pandigital: Get_Pandigital(n: Integer) -> Boolean  
    备注: 判断一个数是否为潘多数字  
    - 若该数包含所有的 0 到 9 的数字至少一次，则返回 `True`。  
    - 例：`Get_Pandigital(1023456789) = True`

14. Get_SumOfSquares: Get_SumOfSquares(n: Integer) -> Integer  
    备注: 获取一个数的平方和  
    - 返回从 1 到 `n` 的平方和。  
    - 例：`Get_SumOfSquares(3) = 14`（因为 \(1^2 + 2^2 + 3^2 = 14\)）

15. Convert_Number_Base: Convert_Number_Base({n: Integer}, {a: Base}, {b: Base}) -> Integer
    备注：将数字从a进制转换到b进制

16. Get_Ones_Digit: Get_Ones_Digit({n: Integer}) -> Integer
    备注: 获取一个数的最后一位数字

### Primes 

1. Get_Nearest_Prime: Get_Nearest_Prime(x: Integer) -> Prime  
   备注: 获取最接近 `x` 的素数  
   - 返回离 `x` 最近的素数。如果 `x` 不是素数，则返回比 `x` 稍大的素数。  
   - 例：`Get_Nearest_Prime(10) = 11`

2. Get_Next_Prime: Get_Next_Prime(x: Integer) -> Prime  
   备注: 获取大于 `x` 的下一个素数  
   - 返回比 `x` 大的最小素数。  
   - 例：`Get_Next_Prime(10) = 11`

3. Get_Previous_Prime: Get_Previous_Prime(x: Integer) -> Prime  
   备注: 获取小于 `x` 的最近素数  
   - 返回比 `x` 小的最大素数。  
   - 例：`Get_Previous_Prime(10) = 7`

4. Get_Least_Prime_Factor: Get_Least_Prime_Factor(x: Integer) -> Prime  
   备注: 获取 `x` 的最小素因子  
   - 返回 `x` 的最小素因子（`x` 的最小的素数因子）。  
   - 例：`Get_Least_Prime_Factor(10) = 2`

5. Get_Greatest_Prime_Factor: Get_Greatest_Prime_Factor(x: Integer) -> Prime  
   备注: 获取 `x` 的最大素因子  
   - 返回 `x` 的最大素因子（`x` 的最大的素数因子）。  
   - 例：`Get_Greatest_Prime_Factor(10) = 5`

6. Get_Prime_Factorization: Get_Prime_Factorization(x: Integer) -> Set(Prime)  
   备注: 获取 `x` 的素因子分解  
   - 返回 `x` 的所有素因子。  
   - 例：`Get_Prime_Factorization(12) = {2, 3}`

7. Is_Prime: Is_Prime(x: Integer) -> Boolean  
   备注: 判断 `x` 是否为素数  
   - 若 `x` 是素数，则返回 `True`，否则返回 `False`。  
   - 例：`Is_Prime(7) = True`

8. Is_Composite: Is_Composite(x: Integer) -> Boolean  
   备注: 判断 `x` 是否为合数  
   - 若 `x` 是合数（大于 1 且不是素数的数），返回 `True`，否则返回 `False`。  
   - 例：`Is_Composite(10) = True`

9. Is_Twin_Prime: Is_Twin_Prime(p: Prime) -> Boolean  
   备注: 判断 `p` 是否为孪生素数  
   - 若 `p` 与 `p±2` 也是素数，则返回 `True`。  
   - 例：`Is_Twin_Prime(11) = True`（因 13 也是素数）

10. Is_Palindromic_Prime: Is_Palindromic_Prime(p: Prime) -> Boolean  
    备注: 判断 `p` 是否为回文素数  
    - 若 `p` 是素数，且它的数位反转后仍然是相同的数，则返回 `True`。  
    - 例：`Is_Palindromic_Prime(131) = True`（因 131 反转后仍是 131）

11. Is_Factorial_Prime: Is_Factorial_Prime(p: Prime) -> Boolean  
    备注: 判断 `p` 是否为阶乘素数  
    - 若 `p` 形如 `n! ± 1`，则返回 `True`。  
    - 例：`Is_Factorial_Prime(5) = True`（因 `4! + 1 = 25`，`5` 是素数）

12. Apply_Sieve_of_Eratosthenes: Apply_Sieve_of_Eratosthenes(n: Integer) -> Set(Prime)  
    备注: 应用埃拉托色尼筛法找出 `n` 以内的所有素数  
    - 通过标记非素数的方法，筛选出 `n` 以内的所有素数。  
    - 例：`Apply_Sieve_of_Eratosthenes(10) = {2, 3, 5, 7}`



## Module

1. Get_Module

2. Is_ModularInverse




