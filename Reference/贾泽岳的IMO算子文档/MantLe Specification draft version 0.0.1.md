# MantLe Specification draft version 0.0.1

proposals requiring further discussion will be marked with `(?)`

## Value denotion

### MantLe defined special entities

+ Symbols

   A symbol is a string consisting of [a-z], [A-Z], [0-9] and starting with a character other than [0-9].

### Individuals

+ a symbol can denote an individual

   + The declaration of a symbol as an individual see chapter[]
   + The list of pre-declared symbols see appendix[]

+ a value literal can denote an individual with a specified value

   + | Type of value | literal form |
      | ---- | ---- |
      | boolean | `(?)` <br/>TRUE/FALSE <br/> True/False <br/> true/false |
      | number( integers divided by $10^n$ ) | Decimal form |
      | string | "abc" ( ' and \` left for future usage ) |
      | tuple | `(?)` $\begin{align*} \text{current:} & & \begin{array} & jzy:& (a,b,c) \\ chw:& \$(a,b,c)\$ \end{array} \\ \text{extra proposal:} & & [a,b,c] \hspace{0.7em}\end{align*}$<br/>problem: tuple with length 1 introduces confuse: (a\*b) (a\*b) |
      | set | `(?)` <br/> $\begin{array}[lr] & enumerable: & \begin{array}[m] & jzy:& \{a,b,c\} \\ chw:& \$\{a,b,c\}\$ \end{array} \\ descripted: &concept\ literal \end{array}$ |
      
      A concept literal is a comma-delimited list of variable declarations and assertions, enclosed in curly braces(`{}`). The variables declared within are the representatives of the set, 
      
      e.g.$\{x\in\mathbb{R}|x^2+1<5\}$ is denoted with `{ x: Real, x^2+1<5 }`

### Operator

+ operators

   + An operator should be denoted with either:

      + a symbol
      + a term with concept instance of `Operator`
      + each one in the list below:
         + `+`
            + binary: operator `Add`
            + unitary: operator `Positive`
         + `-`
            + binary: operator `Minus`
            + unitary: operator `Negative`
         + `*`
            + binary: operator `multiply`
         + `/`
            + binary: operator `devides`
         + `^`
            + binary: operator `power`
         + `` `
            + not defined yet
            + `(?)` proposal: to denote differential
               +  f(x)`x denotes $\frac{\partial f(x)}{\partial x}$
         + `'`
            + not defined yet
         + `_` 
            + not defined yet
            + `(?)` proposal: to denote operator `Item`
               + `a_n` denotes `Item( a, n )`
         + `@`
            + the representative operator: to change the representatives of a concept
               + `x@PositiveInteger` gives the concept `PositiveInteger` a representative `x`
               + `((a,b,p))@{ a: PositiveInteger, b: PositiveInteger, p: PositiveInteger, a^2+b^2=p}` defines the solution set of the equation $a^2+b^2=p,\ a,b,p\in\mathbb{N}$
               + `(b=2*a)@{ a: PositiveInteger }` renames or restructures the representative
   
   + An operator should be defined with each of the Internal methods listed below
   
     + `[[Bind]]`
     
        + The procedure of binding an operator with arguments to form a term is called binding.
     
           e.g. let `f` denote an operator, `f(x)` and `f(x,y,z)` are both bindings with different argument list.
     
        + The information indicating the concept of each term formed by a binding is recorded by the operator.
     
           e.g. `Sigma( { x: PositiveInteger, x < 5 }, x )` and `Sigma( { i: PositiveInteger }, i, 1, 5 )`
     
           are two different type of bindings with the same operator `Sigma`
     
     + `[[Evaluate]]`
     
        + The procedure of turning an operator into Mathematica’s form is called Evaluate.
     
             e.g. When `Sigma( { i: PositiveInteger }, i, 1, 5 )` is applied `[[Evaluate]]`, it is turned to
     
             ```mathematica
             Sum[i,{i,1,5}]
             ```

### Concept

+ a concept is denoted with either:
   + a symbol
   + a term with concept `Concept`
   
+ namespace

   + used in knowledge database to store the information

   + declaration: the grammar used to denote concept literal is used with a little difference to denote namespace

      ```MantLe
      NumberTheory@0.0.1: Namespace { // use Namespace prefix to indicate a namespace declaration
      	Prime: Concept, // declare Prime as a concept
      	ForAll( { x: Prime }, In( x, PositiveInteger ) ), // consider inheritance
      	ForAll( { x: Prime }, 
      		ForAll( { n: PositiveInteger, n <= x, not( n = 1 ) }, not( Divisible( n, x ) ) )
      	) //specialty of Prime
      } with Core@0.0.1 // declare the namespaces involved
      ```

   + import: use `with` keyword

      ```MantLe
      // with Core version latest
      // import the latest Core by default
      with NumberTheory version 0.0.1 // with NumberTheory version latest
      // `with Prime from NumberTheory version latest` only introduces `Prime`
      Fact List
      p: Prime
      ...
      ```

## Induction

#### Interactive induction syntax

```MantLe
8| ForAll( { n: PositiveInteger }, Item( a, n )=1 )
9| k: PositiveInteger
10||>8,9 Rule: Apply(k)
```


