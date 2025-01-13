# Basic Geometry Axion 基础的几何公理
## Axiom of Connection 关联公理
### Connection 关联
1. Connection : show that point is on a line/plane and so on / or set inclution
   Connection : ({-,-},{-,-}) -> Bool

2. Point on : show point is on some set
   Point on : (Point, {-,-}) -> Bool

3. Line on Plane : show Line is on some plane
   Line on Plane : (Line, Plane) -> Bool

### Point and Line 点与线

1. Line Determined by Two Points : The line determined by two points
   Line Determined by Two Points : (Point,Point) -> Line 

3. Intersected : two geometry sets are intersected
   Intersected : ({-,-},{-,-}) -> Bool

3. Line Intersected : two lines are intersected
   Line Intersected : (Line, Line) -> Bool

4. Intersection Point : The intersection point of two lines is the unique point where the two lines meet in the plane.
   Intersection Point : (Line,Line) -> Point

5. Points on the same line : there exist some line that Three or more point is on it.
   Points on the same line : (Point, Point, Point, ...) -> Bool

6. Lines share a common point : there exist some point that Three or more line is containing it.
   Lines share a common point : (Line, Line, Line, ...) -> Bool

### Line and Plane 线与面

1. Plane Intersected : two planes are intersected
   Plane Intersected : (Plane, Plane) -> Bool

2. Intersection Line : the intersection line of two planes
   Intersection Line : (Plane, Plane) -> Line

## Axiom of Order 顺序公理

1. In the Upper of a point : the "greater than" relation on ordered line.
   In the Upper of a point : (Ordered Line, Point, Point) -> Bool

2. Between two point : show the first point on the line is between the following two points / on the line segment of the following two points.
   Between two point : (Line, Point, Point, Point) -> Bool

3. On the Ray of two point : show the first point on the line is on the ray of following two point.
   On the Ray of two point : (Line, Point, Point, Point) -> Bool

4. Line with the order of a ray : the ordered line with the same order of a ray.
   Line with the order of a ray : (Point, Point) -> Ordered Line

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
   the movement of Line Segment : (Point, Ordered Line, Line Sqgment) -> Line Sqgment

2. the movement of Angle : the Angle with given edge , and with the same "degree" of the given angle.
   the movement of Angle : (Ray, Angle) -> Angle

## measure 测度

1. length of line segment : (Line Segment) -> (0, +∞)

2. area of : ({-,-}) -> [0, +∞)

3. volume of : ({-,-}) -> [0, +∞)

### Angle 角度
1. the degree of angle : (Angle) -> [0, 180°]

2. Is Acute Angle : An angle less than 90°.
   Is Acute Angle : (Angle) -> Bool

3. Is Right Angle : An angle exactly equal to 90°.
   Is Right Angle : (Angle) -> Bool

4. Is Obtuse Angle: An angle greater than 90° but less than 180°.
   Is Obtuse Angle : (Angle) -> Bool
   
5. Is Straight Angle : An angle equal to 180°.
   Is Straight Angle : (Angle) -> Bool

## 平行公理

1. 
