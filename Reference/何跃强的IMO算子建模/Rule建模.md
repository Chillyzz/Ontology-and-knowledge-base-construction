# Rule

> VariableDeclaration; (Body ->) Head #comment
>
> 73

## Preprocessing(16)

x: Oval;    GreaterThan(ParameterA(x), ParameterB(x)) #椭圆 参数a>参数b

x: Oval, Hyperbola ;  ParameterA(x) = GetParameterAFromExpression(x) #获取 <椭圆/双曲线> 的参数a

x: Oval, Hyperbola ;  ParameterB(x) = GetParameterBFromExpression(x) #获取 <椭圆/双曲线> 的参数a

x: Oval, Hyperbola, Parabola, Circle ;  ParameterX0(x) = GetParameterX0FromExpression(x)#获取 <椭圆/双曲线/抛物线/圆> 的参数x0

x: Oval, Hyperbola, Parabola, Circle ;  ParameterY0(x) = GetParameterY0FromExpression(x)#获取 <椭圆/双曲线/抛物线/圆> 的参数y0

x: Oval, Hyperbola, Parabola, Circle ;  Center(x) = GetCenterFromExpression(x)#获取 <椭圆/双曲线/抛物线/圆> 的中心

x: Oval, Hyperbola, Parabola, Circle ;  XCoordinate(Center(x)) = ParameterX0(x), YCoordinate(Center(x)) = ParameterY0(x) # <椭圆/双曲线/抛物线/圆>中心坐标 与 x0，y0关系

<u>x: Parabola; ParameterP(x) = GetParameterPFromExpression(x) #获取抛物线参数p</u>

<u>x: Parabola; P_Flag(x) = Get_P_Flag(x) # 获取抛物线参数p的正负号</u>

x: Line ;  Slope(x) = GetSlopeFromExpression(x) #获取直线斜率

x: Line ;  Intercept(x) = GetInterceptFromExpression(x) #获取直线截距

✒︎ x: Oval, Hyperbola, Parabola; FocusJudge(x)=True -> Major_P_XAxis(x) = True, Major_P_YAxis(x) = False #判断<椭圆/双曲线/抛物线>焦点连线与x轴平行

✒︎ x: Oval, Hyperbola, Parabola; FocusJudge(x)=False -> Major_P_XAxis(x) = False, Major_P_YAxis(x) = True #判断<椭圆/双曲线/抛物线>焦点连线与y轴平行

✒︎ x: Oval, Hyperbola, Parabola; FocusOnXAxis(x)=True -> Major_P_XAxis(x) = True, Major_P_YAxis(x) = False, ParameterY0(x)=0 #<椭圆/双曲线> 焦点在x轴上，则其焦点联系与x轴平行，系数y0=0

✒︎ x: Oval, Hyperbola, Parabola; FocusOnYAxis(x)=True -> Major_P_YAxis(x) = True, Major_P_XAxis(x) = False, ParameterX0(x)=0 #<椭圆/双曲线> 焦点在x轴上，则其焦点联系与y轴平行，系数x0=0

> p: Point; PointCoordinate(p) = (XCoordinate(p),YCoordinate(p))

<u>p: Point; XCoordinate(p) = GetValueByIndex(PointCoordinate(p),0), YCoordinate(p) = AssignPointValue(PointCoordinate(p),1) # 分别获取一个点的横纵坐标</u>

## Other

#### Conic Section (38+)

x:Oval;    ParameterA(x)^2 - ParameterB(x)^2 = ParameterC(x)^2  #椭圆 $a^2-b^2=c^2$

x:Hyperbola;    ParameterA(x)^2 + ParameterB(x)^2 = ParameterC(x)^2  # 双曲线 $a^2+b^2=c^2$



###### Focus Point

x: Oval, Hyperbola; Major_P_XAxis(x)=True -> Xcoordinate(RightFocus(x)) = ParameterC(x)+ParameterX0(x), Ycoordinate(RightFocus(x)) = ParameterY0(x) #<椭圆/双曲线>当焦点连线与x轴平行时，右焦点坐标为 $(c+x_0,y_0)$

x: Oval, Hyperbola; Major_P_XAxis(x)=True -> Xcoordinate(LeftFocus(x)) = - ParameterC(x)+ParameterX0(x), Ycoordinate(LeftFocus(x)) = ParameterY0(x) #<椭圆/双曲线>当焦点连线与x轴平行时，左焦点坐标为 $(-c+x_0,y_0)$

x: Oval, Hyperbola; Major_P_XAxis(x)=True -> Focus(x) = ==set==(RightFocus(x), LeftFocus(x))



x: Oval, Hyperbola; Major_P_YAxis(x)=True -> Xcoordinate(UpFocus(x)) = ParameterX0(x), Ycoordinate(UpFocus(x)) = ParameterC(x)+ParameterY0(x) #<椭圆/双曲线>当焦点连线与y轴平行时，上焦点坐标 $(x_0,y_0+c)$

x: Oval, Hyperbola; Major_P_YAxis(x)=True -> Xcoordinate(DownFocus(x)) = ParameterX0(x), Ycoordinate(DownFocus(x)) = - ParameterC(x)+ParameterY0(x) #<椭圆/双曲线>当焦点连线与y轴平行时，下焦点坐标 $(x_0,y_0-c)$

x: Oval, Hyperbola; Major_P_YAxis(x)=True -> Focus(x) = ==set==(UpFocus(x), DownFocus(x))



<u>x: Parabola; Major_P_XAxis(x)=True -> ParameterP(x) = 2 * P_Flag(x) * (XCoordinate(Focus(x)) - ParameterX0(x)), YCoordinate(Focus(x))=ParameterY0(x) #对称轴平行于x轴-> F(p/2+x_0,y_0), p=p_flag * (焦点横坐标-x_0) * 2, 焦点纵坐标=y_0</u>

<u>x: Parabola; Major_P_YAxis(x)=True -> ParameterP(x) = 2 * P_Flag(x) * (YCoordinate(Focus(x)) - ParameterY0(x)), XCoordinate(Focus(x))=ParameterX0(x) #对称轴平行于y轴-> F(x_0,p/2+y_0), p=p_flag * (焦点纵坐标-y_0) * 2, 焦点横坐标=x_0</u>



捷径

x: Oval, Hyperbola; Major_P_XAxis(x)=True -> XCoordinate(RightFocus(x)) + XCoordinate(LeftFocus(x)) = 2 * ParameterX0(x), YCoordinate(RightFocus(x)) + YCoordinate(LeftFocus(x)) = 2 * ParameterY0(x) # <椭圆/双曲线>长轴（实轴）与x轴平行， $F_1(-c+x_0,y_0),F_2(c+x_0,y_0),F_1+F_2 = 2(x_0,y_0)$ ; 左右焦点关系

x: Oval, Hyperbola; Major_P_YAxis(x)=True -> XCoordinate(UpFocus(x)) + XCoordinate(DownFocus(x)) = 2 * ParameterX0(x), YCoordinate(UpFocus(x)) + YCoordinate(DownFocus(x)) = 2 * ParameterY0(x) # <椭圆/双曲线>长轴（实轴）与y轴平行， $F_1(x_0,-c+y_0),F_2(x_0,c+y_0),F_1+F_2 = 2(x_0,y_0)$; 上下焦点关系



###### Eccentricity

x:Oval, Hyperbola; Eccentricity(x)=ParameterC(x)/ParameterA(x)  # <椭圆/双曲线>离心率 e=c/a

x: Parabola;    Eccentricity(x)=1 #抛物线离心率=1

x: Circle;    Eccentricity(x)=0 #圆离心率=0



###### FocalRadius

x:Oval, p:Point;    PointOnCurve(p,x)=True -> AbsoluteValue(RightFocalRadius(x,p)+LeftFocalRadius(x,p))=2*ParameterA(x)  #$||PF1|+|PF2||=2a$

x:Hyperbola, p:Point;    PointOnCurve(p,x)=True -> AbsoluteValue(RightFocalRadius(x,p) - LeftFocalRadius(x,p))=2*ParameterA(x)  #$||PF1|-|PF2||=2a$



x:Oval, p:Point;    PointOnCurve(p,x)=True, Major_P_XAxis(x)=True  -> RightFocalRadius(x,p) = ParameterA(x)-Eccentricity(x) * (XCoordinate(p)-ParameterX0(x)) #焦点在X轴上->右焦半径 $|PF_2|=a-e(x-x_0)$

x:Oval, p:Point;    PointOnCurve(p,x)=True, Major_P_XAxis(x)=True  -> LeftFocalRadius(x,p) = ParameterA(x)+Eccentricity(x)* (XCoordinate(p) - ParameterX0(x)) #焦点在X轴上->左焦半径 $|PF1|=a+e(x-x_0)$

x:Oval, p:Point;    PointOnCurve(p,x)=True, Major_P_YAxis(x)=True  -> HigherFocalRadius(x,p) = ParameterA(x)-Eccentricity(x)* (YCoordinate(p) - ParameterY0(x)) #焦点在Y轴上->上焦半径 $|PF2|=a-e(y-y_0)$

x:Oval, p:Point;    PointOnCurve(p,x)=True, Major_P_YAxis(x)=True -> LowerFocalRadius(x,p) = ParameterA(x)+Eccentricity(x)* (YCoordinate(p) - ParameterY0(x)) #焦点在Y轴上->下焦半径 $|PF1|=a+e(y-y_0)$



<img src="/Users/katherine/Library/Application Support/typora-user-images/image-20211113093632585.png" alt="image-20211113093632585" style="zoom:50%;" />

x:Hyperbola, p:Point; PointOnCurve(p,RightPart(x))=True, Major_P_XAxis(x)=True ->  LeftFocalRadius(x,p) = ParameterA(x)+Eccentricity(x)* (XCoordinate(p) - ParameterX0(x)) #双曲线，p在右支，左焦半径 $|PF1|=a+e(x-x_0)$

x:Hyperbola, p:Point; PointOnCurve(p,RightPart(x))=True, Major_P_XAxis(x)=True ->  RightFocalRadius(x,p) = -ParameterA(x)+Eccentricity(x)* (XCoordinate(p) - ParameterX0(x)) #双曲线，p在右支，右焦半径 $|PF1|=-a+e(x-x_0)$

<u>x:Hyperbola, p:Point; PointOnCurve(p,LeftPart(x))=True, Major_P_XAxis(x)=True ->  LeftFocalRadius(x,p) = -ParameterA(x)-Eccentricity(x)* (XCoordinate(p) - ParameterX0(x)) #双曲线，p在左支，左焦半径 $|PF1|=-a-e(x-x_0)$</u>

<u>x:Hyperbola, p:Point; PointOnCurve(p,LeftPart(x))=True, Major_P_XAxis(x)=True ->  RightFocalRadius(x,p) = ParameterA(x)-Eccentricity(x)* (XCoordinate(p) - ParameterX0(x)) #双曲线，p在左支，右焦半径 $|PF1|=a-e(x-x_0)$</u>



<u>x:Hyperbola, p:Point; PointOnCurve(p,UpPart(x))=True, Major_P_YAxis(x)=True ->  LeftFocalRadius(x,p) = ParameterA(x)+Eccentricity(x)* (YCoordinate(p) - ParameterY0(x)) #双曲线，p在上支，下焦半径 $|PF1|=a+e(y-y_0)$</u>

<u>x:Hyperbola, p:Point; PointOnCurve(p,UpPart(x))=True, Major_P_YAxis(x)=True ->  RightFocalRadius(x,p) = -ParameterA(x)+Eccentricity(x)* (YCoordinate(p) - ParameterY0(x)) #双曲线，p在上支，上焦半径 $|PF1|=-a+e(y-y_0)$</u>

<u>x:Hyperbola, p:Point; PointOnCurve(p,DownPart(x))=True, Major_P_YAxis(x)=True ->  LeftFocalRadius(x,p) = -ParameterA(x)-Eccentricity(x)* (YCoordinate(p) - ParameterY0(x)) #双曲线，p在下支，下焦半径 $|PF1|=-a-e(y-y_0)$</u>

<u>x:Hyperbola, p:Point; PointOnCurve(p,DownPart(x))=True, Major_P_YAxis(x)=True ->  RightFocalRadius(x,p) = ParameterA(x)-Eccentricity(x)* (YCoordinate(p) - ParameterY0(x)) #双曲线，p在下支，上焦半径 $|PF1|=a-e(y-y_0)​</u>$





x:Oval, Hyperbola;  Major_P_XAxis(x)=True -> Distance(LeftFocus(x),RightFocus(x)) = 2*ParameterC(x)  #|F1F2|=2c

x:Oval, Hyperbola;  Major_P_YAxis(x)=True ->  Distance(UpFocus(x),DownFocus(x)) = 2*ParameterC(x)  #|F1F2|=2c



<u>x: Parabola, p: Point; PointOnCurve(p,x)=True -> FocalRadius(x,p)=Distance(p,Directrix(x)) #抛物线上点到准线距离等于焦半径长度</u>

<u>x: Parabola, p: Point;   PointOnCurve(p,x)=True, Major_P_XAxis(x)=True -> FocalRadius(x) = ParameterP(x)/2 + AbsoluteValue(XCoordinate(p) - ParameterX0(x)) #$|PF|= |p_x-x_0|+p/2$</u>

<u>x: Parabola, p: Point;   PointOnCurve(p,x)=True, Major_P_YAxis(x)=True,  -> FocalRadius(x) = ParameterP(x)/2 + AbsoluteValue(YCoordinate(p) - ParameterY0(x)) #$|PF|= |p_y-y_0|+p/2​</u>$



###### Conic Axis

x:Oval;    Length(LongerAxis(x)) = 2*ParameterA(x) #长轴=2a

x:Oval;    Length(ShorterAxis(x)) = 2*ParameterB(x) #短轴=2b

x:Hyperbola;   Length(RealAxis(x)) = 2*ParameterA(x) #实轴=2a

x:Hyperbola;   Length(VirtualAxis(x)) = 2*ParameterB(x) #虚轴=2b



#### Line (12)

L:Line, LineSegment;    Negation(AngleValue(AngleOfInclination(L)) = ==ApplyUnit==(pi/2, radian))  -> Tan(AngleOfInclination(L))=Slope(L) #直线/线段的倾斜角->直线/线段的斜率的反正切函数

L:Line, LineSegment, yAxis: Axis ; LineEquationExpression(yAxis)=(x=0), ==IntersectionCoordinate==(L,yAxis)=1->   Intercept(L) = YCoordinate(IntersectionCoordinate(L,yAxis))直线/线段的截距->直线/线段与y轴交点的纵坐标值



<u>L:LineSegment;    XCoordinate(MidPoint(L))=(XCoordinate(GetValueByIndex(Endpoint(L),0))+XCoordinate(GetValueByIndex(Endpoint(L),1)))/2, YCoordinate(MidPoint(L))=(YCoordinate(GetValueByIndex(Endpoint(L),0))+YCoordinate(GetValueByIndex(Endpoint(L),1)))/2 线段的中点->线段端点坐标的平均</u>

<u>L:LineSegment;    Length(L) = Distance(GetValueByIndex(Endpoint(L),0), GetValueByIndex(Endpoint(L),1)) #线段的长度->线段端点的距离</u>



L1, L2: Line, LineSegment;    IsParallel(L1, L2)-> ==AngleOfInclination==(L1)=AngleOfInclination(L2), Negation(Intercept(L1)=Intercept(L2))#直线平行->两直线斜率相等,截距不等



L1, L2: Line, LineSegment; IsIntersect(L1,L2) <--> Negation(IsParallel(L1, L2)) #直线相交->直线不平行

L1, L2: Line, LineSegment; Negation(IsIntersect(L1,L2))<--> IsParallel(L1, L2) #直线平行->直线不相交

L1: LineSegment, L2: Line; IsIntersect(L1,L2) -> Negation(IsParallel(L1, L2)) #直线与线段相交->不平行

L1: LineSegment, L2: Line; IsParallel(L1, L2)-> Negation(IsIntersect(L1,L2)) #直线与线段平行->不相交



<u>A,B:Curve; P: Point;    In(P,IntersectionPoint(A,B)) <--> PointOnCurve(P, A), PointOnCurve(P, B) #如果P为A，B的交点，那么P在A,B上</u>



P1, P2, P3: Point;    BetweenTwoPoints(P1, P2, P3) = True, XCoordinate(P2) < XCoordinate(P3), YCoordinate(P2) < YCoordinate(P3) <--> XCoordinate(P1)<XCoordinate(P3), XCoordinate(P2) < XCoordiante(P1), YCoordinate(P1) < YCoordinate(P3), YCoordinate(P2) < YCoordinate(P1) #P1在P2,P3线段之间，当$x_{P_2}<x_{p_3},y_{P_2}<y_{P_3}$时，$x_{p_2}<x_{P_1}<x_{P_3},y_{p_2}<y_{p_1}<y_{p_3}$



P1, P2, P3: Point;    BetweenTwoPoints(P1, P2, P3) = True, XCoordinate(P2) >= XCoordinate(P3), YCoordinate(P2) >= YCoordinate(P3) <--> XCoordinate(P1)>=XCoordinate(P3), XCoordinate(P2) >= XCoordiante(P1), YCoordinate(P1) >= YCoordinate(P3), YCoordinate(P2) >= YCoordinate(P1) #P1在P2,P3之间，当$x_{P_2} \ge x_{p_3},y_{P_2}\ge y_{P_3}$时，$x_{p_2}\ge x_{P_1} \ge x_{P_3},y_{p_2} \ge y_{p_1} \ge y_{p_3}$



#### Equation (2)

<u>x: Oval, Hyperbola, Parabola, Circle,   p: Point;  PointOnCurve(p,x)=True -> SubstitutePoint(p, ConicEquationExpression(x)) #把点代入曲线方程</u>

<u>x: Line,   p: Point;  PointOnCurve(p,x)=True -> SubstitutePoint(p, LineEquationExpression(x)) #把点代入直线方程</u>



###### Generate(3)

<u>x: Oval; GenerateOvalExpression(ParameterA(x),ParameterB(x),Center(x), flag ) = ConicEquationExpression(x)</u>

<u>x: Hyperbola; GenerateHyperbolaExpression(ParameterA(x),ParameterB(x),Center(x), flag) = ConicEquationExpression(x)</u>

<u>x: Line; Negation(AngleValue(AngleOfInclination(L)) = ApplyUnit(pi/2, radian)) -> GenerateLineExpression(Slope(x),Intercept(x)) = LineEquationExpression(x)</u>



#### Triangle(2)

P1, P2, P3: Point; T: ==Triangle==;    T=PointTriangle(P1, P2, P3) -> Apex(T)[0] = P1, Apex(T)[1] = P2, Apex(T)[2]=P3

T: ==Triangle==;    Area(T) = XCoordinate(Apex(T)[0]) * YCoordinate(Apex(T)[1]) - XCoordinate(Apex(T)[0]) * YCoordinate(Apex(T)[2]) + XCoordinate(Apex(T)[1]) * YCoordinate(Apex(T)[2]) - XCoordinate(Apex(T)[1]) * YCoordinate(Apex(T)[0]) + XCoordinate(Apex(T)[2]) * YCoordinate(Apex(T)[0]) - XCoordinate(Apex(T)[1]) * YCoordinate(Apex(T)[1]) #从三角形的三个顶点计算三角形面积 $S=x_1y_2-x_1y_3+x_2y_3-x_2y_1+x_3y_1-x_2y_2$

