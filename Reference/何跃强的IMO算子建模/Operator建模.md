# Operator

#### Arithmetical Operation (16)

Add:定义域{(数值),(数值)}, 值域{数值} # 加法运算

Minus: 定义域{(数值),(数值)}, 值域{数值} # 减法运算，Minus(a,b) -> a-b

Multiply: 定义域{(数值),(数值)}, 值域{数值} # 乘法运算

Divide: 定义域{(数值),(数值)}, 值域{数值} # 除法运算，Divide(a,b) -> a/b

Power: 定义域{(数值),(数值)}, 值域{数值} # 幂法运算，Power(a,b) -> $a^b$



==Tan: 定义域{角}，值域{数值} #获取角的正切值==

==Cos: 定义域{角}，值域{数值} #获取角的余弦值==

==Sin: 定义域{角}，值域{数值} #获取角的正弦值==

###### Compare

GreaterThan: 定义域{(数值),(数值)}, 值域{boolean} # 大于 GreaterThan(a,b) -> $a>b$

LessThan: 定义域{(数值),(数值)}, 值域{boolean} # 小于 LessThan(a,b) -> $a<b$

GreaterOrEqualThan: 定义域{(数值),(数值)}, 值域{boolean} # 大等于 GreaterOrEqualThan(a,b) -> $a \ge b$

LessOrEqualThan: 定义域{(数值),(数值)}, 值域{boolean} # 大等于 LesssOrEqualThan(a,b) -> $a \le b$



==Maximum: 定义域{函数}，值域{数值} #获取某表达式的最大值==

==Minimum: 定义域{函数}，值域{数值} #获取某表达式的最小值==

==ValueRange: 定义域{函数}，值域{数值} #获取某表达式的取值范围==

AbsoluteValue: 定义域{数值}，值域{数值} #获取绝对值



#### Set Operation (4)

SetUnion: 定义域{(集合),(集合)}, 值域{集合} # 集合的并 SetUnion(A,B) -> $A \cup B$

SetIntersection: 定义域{(集合),(集合)}, 值域{集合} # 集合的交 SetIntersection(A,B) ->  $A \cap B$

SetDifference: 定义域{(集合),(集合)}, 值域{集合} # 集合的差集 SetDifference(A,B) -> $A - B$

<u>In: 定义域{(Term,Individual,Assertion),(集合)}, 值域{boolean} # 元素(Term/Individual/Assertion)是否在集合中</u>



#### Logical Operation (7)

<u>Negation: 定义域{Assertion}, 值域{Assertion} # 否，取反， $\neg$</u>

==Conjunction: 定义域{(Assertion),(Assertion)}, 值域{list of Assertions} # 合取 and==

==Disjunction: 定义域{(Assertion),(Assertion)}, 值域{list of Assertions} # 析取 or==

==Implication: 定义域{(list of Assertions),(list of Assertions)}, 值域{list of Assertions} # 蕴涵==

==Equivalence: 定义域{(list of Assertions),(list of Assertions)}, 值域{list of Assertions} # 等价==

==Universal: 定义域{(list of individuals/Term),(list of Assertions)}, 值域{list of Assertions} # 全称量词==

==Existence: 定义域{(list of individuals/Term),(list of Assertions)}, 值域{list of Assertions} # 存在量词==



#### Conic Section (44)

<u>ConicEquationExpression: 定义域{(椭圆，抛物线，双曲线，圆)}, 值域 {等式}. # 获取圆锥曲线的表示方程</u>

Eccentricity: 定义域{椭圆, 双曲线, 抛物线}, 值域{数值} #获取离心率

FocalRadius: 定义域{(圆锥曲线)，(点)}, 值域{数值} #获取圆锥曲线上点的焦半径

LeftPart: 定义域{椭圆，双曲线}， 值域{曲线} #获取椭圆、双曲线的左支

RightPart: 定义域{椭圆，双曲线}， 值域{曲线} #获取椭圆、双曲线的右支

<u>UpPart: 定义域{椭圆，双曲线}， 值域{曲线} #获取椭圆、双曲线的上支</u>

<u>DownPart: 定义域{椭圆，双曲线}， 值域{曲线} #获取椭圆、双曲线的下支</u>

FocalLength: 定义域{椭圆, 双曲线, 抛物线}, 值域{数值} #获取焦距

###### Focus

> 椭圆：
>
> ​		$\frac{x^2}{a^2}+\frac{y^2}{b^2}=1\, (a>b)\;\; \Longrightarrow \;\; F_1(-c,0),F_2(c,0)$		
>
> ​		$\frac{y^2}{a^2}+\frac{x^2}{b^2}=1\, (a>b)\;\; \Longrightarrow \;\; F_1(0,c),F_2(0,-c)$	
>
> ​		$\frac{(x-x_0)^2}{a^2}+\frac{(y-y_0)^2}{b^2}=1\, (a>b)\;\; \Longrightarrow \;\; F_1(-c+x_0,y_0),F_2(c+x_0,y_0)$
>
> 双曲线：
>
> ​		$\frac{x^2}{a^2}-\frac{y^2}{b^2}=1\, (a>b)\;\; \Longrightarrow \;\; F_1(-c,0),F_2(c,0)$
>
> ​		$\frac{y^2}{a^2}-\frac{x^2}{b^2}=1\, (a>b)\;\; \Longrightarrow \;\;F_1(0,c),F_2(0,-c)$
>
> 抛物线：
>
> ​		$y^2=2px\;\; \Longrightarrow \;\; F(\frac{p}{2},0)$
>
> ​		$x^2=2py\;\; \Longrightarrow \;\; F(0,\frac{p}{2})$

<u>Focus: 定义域{椭圆,双曲线,抛物线}, 值域{点,(点, 点)} #获取焦点 -> 一个点/两个点的集合</u>

LeftFocus:定义域{椭圆，双曲线，抛物线}，值域{点} #获取左焦点坐标

RightFocus:定义域{椭圆，双曲线，抛物线}，值域{点} #获取右焦点坐标

UpFocus: 定义域{椭圆，双曲线，抛物线}，值域{点} #获取上焦点坐标

DownFocus: 定义域{椭圆，双曲线，抛物线}，值域{点} #获取下焦点坐标

###### Directrix

> 椭圆：垂直于长轴
>
> ​		$\frac{x^2}{a^2}+\frac{y^2}{b^2}=1\, (a>b)\;\; \Longrightarrow \;\; x= \pm \frac{a^2}{c}$
>
> ​		$\frac{x^2}{b^2}+\frac{y^2}{a^2}=1\, (a>b)\;\; \Longrightarrow \;\; y= \pm \frac{a^2}{c}$
>
> ​		$\frac{(x-x_0)^2}{a^2}+\frac{(y-y_0)^2}{b^2}=1\, (a>b)\;\; \Longrightarrow \;\; x= \pm \frac{a^2}{c}+x_0$
>
> 双曲线：
>
> ​		$\frac{x^2}{a^2}-\frac{y^2}{b^2}=1\, (a>b)\;\; \Longrightarrow \;\; x= \pm \frac{a^2}{c}$
>
> ​		$\frac{y^2}{a^2}-\frac{x^2}{b^2}=1\, (a>b)\;\; \Longrightarrow \;\; y= \pm \frac{a^2}{c}$
>
> 抛物线：
>
> ​		$y^2=2px\;\; \Longrightarrow \;\; x= - \frac{p}{2}$
>
> ​		$x^2=2py\;\; \Longrightarrow \;\; y= - \frac{p}{2}$

LeftDirectrix: 定义域{椭圆,双曲线}, 值域{直线} #获取椭圆/双曲线 的左准线

RightDirectrix: 定义域{椭圆,双曲线}, 值域{直线} #获取椭圆/双曲线 的右准线

UpDirectrix: 定义域{椭圆,双曲线}, 值域{直线} #获取椭圆/双曲线 的上准线

DownDirectrix: 定义域{椭圆,双曲线}, 值域{直线} #获取椭圆/双曲线 的下准线

<u>Directrix: 定义域{椭圆,双曲线,抛物线}, 值域{直线, set(直线,直线)} #获取椭圆/双曲线/抛物线 的准线</u>

###### SymmetryAxis

<u>SymmetryAxis: 定义域{椭圆,双曲线,抛物线}，值域{直线, set(直线,直线)} #获取椭圆/双曲线/抛物线的对称轴</u>

###### FocalRadius

RightFocalRadius: 定义域{(椭圆,双曲线,抛物线)，(点)}, 值域{数值} #获取圆锥曲线上点与右焦点的焦半径

LeftFocalRadius: 定义域{(椭圆,双曲线,抛物线)，(点)}, 值域{数值} #获取圆锥曲线上点与左焦点的焦半径

HigherFocalRadius: 定义域{(椭圆,双曲线,抛物线)，(点)}, 值域{数值} #获取圆锥曲线上点与上焦点的焦半径

LowerFocalRadius: 定义域{(椭圆,双曲线,抛物线)，(点)}, 值域{数值} #获取圆锥曲线上点与下焦点的焦半径

###### Focus Location

FocusOnXAxis: 定义域{椭圆,双曲线}，值域{Boolean} #椭圆/双曲线 焦点在x轴上

FocusOnYAxis: 定义域{椭圆,双曲线}，值域{Boolean} #椭圆长轴/双曲线 焦点在y轴上



Major_P_XAxis: 定义域{椭圆,双曲线}，值域{Boolean} #椭圆长轴/双曲线实轴 与x轴平行

Major_P_YAxis: 定义域{椭圆,双曲线}，值域{Boolean} #椭圆长轴/双曲线实轴 与y轴平行



<u>P_Flag: 定义域{抛物线}，值域{数值} #抛物线参数p前的正负，表示焦点在正负哪个半轴上，值域={-1,1}</u>

###### Apex

<u>Apex: 定义域{椭圆,双曲线,抛物线,三角形}， 值域{点的集合} #获取圆锥曲线/三角形的顶点</u>

ConicUpVertex: 定义域{椭圆，双曲线}， 值域 {点}. # 获取椭圆或双曲线的上顶点。

ConicDownVertex: 定义域{椭圆，双曲线}， 值域 {点}. # 获取椭圆或双曲线的下顶点。

ConicLeftVertex: 定义域{椭圆，双曲线}， 值域 {点}. # 获取椭圆或双曲线的左顶点。

ConicRightVertex: 定义域{椭圆，双曲线}， 值域 {点}. # 获取椭圆或双曲线的右顶点。

###### Oval

LongerAxis: 定义域{椭圆}, 值域{线段} #获取椭圆的长轴

ShorterAxis: 定义域{椭圆}, 值域{线段} #获取椭圆的短轴

###### Hyperbola

RealAxis: 定义域{双曲线}，值域{线段} #获取双曲线的实轴

VirtualAxis: 定义域{双曲线}，值域{线段} #获取双曲线的虚轴

<u>Asymptote: 定义域{双曲线}，值域{set(直线,直线)} #获取双曲线的渐近线方程</u>

###### Parabola

// SymmetryAxis: 定义域{抛物线}，值域{直线} #获取抛物线的对称轴

###### Parameter

ParameterA: 定义域{椭圆，双曲线}，值域{数值} #获取圆锥曲线参数a>0

ParameterB: 定义域{椭圆，双曲线}，值域{数值} #获取圆锥曲线参数b>0

ParameterC: 定义域{椭圆，双曲线}，值域{数值} #获取圆锥曲线参数c>0

ParameterP: 定义域{抛物线}，值域{数值} ##获取抛物线参数p

Diameter: 定义域{圆}，值域{线段} #获取该圆的直径

Radius: 定义域{圆}，值域{直线} #获取该圆的半径

Center: 定义域{圆，椭圆，双曲线，抛物线}，值域{点} #获取该圆锥曲线的中心

ParameterX0: 定义域{椭圆，双曲线，抛物线,圆}，值域{数值}# 获取圆、椭圆、双曲线、抛物线的中心横坐标

ParameterY0:定义域{椭圆，双曲线，抛物线,圆}，值域{数值}# 获取圆、椭圆、双曲线、抛物线的中心纵坐标



#### Curve Relation (11)

<u>IntersectionPoint: 定义域{(直线，圆锥曲线),(直线，圆锥曲线)}，值域{set of Points} #获取输入的两个曲线的交点</u>

NumberOfIntersection: 定义域{(直线，圆锥曲线),(直线，圆锥曲线)},值域{数值} #获取两个对象的公共点/交点个数

PointOnCurve: 定义域{(点)，(圆锥曲线,直线)}，值域{boolean} #判断点是否在圆锥曲线/直线上



IsTangency: 定义域{(直线，圆锥曲线),(直线，圆锥曲线)}，值域{boolean} #判断是否相切

IsIntersect: 定义域{(直线，圆锥曲线),(直线，圆锥曲线)}，值域{boolean} #判断是否相交

IsSeparated: 定义域{(直线，圆锥曲线),(直线，圆锥曲线)}，值域{boolean} #判断是否相离

IsParallel：定义域{(直线)，(直线)}，值域{boolean} #判断两直线是否平行



Distance: 定义域{(点，直线)，(点，直线)}，值域{数值} #获取 两直线/两点/点到直线 的距离

Length: 定义域{线段}，值域{数值} #获取线段的长度



FixedPointTangent: 定义域{(点)，(圆锥曲线)}，值域{直线} #获取过某点的切线

<u>FixedSlopeTangent: 定义域{(数值)，(圆锥曲线)}，值域{直线,set(直线,直线)} #获取某曲线上以某值为斜率的切线方程（可能有两条）</u>



#### Line (8)

<u>LineEquationExpression: 定义域{直线}, 值域{等式}. # 获取直线方程</u>

EndpointLineSegment: 定义域{(点)，(点)}，值域{线段} #根据端点构建线段

OverlappedLine: 定义域{线段}，值域{直线} #与给定线段重合的直线

Slope: 定义域{直线,线段}，值域{实数}  #获取斜率

==AngleOfInclination:定义域{直线,线段}，值域{角} #获取倾斜角==

Intercept: 定义域{直线,线段}，值域{实数} #获取截距

<u>Endpoint: 定义域{线段，射线}，值域{点，set(点，点)} #获取线段/射线的端点</u>

<u>EquallyDivide: 定义域{(线段),(数值)}，值域{点的集合} #EquallyDivide(线段,k) -> 获取线段的k等分点</u>





#### Coordinate (5)

<u>PointCoordinate: 定义域{点},值域{坐标} #获取该点坐标 (x,y)形式</u>

XCoordinate: 定义域{点}，值域{数值} #获取点的横坐标

YCoordinate: 定义域{点}，值域{数值} #获取点的纵坐标

MidPoint: 定义域{线段}，值域{点} #获取线段的中点

BetweenTwoPoints: 定义域{(点)，(点)，(点)}， 值域{boolean} #BetweenTwoPoints(1,2,3) -> 判断点1是否在点2和点3之间



#### Vector (2)

VectorInstance: 定义域{(点)，(点)}， 值域{向量} #根据给定点构建向量{(起点)，(终点)}

DotProduct: 定义域{(向量)，(向量)}，值域{数值} #向量的点乘



#### Triangle/Geometry (4)

==PointTriangle: 定义域{(点)，(点)，(点)}，值域{三角形} #根据三个点构建三角形==

==CircumCircle: 定义域{三角形}，值域{圆} #获取三角形的外接圆方程==

==InscribedCircle: 定义域{三角形}，值域{圆} #获取三角形的内切圆方程==

==Area: 定义域{平面/二维几何}，值域{数值} #获取某平面几何的面积==



#### Preprocessing (9)

GetParameterX0FromExpression: 定义域{椭圆，双曲线，抛物线}，值域{数值}# 从方程中获取椭圆、双曲线、抛物线的中心横坐标

GetParameterY0FromExpression: 定义域{椭圆，双曲线，抛物线}，值域{数值}# 从方程中获取椭圆、双曲线、抛物线的中心纵坐标

GetCenterFromExpression:  定义域{椭圆，双曲线，抛物线}，值域{点}# 从方程中获取椭圆、双曲线、抛物线的中心点

GetParameterAFromExpression: 定义域{椭圆，双曲线}，值域{数值} #从方程中获取椭圆、双曲线的参数a

GetParameterBFromExpression: 定义域{椭圆，双曲线}，值域{数值} # 从方程中获取椭圆、双曲线的参数b

GetParameterPFromExpression: 定义域{抛物线}，值域{数值} # 从方程中获取抛物线的参数p>0

GetSlopeFromExpression: 定义域{直线}, 值域{数值}, #自动获取直线斜率

GetInterceptFromExpression: 定义域{直线}, 值域{数值}, #自动获取直线截距

FocusJudge: 定义域{椭圆，双曲线}，值域{boolean}#判断焦点位置，True：长轴(实轴)与x轴平行，False：长轴(实轴)与y轴平行

<u>GetValueByIndex: 定义域{(Set,List),(数值)}, 值域{数值} #定义域中的数值为index，(x1,x2,...),输出第index位的值</u>

<u>Get_P_Flag: 定义域{抛物线}，值域{数值}# 从方程中获取 抛物线参数p前的正负</u>



#### Angle

==ApplyUnit: 定义域{(数值),(unit)}, 值域{(角度)}==

==AngleValue: 定义域{(角)}, 值域{(角度)}==



#### Other (3)

==Trajectory: 定义域{点}, 值域{曲线方程} # 获取动点的轨迹方程==

<u>Average: 定义域{set of Points}, 值域{(点)} # 获取点的均值</u>

<u>SubstitutePoint: 定义域{(点), (表达式)}, 值域{(表达式)} #将点代入曲线表达式，替换</u>



GenerateOvalExpression: 定义域{(数值),(数值),(点),(boolean)}, 值域{(表达式)} 

#生成椭圆标准方程 {(ParameterA),(ParameterB),(Center),(Major_P_XAxis)} -> $\frac{(x-x_0)^2}{a^2}+\frac{(y-y_0)^2}{b^2}=1\;\;or\;\;\frac{(x-x_0)^2}{b^2}+\frac{(y-y_0)^2}{a^2}=1$

GenerateHyperbolaExpression: 定义域{(数值),(数值),(点),(boolean)}, 值域{(表达式)} 

#生成双曲线方程 {(ParameterA),(ParameterB),(Center),(Major_P_XAxis)} ->  $\frac{(x-x_0)^2}{a^2}-\frac{(y-y_0)^2}{b^2}=1\;\;or\;\;\frac{(y-y_0)^2}{b^2}-\frac{(x-x_0)^2}{a^2}=1$

GenerateLineExpression: 定义域{(数值),(数值)}, 值域{(表达式)} 

#生成直线方程（斜率存在）。定义域：{(Slope),(Intercept)} -> $y = kx+b$

> 斜率不存在情况；两点生成直线；一点+斜率；斜率不存在+一点



```
椭圆，双曲线
FocusOnXAxis, FocusOnYAxis
MajorAxisDirection	= 0 与x轴平行
										= 1 与y轴平行
长轴倾角 0/90
rotation angle

抛物线
SymmetryDirection
```

