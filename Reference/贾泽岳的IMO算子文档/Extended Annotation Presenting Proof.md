# Extended Annotation Presenting Proof

## Language Structure
This language is extension to for the annotation language, to view its behaviour, <a href="https://pad.degrowth.net/s/HJo7ZdTjt"> click here for the annotation handbook</a> .

The purpose for this language is basicly to extand the annotation language, enabling it to present the proof in additional to the question.
## First Example

    Fact List 
    a : sequence 
    Content( a ) = Number
    Item( a , 1 ) = 1 
    ForAll( { n : PositiveInteger } , Item( a , n+1 ) = Item( a , n )/(Item( a , n )+1 ) )
    
    Query List
    Proof( ForAll( { n : PositiveInteger } , Item( a , n ) = 1/n ) )
    
    Proof:
    
    Global Scope
    0| a : sequence 
    1| Content( a ) = Number
    2| Item( a , 1 ) = 1 
    3| ForAll( { n : PositiveInteger }, Item( a , n+1 ) = Item( a , n )/(Item( a , n )+1 ) )
    
    /*
        \1
        4| n: PositiveInteger ||3 Rule: ForAll Generates Scope
        5| Item( a , n+1 ) = Item( a , n )/(Item( a , n )+1 ) ||3 Rule: ForAll Generates Scope
    */
    
        \2
        Q2| Item( a , n ) = 1/n || Method: 归纳法奠基
        6| n: PositiveInteger || Method: 归纳法奠基
        7| n = 1 || Method: 归纳法奠基
        8| Item( a , n ) = 1/n ||2,7 Rule: 计算
    
        \3
        Q3| Item( a , k+1 ) = 1/(k+1) || Method: 归纳假设
        9| k: PositiveInteger || Method: 归纳假设
        10| Item( a , k ) = 1/k || Method: 归纳假设
        11| Item( a , k+1 ) = Item( a , k )/(Item( a , k )+1 ) ||3 Rule: Apply k
        12| Item( a , k+1 ) = 1/(k+1) ||10,11 Rule: 计算 
    
    13| ForAll( { n : PositiveInteger } , Item( a , n ) = 1/n ) ||8,12 Method: 归纳法


In this Example, the Fact list and Query list part is the same as the annotation language, where the Proof part is noval.

In the following sections we will describe the overall guideline of this language and how the proof part will work.

## GuideLine

In a process to prove a statement, we only care about four kinds of things, which are called individuals, assertions, rules and methods.

### Individuals

Individuals are the basic elements used in a question proof. The proof of a statement is basicly doing study on some properties certain individuals possess.

### Assertions

Assertions describe the properties individuals possess and the relationship between individuals. The procedure of ratiocination is mainly mainly a sequence of exploration from supposing some assertions as a fact list, with a purpose of adding target assertion to the fact list, within each step we add one assertion to the fact list based on some certain rule.

### Rules

Rules are used to describe the relationship between assertions. Rules are mostly telling that when some certain assertions are all in the fact list, then you may add another assertion to the fact list.

### Methods 

Some complicated problems may not be solved with rules only, this is the situation which methods are aimed for. Some methods give a set of assertions equivalent to the target assertion, some devides the problem into smaller and easier parts and others work otherwise, all of which simplifies the problem. Sometimes methods divide the overall situation into cases, within each case it foucus on a certain type of elements, this is when scopes come into use.

### Scopes 

Scopes describes a general condition where all individuals in the scope behaves exactly like what it does in the scope. We use scope to generate ForAll assertions in the annotation language.
Scopes are often generated when a query is devided into several subqueries. When scopes are generated, a list of facts is added to the local facr list of the scope, as well as the subwuery. These cases will cause a syntex exception.

## Syntex

This section is a overall requirement for the proof part syntex.

To make it easier to write a proof with this language, we use 
`/*` and `*/` to denote a part of text which should be negelected. `/*` and `*/` should be each at the head of a row.

Each line in the text denotes a step to solve the problem, its structure should be like:

    [ST][SO or QO]|[Annotation]||[SS][Base Rule][Root Query][Base Method]

### ST: Scope Tabs 

The number of scope tabs is given by the rule below.

1.The global scope has no tabs in front of its contents. 
2.The direct child scope of a scope has one more tab than it.

### SO: Step Order

Step orders are numbers marking the order individuals and assertions are added to the proof. 

In general, step orders do not have to rise during the proof, because you may need an assertion created by later scopes in the former scope. **But in practical usage we should list them in order if able.**

### QO: Query Order

Query orders are numbers marking the order queries are generated in the progress of the proof.

In general, query orders do not have to rise during the proof, **but in practical usage we shoule list them in order if able.**

<a href="#SQ">Syntex Exceptions: *scope queries*</a>

### Annotation 

The extended annotation.
See <a href="#HANDBOOK"> Extention Handbook </a>.
Annotations should be surrounded with `|` in the front and `||` the back.

### SS: Supporting Steps

We use a series of numbers to denote the steps supporting the current step. We should denote that the the indexes of supporting steps should be each less than the current step.

### Base Rule 

The rule based to deduce this assertion.

### Root Query

Each query generated in the proof should be either in the query list, or a method generated it in order to solve another query. If the latter is true, then that query is called the root query of this one. We write its Query Order here.

### Base Method

The method obeyed to generate this individual or assertion.

:::warning
Up to now, we have not found any situations where we need some certain step along with a method to generate an individual or assertion, but we expect there to be this sort of situation. Therefore, we are not listing Base Method as a syntex exception.
:::

:::warning
We have not yet ruled out the possibility that some assertions or individuals need more than one method to generate, but we estimate the possibility to be rather small. The same is true for rules. Therefore, we are not yet using "Base Rules" or "Base Methods", to show that we assert there to be only one rule or method to be used.
:::

### Syntex Exceptions

<a id="SQ"></a>

#### Scope Quries

This part mainly deals with the syntex variation in a scope.

- A scope is leaded by a line
     `\[Scope Order]`
- Inside each scope there is a line leaded by `[Query Order]|` instead of a step order which present the query of this scope.
    + If an assertion presenting the query of a scope would be added to the fact list, we can add a ForAll assertion to its father scope in the main time.
    :::warning 
    We now, not taking calculating efficiency into account, assert each scope to have only one query.
    :::
    :::info
    This is an outdated form presenting the proof. Now we instead directly add the assertion into the scope, then deduct the forall operator in the father scope based on a method.
    :::
- The fact list we add to a scope when generating it has no supporting steps after it, only the method that genera this scope.

:::info
We now put the Query of a scope in the front of it. But remember, **the query of a socpe and the fact list of it are added into it in the mean time, without regard to the orders they are writen.** This is because in logic we prefer to let the query lead the scope, but it may have to use some individuals declared afterwards.
:::

<a id="HANDBOOK"></a>

Extension HandBook
===

## Concept

|   Name      | Description |
| ----------- | ----------- |
|Number|数
|Real|实数
|PositiveNumber|正数
|OddNumber|奇数
|EvenNumber|偶数
|Integer|整数
|PositiveInteger|正整数
|Sequence|数列
|Content|内容
|Item|项
|ArithmeticProgression|等差数列
|ArithmeticMean|等差中项
|CommonDifference|公差
|GeometricProgression|等比数列
|GeometricMean|等比中项
|CommonRatio|公比
|Constant|常数
|FibonacciSequence|斐波那契数列
|LucasSequence|卢卡斯数列

| Build-in Sequences | Description |
| --------------------- | ----------- |
| NaturalNumberSequence | 自然数数列 |
| PositiveOddSequence | 正奇数数列 |
| PositiveEvenSequence | 正偶数数列 |
| PositiveIntegerSequence | 正整数数列 |

:::info
We denote that ArithmeticProgression, GeometricProgression, FibonacciSequence and LucasSequence are subconcepts of Sequence, all of which have number as their content, and each has other properties.
:::


## Reference

### 1.1 Sequence

In mathematics, a sequence uaually means an ordered list of events.


:::info
Example:

数列{$a_n$}……
```
a:Sequence
```
:::

### 1.2 Content
Sometimes,we need to be clear about the range to which elements of the sequence belongs. So we use 'Content(a)' to dicribe the value of sequence. 

Be careful that Content' can't be used to definite the value of one specific element.


:::info
Example：
实数数列{$a_n$}……

```
Content(a)=Real
```
整数数列$\{a_n\}$……

```
Content(a)=Integer
```
正数数列{$a_n$}……
```
Content(a)=PositiveNumber
```

:::

### 1.3 ArithmeticProgression，CommonDifference
Arithmetic progression  is a sequence that from the second item, the difference between each item and its previous item is equal to a constant.

After that, we call the same constant 'CommonDifference'.We often use 'd' to express common difference.

:::info
Example:

{$a_n$}是等差数列，且公差d为1……
```
a:Sequence
a:ArithmeticProgression
d=CommonDifference(a)
d=1
```
:::

### 1.4 ArithmeticMean

We call the intermediate item of three items which make up an arithmetic progression arithmetic mean.


:::info
Example:

a,b,c依次构成等差数列……
```
b=ArithmeticMean(a,c)   
```
:::

It should be noted that the above word '依次' tell us the diffrence between b and a equals to the diffrence between c and b.

### 1.5 Item

Each element of a sequence is called a item of that sequence.We can use 'Item' like this.

:::info
Example:

在数列{$a_n$}中，$a_1=1$……
```
a:Sequence
Item(a,1)=1  
```
:::

### 1.6 GeometricProgression，CommonRatio

Geometric progression is a sequence that from the second item, the ratio of each item to its previous item is equal to a constant.

After that, we call the same constant 'CommonRatio'. We often use 'q' to express common ratio.

:::info
Example:

{$a_n$}是等比数列，且公比q为2……
```
a:GeometricProgression
q=CommonRatio(a)
q=2
```
:::

### 1.7 GeometricMean

We call the intermediate item of three items which make up an arithmetic progression arithmetic mean.


:::info
Example:

a,b,c依次构成等比数列……
```
b=GeometricMean(a,c)   
```
:::

### 1.8 Constant

In mathematic , the value of a constant is unchanged.


### 1.9 FibonacciSequence

Fibonacci sequence is a sequence that begins with item 3, each equals to the sum of the previous two items . In this sequence , the first two items are both equal to 1.


:::info
Example:

在斐波那契数列{$a_n$}中……
```
a:FibonacciSequence
```
:::


### 1.10 LucasSequence

Lucas sequence is a sequence that begins with item 3, each equals to the sum of the previous two items . In this sequence , the first item equals to 1,the twice item equals to 3.

:::info
Example:

在卢卡斯数列{$a_n$}中……
```
a:LucasSequence
```
:::


### 2.1  Item

We always need to express one element of a sequence. If we use {a_n} to express $a_n$ , it would be confused. So we defined a new operator , 'Item' ,and it is used as 'Item ({Sequence,Integer})'


:::info
Example:

在数列{$a_n$}中，$a_1=1$,……

```
a:Sequence
Item(a,1)=1

```
:::


### 2.2 PartialSum

In many problems, we can see '数列{$a_n$}前n项的和为$S_n$'. We need a operator to describe it, then we define 'PartialSum'. 'PartialSum' can be used as 'PartialSum({Sequence,Integer,Integer})'

:::info
Example:
{$S_n$}是数列{$a_n$}的前n项和……

```
a:Sequence
S:Sequence
Item(S,n)=PartialSum(a,1,n)

```


Please be careful that we also definited 'S' as a sequence.
:::


### 2.3 PartialProduct

In many problems, we can see '数列{$a_n$}前n项的积为$S_n$'. We need a operator to describe it, then we define 'Product'. 'Product' can be used as 'Product ({Sequence,Integer,Integer})'

:::info
Example:
$S_n$是数列$a_n$的前n项和……

```
a:Sequence
S:Sequence
Item(S,n)=PartialProduct(a,1,n)

```


Please be careful that we also definited 'S' as a sequence.
:::



### 2.4 IsCommonDifference

Sometimes we need to know that how much is the common difference of a arithmetic progression. Then we use 'IsCommonDifference' to describe.



:::info
Example:

在等差数列 {$a_n$} 中，公差为1……


```
a: ArithmeticProgression
IsCommonDifference (a,1)=True

```
:::


### 2.5 Forall

When we want to describe the general formula of a sequence, we use 'Forall({Set,Formula})'.

For example, 'Forall ( { n : PositiveInteger } , Item( a , n ) = n ) ' means ' 数列{$a_n$}的通项公式为$a_n=n$ '

### 2.6 Sigma and Pi

The sigma operator($\Sigma$) has two forms. For one thing, sigma can be used to calculate the sum of a function of a  sequence; and for another, it can operate on a set and calculate a function of the set.

Therefore, we introduce two operator-sigma as the following forms:

- Sigma( Iterator Sequence , Expression , First_place , Last_place )
    :::info
    For example, to present $\Sigma_{i=1}^n\frac{a_i}{i}$, we use
    ```
        Sigma( { i: NaturalNumberSequence } , Item(a,i)/i , 1 , n )
    ```
    And this can be calculated by python with 
    ```
    sum = 0 
    For i in NaturalNumberSequence[1:n]:
        sum = sum + Item(a,i)/i 
        pass
    ```
    :::
- Sigma( Iterator Set , Expression )
    :::info
    For example, to present $\Sigma_{ x \in S }x^2$, we use
    ```
        Sigma( { x : S } , x^2 )
    ```
    This can be calculated by python with
    ```
    sum = 0 
    For x in S:
        sum = sum + x**2
        pass
    ```
    :::

We handle the pi operator( $\Pi$ ) as the same.

### 3.1 Build-in Sequences

Sometimes, there are a known sequence of numbers, so we make a build-in sequences.

NaturalNumberSequence equals to {n: Interger|In(n,PositiveNumber) or n=0}
PositiveOddSequence equals to {2n-1|n:PositiveNumber}
PositiveEvenSequence equals to {2n|n:PositiveNumber}
PositiveIntegerSequence equals to {n:PositiveNumber}










