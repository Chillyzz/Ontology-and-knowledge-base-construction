- 共68operator,在更新
# Basic Geometry Axion 基础的几何公理
## Axiom of Connection 关联公理
### Connection 关联
1. Connection : show that point is on a line/plane and so on / or set inclution
   Connection : ({x: ConnectionType}, {y: ConnectionType}) -> Boolean

2. Is_Point_On : show point is on some set
   Is_Point_On : ({x: Point}, {y: Set}) -> Boolean

3. Line on Plane : show Line is on some plane
   Line_On_Plane : ({x: Line}, {y: Plane}) -> Boolean

### Point and Line 点与线

1. Intersected : two geometry sets are intersected
   Intersected : ({x: Set}, {y: Set}) -> Boolean

2. Line Intersected : two lines are intersected
   Line_Intersected : ({x: Line}, {y: Line}) -> Boolean

3. Intersection Point : The intersection point of two lines is the unique point where the two lines meet in the plane.
   Intersection_Point : ({x: Line}, {y: Line}) -> Point

4. Points on the same line : there exist some line that Three or more point is on it. (? 真的需要吗 可以用逻辑运算代替)
   Points on the same line : (Point, Point, Point, ...) -> Bool

5. Lines share a common point : there exist some point that Three or more line is containing it. (? 真的需要吗 可以用逻辑运算代替)
   Lines share a common point : (Line, Line, Line, ...) -> Bool

### Line and Plane 线与面

1. Plane_Intersected : two planes are intersected
   Plane_Intersected : ({x: Plane}, {y: Plane}) -> Boolean

2. Intersection Line : the intersection line of two planes
   Get_Intersection_Line : ({x: Plane}, {y: Plane}) -> Line

## Axiom of Order 顺序公理

1. In the Upper of a point : the "greater than" relation on ordered line. ( 更规范些 )
   In the Upper of a point : (Ordered Line, Point, Point) -> Bool

## Axiom of Congruence 合同公理

### Congruence Relation 合同关系

1. Congruence : the congruence relation of geometry items.
   Congruence : ({-,-}, {-,-}) -> Bool

2. Congruence of Line Segment : the two line segments' "length" is the same.
   Congruence of Line : (Line Segment, Line Segment) -> Bool

3. Congruence of Angle : the two angles' "degree" is the same.
   Congruence of Angle : (Angle, Angle) -> Bool

4. Congruence of Triangle : (Triangle, Triangle) -> Bool

### the movement of Maintaining Congruence Relation 保合同的移动

1. the movement of Line Segment : the Line Segment begin at a point on an Ordered Line, with the same "length" of the given one.
   the movement of Line Segment : (Point, Ordered Line, Line Sqgment) -> Line Segment

2. the movement of Angle : the Angle with given edge , and with the same "degree" of the given angle.
   the movement of Angle : (Ray, Angle) -> Angle

## measure 测度

1. length of line segment : (Line Segment) -> (0, +∞)
   Get_Lenght: ({x: LineSegment}) -> PositiveNumber

2. area of : ({-,-}) -> [0, +∞)
   Get_Area: ({x: 2DGeometryObject}) -> PositiveNumber

3. volume of : ({-,-}) -> [0, +∞)
   Get_Volume: ({x: 3DGeometryObject}) -> PositiveNumber

### Angle 角度
1. the degree of angle : (Angle) -> [0, 180°]
   Get_Angle_Degree: ({x: Angle}) -> PositiveNumber

2. Is Acute Angle : An angle less than 90°.
   Is_Acute_Angle : ({x: Angle}) -> Boolean

3. Is Right Angle : An angle exactly equal to 90°.
   Is_Right_Angle : ({x: Angle}) -> Boolean

4. Is Obtuse Angle: An angle greater than 90° but less than 180°.
   Is_Obtuse_Angle : ({x: Angle}) -> Boolean
   
5. Is Straight Angle : An angle equal to 180°.
   Is_Straight_Angle : ({x: Angle}) -> Boolean

## 平行公理 

1. Is Paralleled with : the parallel relationship of line, line segment, ray, vector, plane...
   Is Paralleled with : ({-,-}, {-,-}) -> Bool

2. Lines Is Paralleled : the parallel relationship of line
   Is Paralleled with : (Line, Line) -> Bool

3. Vectors Is Paralleled : the parallel relationship of Vectors
   Is Paralleled with : (Vector, Vector) -> Bool

4. Line Is Paealleled with Plane : the parallel relationship between Line and Plane.
   Line Is Paealleled with Plane : (Line, Plane) -> Bool

5. Planes Is Paealleled: the parallel relationship of Planes.
   Line Is Paealleled with Plane : (Plane, Plane) -> Bool

# Construction of Geometric Shapes 几何图形的构建
## Line and so on 线类

1. Line Determined by Two Points : The line determined by two points
   Line Determined by Two Points : (Point,Point) -> Line 
   Build_Line: ({x: Point}, {y: Point}) -> Line

2. Line Segment Determined by Two Points : The Line Segment determined by two points
   Line Segment Determined by Two Points : (Point,Point) -> Line Segment
   Build_LineSegment: ({x: Point}, {y: Point}) -> LineSegment

3. Ray Determined by Two Points : The Ray determined from the begining point to other point.
   Ray Determined by Two Points : (Point,Point) -> Ray
   Build_Ray: ({x: Point}, {y: Point}) -> Ray

4. Vector Determined by Two Points : The Vector determined from the begining point to the ending point.
   Vector Determined by Two Points : (Point,Point) -> Vector
   Build_Vector: ({x: Point}, {y: Point}) -> Vector

5. Ordered Line Determined by Two Points : The Ordered Line from the begining point to the ending point.
   Ordered Line Determined by Two Points : (Point,Point) -> Ordered Line
   Build_OrderedLine: ({x: Point}, {y: Point}) -> OrderedLine

## Plane figures 平面图形
1. Triangle Determined by Three Points in general positions : (Point, Point, Point, Bool) -> Triangle

2. Plane Determined by Three Points in general positions : (Point, Point, Point, Bool) -> Plane

3. Quadrilateral Determined by Four Points : (Point, Point, Point, Point) -> Quadrilateral

4. Polygon Determined by Points : (Point, Point, Point, ...) -> Polygon

5. Angle Determined by Three Points : (Point, Point, Point) -> Angle

6. Vertical Ordered line Determined by Line and outer point : (Line, Point, Bool) -> Ordered Line

7. vertical with : ({-,-}, {-,-}) -> Bool

8. Vertical line Determined by Line and point on Plane : (Line, Point, Bool) -> Line

9. Paralleled line Determined by Line and outer point : (Line, Point, Bool) -> Line

### Circle  圆
1. Circle Determined by center and Point : (Point, Point) -> Circle

2. Circle Determined by center and Radius : (Point, [0, +∞)) -> Circle

3. center of Circle : (Circle) -> Point

4. Radius of Circle : (Circle) -> [0, +∞)

5. Diameter of Circle : (Circle) -> [0, +∞)

6. some Point on circle : (Circle) -> Point

7. Circular Inferior Arc : (Point, Point, Bool) -> Set

8. In the middle of on circle : show a point on circle is in the middle of another two points on circle
   In the middle of on circle : (Point, Point, Point) -> Bool

9. Circular Arc Determined by Three point : when a point is in the middle of two points, then they determine an  circular arc.
   Circular Arc Determined by Three point : (Point, Point, Point, Bool) -> Set

# Rectangular Plane Coordinate System 平面直角坐标系

1. Origin : The point where the axes intersect is called the **origin**, denoted as \( (0, 0) \).
   Origin : (Coordinate System) -> Point

2. x-axis : (Rectangular Plane Coordinate System) -> Ordered Line

3. y-axis : (Rectangular Plane Coordinate System) -> Ordered Line

4. Quadrants : The plane is divided into four regions (quadrants) by the axes.
   Quadrants : (Rectangular Plane Coordinate System, Natural Number [1, 4]) -> Set

5. x-ordinate : (Rectangular Plane Coordinate System, Point) -> Real Number

6. y-ordinate : (Rectangular Plane Coordinate System, Point) -> Real Number

7. equation of : (Rectangular Plane Coordinate System, {-,-}) -> Function

## The equation of a line 直线方程 (省略了背景参量:Rectangular Plane Coordinate System)

1. The standard equation of line : ax + by + c = 0
   The standard equation of line : (Line) -> Function

2. The inclination angle of Line : the angle between line and the x-axis's positive part.
   The inclination angle of Line : (Line) -> [0,180°)

3. The Slope of Line : tangent of (The inclination angle of Line)
   The Slope of Line : (Line) -> Real Number with infinite

4. The Intercept of Line with y-axis : the y-ordinate of the intercept point of line and y-axis if exist
   The Intercept of Line with y-axis : (Line, Bool) -> Real Number

5. The Intercept of Line with x-axis : the x-ordinate of the intercept point of line and x-axis if exist
   The Intercept of Line with x-axis : (Line, Bool) -> Real Number

6. Slope-intercept equation of a line : y - kx - b = 0
   Slope-intercept equation of a line : (Line, Bool) -> Function

## The equation of a circle 圆方程 (省略了背景参量:Rectangular Plane Coordinate System)

1. The center-radius of Circle : (x - a)^2 + (y - b)^2 - r^2 = 0
   The center-radius of Circle : (Circle) -> Function

2. The standard equation of circle : x^2 + y^2 + Dx + Ey + F = 0
   The standard equation of circle : (Circle) -> Function





