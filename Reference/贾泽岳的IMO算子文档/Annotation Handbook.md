# Annotation Handbook

This is a handbook for annotation. Contents are mostly collected from weekly meetings since the project starts.

## Overview

### Pipeline

```
   NL  +---------+  L  +--------------+  AL
  ---->| Pre-NLU | --> | Post-Process | ---->
       +---------+     +--------------+
```

The annotation task is to convert NL to L manually.

### Principle

The annotation should achieve:
1. **No ambiguity.** With the information inside the annotations, we can work out the solution by hand.
2. **Apply basic AL syntax.** Conversion to AL should be possible and easy.
3. **Close to NL.** It should <u>represent</u> the question without <u>rephrasing</u> it.

## Annotation Structure

An annotation is composed of 4 parts:
1. NL. The natural language representation of the question;
2. Fact List. A list of assertions representing the question.
3. Query List. A list of terms representing the queries.
4. Answer. A list of terms representing the answer.

For some questions, the annotation may not exist. See the last part 'Cannot Annotate' for details.

## Syntax

The syntax of our annotation language:

### Basic Syntax

```
Sentence    -> Assertion
Assertion   -> Term = Term
Term        -> Operator(Terms) | AtomicIndividual | (Assertion) | (Terms) | {Terms}
Terms       -> Term | Terms, Term

AtomicIndividual  -> Constant | Variable 
Constant    -> 1 | 2 | True | False | pi | e ...
Variable    -> Parabola_C | Point_A ...

Operator    -> In | PointOnCurve 
             | Radius | Length | Sin 
             | Focus | Apex | ...
```

### Variable Declaration

This should be clear. Variables declare in this way:

```
var[, vars...]: Concept
```

### Syntactic Sugar

We use syntactic sugar (without ambiguity) in the annotation. This includes 

| Symbol   | Code   | Comments                             |
| -------- | ------ | ------------------------------------ |
| $=$      | =      |                                      |
| $\lt$    | <      |                                      |
| $\gt$    | >      |                                      |
| $\leq$   | <=     |                                      |
| $\geq$   | >=     |                                      |
| $+$      | +      |                                      |
| $-$      | -      |                                      |
| $\times$ | *      |                                      |
| $\div$   | /      |                                      |
| $a^b$    | \*\*,^ | power                                |
| $\ne$    |        | Not allowed! use `Negation` instead. |

## Individual, Concept, Operator Lookup Table

### Individual

Name|Description
-|-
axis| 坐标轴
xAxis| x轴
yAxis| y轴
oo| infinity
rad| 弧度
degree| 度
pi| 3.14 $\pi$

### Concept

Name|Description
-|-
Angle| 角
Real| 实数
Number| 数
Origin| 原点
Vector| 向量
Curve| 曲线
Triangle| 三角形
Axis| 坐标轴
Ray| 射线
LineSegment| 线段
Circle| 圆
Parabola| 抛物线
Hyperbola| 双曲线
Ellipse| 椭圆
ConicSection| 圆锥曲线
Line| 直线
Point| 点

### Operator

Not placed here...

## References

### 0 Default Individuals

### 0.1 Axis

Use `xAxis` to represent the X axis and `yAxis` to represent the Y axis.

No declarations!

:::info
Example:

点$P$在$x$轴上.

```
P: Point
PointOnCurve(P, xAxis) = True
```
:::

### 0.2 Origin

Unfortunately, you need to declare a new variable in order to represent the origin point:

:::info
Example:

椭圆$C$的中心在原点上.

```
O: Origin
Center(C) = O
```
:::

### 0.3 Constants

Feel free to use `pi` directly. Our system is quite familiar with this symbol.

### 0.4 rad, deg

The question may describe angles with units. You may use `applyUnit` to represent this:

:::info
Example:

$\angle ABC = 60^{\circ}$
```
A, B, C: Point
AngleOf(A,B,C) = ApplyUnit(60, degree)
```

$\angle ABC = \pi$
```
A, B, C: Point
AngleOf(A,B,C) = pi
```
:::

where `degree` is a pre-defined individual. You should not declare it again.

### 0.5 Infinity

Mostly it only appears in the answers. Use `oo` to represent $\infty$.

:::info
Example:

$[3, \infty)$
```
[3, oo)
```
:::

### 1 Entities with Properties

### 1.1 Expression

Basic expressions. Declare the variable, and write assertion(s) about its expression. Usually `Ellipse`, `Hyperbola`, `Parabola`, `Circle`, `Curve`, `Line` might have an expression.

If there are parameters in the expression, declare parameters like `a`, `b`, but not `x`, `y`. We never declare `x`, `y` since we think they are keywords.

If not explicitly mentioned, parameters are declared as `Number`.

Remember to write assertions about the constraints (if it exists).

:::info
Example:

已知椭圆$C_{1}: \frac{x^{2}}{a^{2}}+\frac{y^{2}}{b^{2}}=1(a>b>0)$.

```
C1: Ellipse
a, b: Number
a > b
b > 0
Expression(C1) = (x^2/a^2 + y^2/b^2 = 1)
```
:::


Be careful with the brackets`()` when using `=` !

:::danger
Example:

已知双曲线$C$:$\frac{x^{2}}{2m^{2}}-\frac{y^{2}}{n^{2}}=1$.

✖:
```
Expression(C) = x^2/2*m^2 - y^2/n^2 = 1
```

✔:
```
Expression(C) = (x^2/(2*m^2) - y^2/n^2 = 1)
```
:::


### 1.2 Coordinate

Tell the coordinate of a point.

Like the previous, if there are parameters in the expression, declare parameters like `a`, `b`, but not `x`, `y`. We never declare `x`, `y` since we think they are keywords.

If not explicitly mentioned, parameters are declared as `Number`.

:::info
Example:

点$P$的坐标为$(4,3m)$.

```
P: Point
m: Number
Coordinate(P) = (4, 3*m)
```
:::


### 1.3 LineSegment, Line, Vector

It is often to see 线段$AB$, 直线$OP$ in the question texts. We use a constructor operator to represent them:

:::info
Example:

线段$AB$...
```
A, B: Point
LineSegmentOf(A, B)...
```
:::

Similarly, we have `LineOf`, `VectorOf`. Also `TriangleOf`, `AngleOf`.

### 1.4 Distance, Length, Abs

These are the explanations for the three property operators:

`Distance`: 点到点、点到直线、直线到直线的距离
`Length`: xx的长度（题面中出现“长度”）
`Abs`: |...| 中间是向量或线段

We only represent the question texts, so write sentences as it is. 

:::info
Example:

线段$AB$的中点到$y$轴距离是3
```
Distance(MidPoint(LineSegmentOf(A, B)), yAxis) = 3
```

线段$PQ$长度的最小值为5
```
Min(Length(LineSegmentOf(P, Q))) = 5
```

$|AB|=4$
```
Abs(LineSegmentOf(A, B)) = 4
```

$|\overrightarrow{AB}|=4$
```
Abs(VectorOf(A, B)) = 4
```

$AB=4$
```
LineSegmentOf(A, B) = 4
```
:::

### 1.5 Vectors

There are two special things for vectors:

1. Use `DotProduct` to represent dot products.

:::info
Example:

$\overrightarrow{OA}\cdot\overrightarrow{OB}=0$

```
DotProduct(VectorOf(O, A), VectorOf(O, B)) = 0
```
:::

2. Use `0` itself to represent the zero vector($\overrightarrow{0}$, $\mathbf{0}$ ).


### 1.6 Angle

Simply use `AngleOf` to represent angles.

:::info
Example:

$\angle ABC = 60^{\circ}$
```
AngleOf(A,B,C) = ApplyUnit(60, degree)
```

$\angle ABC = \pi$
```
AngleOf(A,B,C) = pi
```

$\angle ABC = \angle BCD$
```
AngleOf(A,B,C) = AngleOf(B,C,D)
```

$\tan \angle ABC = 3$
```
Tan(AngleOf(A,B,C)) = 3
```
:::

### 2 Set Domain

### 2.1 Multi-output Operators

Write a set when and only when there're multiple outputs.

:::info
Example:

已知直线$L$与抛物线交于$A,B$两点,与椭圆交于点$C$.
```
Intersection(L, E1) = {A, B}
Intersection(L, E2) = C
```

抛物线与直线$L$的交点在$x$轴上.
```
PointOnCurve(Intersection(E, L), xAxis) = True
```

椭圆$C$的焦点在$y$轴上

```
PointOnCurve(Focus(C), yAxis) = True
```
:::

但不要在标注时直接表达：

:::danger
✖:
```
PointOnCurve({A, B}, C) = True
```

✔:
```
PointOnCurve(A, C) = True
PointOnCurve(B, C) = True
```
:::

### 2.2 Interval

Mostly it only appears in the answers. The same representation as in math. Use `+` to represent union.

:::info
Example:

直线$l$斜率的取值范围为$(2,3)$.
```
Range(Slope(l))=(2,3)
```

Further more:
$x$的取值范围为$(-\infty,-1]\cup(0,\infty)$.
```
Range(x)=(-oo,-1]+(0,oo)
```
:::

### 2.3 +-

We convert $\pm$ symbol into a set in our representation.

:::danger
This was an early decision that makes L do some rephasing work. Future work is required.
:::

:::info
Example:

双曲线$C$的渐近线方程为$y=\pm\sqrt{3}x$.

```
Expression(Asymptote(C)) = {Eq(y, sqrt(3)*x), Eq(y, -sqrt(3)*x)}
```
:::

### 2.4 OneOf

Sometimes we need to deal with 'oneof' relationships. We treat it as picking an element from a set.

:::danger
This was an early decision that makes L do some rephasing work. Future work is required.
:::

:::info
Example:

已知双曲线$\frac{x^{2}}{a^{2}}-\frac{y^{2}}{b^{2}}=1(a>0,b>0)$的**一条**渐近线与直线$x+2y-1=0$垂直.

```
l: Line
In(l, Asymptote(C)) = True
...
```

Example:

圆$C$经过双曲线的**一个**顶点和**一个**焦点.

```
C: Circle
E: Hyperbola
P, Q: Point
In(P, Vertex(E)) = True
In(Q, Focus(E)) = True
PointOnCurve(P, C) = True
PointOnCurve(Q, C) = True
```
:::

### 3 Relationships

### 3.1 Tangent

We mainly have two kinds of relationships about tangent: '在…点处的切线', '过…点的切线'. The former one indicates that the point is on the curve, while the later one does not.

Others just follow the operator definitions.

:::danger
The naming of the operators might be inappropriate. We should use 'tangent' instead of 'tangency'. Future work is required.
:::

:::info
Example:

圆$E$与$x$轴相切
```
IsTangency(E, xAxis) = True
```

圆$E$与$x$轴相切于椭圆的右焦点$F$

```
F: Point
RightFocus(C) = F
TangencyPoint(E, xAxis) = F
```

过$F$作圆$O$的两条切线,记切点为$A$、$B$
```
l1, l2: Line
TangentOfPoint(F, O) = {l1, l2}
A, B: Point
TangencyPoint(l1, O) = A
TangencyPoint(l2, O) = B
```

抛物线$y=x^{2}$在点$P$处的切线平行于直线$y=4x-5$.
```
C: Parabola
Expression(C) = ( y = x^2 )
D: Line
Expression(D) = ( y = 4*x - 5 )
P: Point
IsParallel(TangentOnPoint(P, C), D) = True
```
:::

### 3.2 Chord

Chord is a relationship describing a line segment with two end points on a curve.

There are currently two operators related to chord: `IsChordOf`, `InterceptChord`.

:::info
Example:

直线$y=x$被曲线$2x^{2}+y^{2}=2$截得的弦长为?
```
l: Line
C: Curve
Length(InterceptChord(l, C)) = ?
```

已知$AB$是过抛物线$y^{2}=2x$焦点的弦
```
A, B: Point
C: Parabola
IsChordOf(LineSegmentOf(A, B), C) = True
PointOnCurve(Focus(C), LineSegmentOf(A, B)) = True
```
:::

If the question mentions 弦$AB$, then you are required to represent this chord relationship.

:::info
Example:

过点$M(1,1)$ 作一条直线与椭圆$x^2/9+y^2/4=1$相交于$A$、$B$两点,若$M$点恰好为弦$AB$的中点,则$AB$所在直线的方程为?
```
M: Point
Coordinate(M) = (1, 1)
l: Line
PointOnCurve(M, l) = True
C: Parabola
Expression(C) = (x^2/9 + y^2/4 = 1)
A, B: Point
Intersection(l, C) = {A, B}
IsChordOf(LineSegmentOf(A, B), C) = True
MidPoint(LineSegmentOf(A, B)) = M
Expression(OverlappingLine(LineSegmentOf(A, B))) = ?
```
:::


### 4 Special Notice

### 4.1 No Rephrasing

Do NOT rephrase the sentence. Stick to the orginal expression.

:::danger
Example:
抛物线 $y=(x−2)^2+3$ 的顶点在直线$l$上。

✖:
```
E: Ellipse
Expression(E) = (y = (x-2)^2 + 3)
P: Point
P = Vertex(E)
l: Line
PointOnCurve(P, l) = True
```

✔:
```
E: Ellipse
Expression(E) = (y = (x-2)^2 + 3)
l: Line
PointOnCurve(Vertex(E), l) = True
```
:::

:::danger
Example:
抛物线 $y=(x−2)^2+3$ 的顶点$P$在直线$l$上。

✖:
```
E: Ellipse
Expression(E) = (y = (x-2)^2 + 3)
l: Line
PointOnCurve(Vertex(E), l) = True
```

✔:
```
E: Ellipse
Expression(E) = (y = (x-2)^2 + 3)
P: Point
P = Vertex(E)
l: Line
PointOnCurve(P, l) = True
```
:::


## Cannot Annotate

### Instruction

What questions cannot get annotated?

0. Out of the question;
1. Questions that are lack of operators/concepts;
2. Questions that need rephrase to annotate;
3. Questions that you are not sure how to annotate;
4. ...

### Categorization

We divide all questions that cannot be annotated into the following categories:
1. Lack of Concepts/Individuals/Opeartors;
2. Question type does not match (E.g. Multiple Choices, Picture involved, etc.);
3. Involving knowledge in other domains;
4. Question proposes new definitions;
5. Ambiguous question description;
6. Others.


