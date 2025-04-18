grammar AssertionalLogic;

// Parser rules
// program
//     : '{' 
//       '"Declarations"' ':' '"' declarationList '"' ','?
//       '"Facts"' ':' '"' assertionList '"' ','?
//       '"Query"' ':' '"' queryList '"'?
//       '}'
//     ;

program
    : declarationList? assertionList? queryList? EOF
    ;


declarationList
    : declaration (';' declaration)*
    ;

declaration
    : variable ':' conceptID
    ;

assertionList
    : (assertion | term) (';' (assertion | term))*
    ;

assertion
    : term '=' term
    ;

queryList
    : assertion (';' assertion)*
    ;

term
    : '(' term ')'                     # ParenTerm
    | operatorID '(' termList ')'         # OperatorTerm
    | term op=('+' | '-') term         # BinaryOpTerm
    | term op=('∈' | '∪' | '∩' | '⊆' | '⊂' | '⊇' |'⊃') term              # SetOpterm
    | term op=('^' | '*' | '/' | '%') term   # BinaryOpTerm
    | term op=('>' | '<' | '=' | '<=' | '>=' | '!=') term # ArithmeticOpTerm
    | term op=('∧' | '∨' | '↔' | '→') term    # LogicalOpterm
    | '{' termList '}'                 # SetTerm 
    | '(' term (',' term)+ ')'         # TupleTerm
    | atomicIndividual                 # AtomicTerm
    ;

termList
    : term (',' term)*                 # CommaTermList  // 逗号分隔的项列表
    ;


atomicIndividual
    : constant
    | variableID
    | declaration
    | '?'
    ;

constant
    : numeral
    | logicalConstant
    | mathematicalConstant
    ;

conceptID
    : 'Real'
    | 'NonNegativeNumbers'
    | 'NegativeNumbers'
    | 'PositiveNumbers'
    | 'TranscendentalNumbers'
    | 'AlgebraicNumbers'
    | 'IrrationalNumbers'
    | 'Integers'
    | 'EvenNumbers'
    | 'OddNumbers'
    | 'PositiveIntegers'
    | 'NegativeIntegers'
    | 'NonNegativeIntegers'
    | 'NaturalNumbers'
    | 'PrimeNumbers'
    | 'CompositeNumbers'
    | 'RationalNumbers'
    | 'Decimals'
    | 'RepeatingDecimals'
    | 'ComplexNumbers'
    | 'ImaginaryNumbers'
    | 'Infinity'
    | 'PositiveInfinity'
    | 'NegativeInfinity'
    | 'Polynomial'
    | 'Monomial'
    | 'IrreduciblePolynomial'
    | 'QuadraticPolynomial'
    | 'CubicPolynomial'
    | 'Function'
    | 'QuadraticFunction'
    | 'CubicFunction'
    | 'Set'
    | 'Sequence'
    | 'ArithmeticSequence'
    | 'GeometricSequence'
    | 'HarmonicSequence'
    | 'Expression'
    | 'Equation'
    | 'Inequation'
    | 'Operator'
    | 'Number'
    ;

operatorID
    : 'Get_Number_Floor'
    | 'Get_Number_Ceil'
    | 'Get_Number_Round'
    | 'Abs'
    | 'Log'
    | 'NaturalLog'
    | 'Sqrt'
    | 'Factorial'
    | 'Get_Combination'
    | 'Get_Reciprocal'
    | 'Get_Sum'
    | 'Get_Prod'
    | 'Exp'
    | 'Solve_equation'
    | 'Solve_inequation'
    | 'Get_Value_Expression'
    | 'Get_PolyDegree'
    | 'Get_Polyroots'
    | 'Get_Term_Coefficient'
    | 'Get_PolyTerm'
    | 'Get_ConstantTerm'
    | 'IsPolyFactor'
    | 'Is_IrreduciblePolynomial'
    | 'Get_PolyCoefficient'
    | 'Eval_Value_Polynomial'
    | 'Is_Polynomial_Root'
    | 'Get_Polynomial_Composition'
    | 'Get_Polynomial_Leading_Coefficient'
    | 'Get_Sequence_Terms'
    | 'Get_Sequences_Sum'
    | 'Is_ArithmeticSequence'
    | 'Is_GeometricSequence'
    | 'Is_MonotonicSequence'
    | 'Get_CommonDifference'
    | 'Get_CommonRatio'
    | 'Is_Monotonic_Increasing_Sequence'
    | 'Is_Monotonic_Decreasing_Sequence'
    | 'Get_FiniteSequences_Length'
    | 'Get_Sequence_Infinite_Sum'
    | 'Get_Function_Range'
    | 'Get_Function_Maximum'
    | 'Get_Function_Minimum'
    | 'Get_Function_Symmetry'
    | 'Get_Function_Zeroes'
    | 'Get_Function_Composition'
    | 'Get_Function_Minimalperiod'
    | 'Get_Inverse_Function'
    | 'Get_Function_IthComposition'
    | 'Get_Function_Value'
    | 'Is_Bijection'
    | 'Is_Injection'
    | 'Is_Surjection'
    | 'Get_QuadraticFunction_Discriminant'
    | 'Get_Function_Expression'
    | 'Get_StepFunction_Expression'
    | 'Is_Function_Root'
    | 'Get_Function_InDomain_Range'
    | 'Set_Union'
    | 'Set_Intersection'
    | 'Set_Difference'
    | 'Set_SymmetricDifference'
    | 'Set_Subset'
    | 'Set_ProperSubset'
    | 'Set_Superset'
    | 'Set_ProperSuperset'
    | 'Set_Cardinality'
    | 'Set_PowerSet'
    | 'Set_Complement'
    | 'Set_Equality'
    | 'Get_Set_Sum'
    | 'Get_Set_Product'
    | 'Build_Set'
    | 'Get_Set_Maximum'
    | 'Get_Set_Minimum'
    | 'Elements_In_Set'
    | 'Get_Set_Means'
    | 'Is_Set_BoundedFromAbove'
    | 'Is_Set_Unbounded'
    | 'Get_UniversalSet'
    | 'Range'
    | 'Get_Open_Interval'
    | 'Get_LeftClosedRightOpen_Interval'
    | 'Get_LeftOpenRightClosed_Interval'
    | 'Get_Closed_Interval'
    | 'Get_RightOpen_Interval'
    | 'Get_RightClosed_Interval'
    | 'Get_LeftOpen_Interval'
    | 'Get_LeftClosed_Interval'
    | 'Negation'
    | 'Build_Universal_Proposition'
    | 'Build_Exist_Proposition'
    | 'And'
    | 'Or'
    | 'Implication'
    | 'Equivalence'
    | 'Build_UniqueExist_Proposition'
    | 'Get_Angle_DegreeMeasure'
    | 'Get_Angle_RadianMeasure'
    | 'Change_Degree_To_Radian'
    | 'Change_Radian_To_Degree'
    | 'Sin'
    | 'Cos'
    | 'Tan'
    | 'Cot'
    | 'Is_Odd_Number'
    | 'Is_Even_Number'
    | 'Is_Prime_Number'
    | 'Is_Composite'
    | 'Get_FractionalPart'
    | 'Get_IntegerPart'
    | 'Get_LeastCommonDenominator'
    | 'Get_Mediant'
    | 'UnitFraction'
    | 'Is_ProperFraction'
    | 'Is_IrreducibleFraction'
    | 'Is_Coprime'
    | 'Is_Factor'
    | 'Get_GCD'
    | 'Get_LCM'
    | 'Is_PerfectSquare'
    | 'Get_Remainder'
    | 'Is_Prime'
    | 'Get_SumOfSquares'
    | 'Is_Twin_Prime'
    | 'Is_Factorial_Prime'
    | 'Is_MersenneNumber'
    | 'Is_SinglyEvenNumber'
    | 'Order'
    | 'Get_Mod_Nat'
    | 'Is_Nat_Mod'
    | 'Negation'
    | 'ForAll'
    | 'Exists'
    | 'Get_Lambda_Function'
    ;


// Lexer rules
variable
    : CHARACTERS 
    | (LOWERCASE_LETTER | UPPERCASE_LETTER) 
    | '-' CHARACTERS
    | '-' (LOWERCASE_LETTER | UPPERCASE_LETTER)
    ;

variableID
    : CHARACTERS
    | (LOWERCASE_LETTER | UPPERCASE_LETTER) 
    | '-' CHARACTERS
    | '-' (LOWERCASE_LETTER | UPPERCASE_LETTER)
    ;

numeral
    : DIGITS                  # PositiveInteger
    | DIGIT                   # PositiveSingleDigit
    | DIGITS '.' DIGITS       # PositiveFloat
    | '-' DIGITS              # NegativeInteger
    | '-' DIGIT               # NegativeSingleDigit
    | '-' DIGITS '.' DIGITS   # NegativeFloat
    ;

DIGIT : [0-9];
DIGITS : DIGIT+;
CHARACTERS : CHARACTER+;
CHARACTER : [A-Za-z0-9];

logicalConstant
    : 'True'
    | 'False'
    ;

mathematicalConstant
    : 'Real.pi'
    | 'Real.e'
    | 'Complex.i'
    ;

// Basic tokens
UPPERCASE_LETTER: [A-Z];
LOWERCASE_LETTER: [a-z];


// Operators and punctuation
QUESTION: '?';
COLON: ':';
COMMA: ',';
SEMICOLON: ';';
LPAREN: '(';
RPAREN: ')';
UNDERSCORE: '_';

// Whitespace and comments
WS: [ \t\r\n]+ -> skip;
COMMENT: '--' ~[\r\n]* -> skip;
