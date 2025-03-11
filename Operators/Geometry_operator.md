- 共110operator,在更新
# Basic Geometry Axion 基础的几何公理
## Axiom of Connection 关联公理
### Connection 关联
1. Is_Connected_With : show that point is on a line/plane and so on / or set inclution
   Is_Connected_With : ({-,-},{-,-}) -> Bool

2. Is_Point_On : show point is on some set
   Is_Point_On : (Point, {-,-}) -> Bool

3. Is_Line_On_Plane : show Line is on some plane
   Is_Line_On_Plane : (Line, Plane) -> Bool

### Point and Line 点与线

1. Is_Intersected_With : two geometry sets are intersected
   Is_Intersected_With : ({-,-},{-,-}) -> Bool

2. Is_Line_Intersected : two lines are intersected
   Is_Line_Intersected : (Line, Line) -> Bool

3. Intersection_Point_Of : The intersection point of two lines is the unique point where the two lines meet in the plane.
   Intersection_Point_Of : (Line,Line) -> Point

### Line and Plane 线与面

1. Is_Plane_Intersected : two planes are intersected
   Is_Plane_Intersected : (Plane, Plane) -> Bool

2. Intersection_Line_Of : the intersection line of two planes
   Intersection_Line_Of : (Plane, Plane) -> Line

## Axiom of Order 顺序公理

1. In the Upper of a point : the "greater than" relation on ordered line.
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

2. area of : ({-,-}) -> [0, +∞)

3. volume of : ({-,-}) -> [0, +∞)

4. lenght of : ({-,-}) -> (0, +∞)
   (the sum of the lengths of Polynomial or the perimeter or Circumference of circle is also this one)

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

2. Line Segment Determined by Two Points : The Line Segment determined by two points
   Line Segment Determined by Two Points : (Point,Point) -> Line Segment

3. Ray Determined by Two Points : The Ray determined from the begining point to other point.
   Ray Determined by Two Points : (Point,Point) -> Ray

4. Vector Determined by Two Points : The Vector determined from the begining point to the ending point.
   Vector Determined by Two Points : (Point,Point) -> Vector

5. Ordered Line Determined by Two Points : The Ordered Line from the begining point to the ending point.
   Ordered Line Determined by Two Points : (Point,Point) -> Ordered Line

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

4. Radius Length of Circle : (Circle) -> [0, +∞)

5. Diameter Length of Circle : (Circle) -> [0, +∞)

6. some Point on circle : (Circle) -> Point

7. Radius of Circle : (Circle, Point) -> LineSegment

8. Diameter of Circle : (Circle, Point) -> LineSegment

9. Circular Inferior Arc : (Point, Point, Bool) -> Set

10. In the middle of on circle : show a point on circle is in the middle of another two points on circle
   In the middle of on circle : (Point, Point, Point) -> Bool

11. Circular Arc Determined by Three point : when a point is in the middle of two points, then they determine an  circular arc.
   Circular Arc Determined by Three point : (Point, Point, Point, Bool) -> Set

### AnnularSector 扇环（扇形，半圆，圆环）
1. AnnularSector_Of : the center, the central angle, the inner radius and outer one form an AnnularSector.
   AnnularSector_Of : (Point, [0,360°], [0, +∞), [0, +∞)) -> AnnularSector

### Midpoint, perpendicular bisector, angular bisector 中点，垂直平分线，角平分线
1. Midpoint of Line Segment : (Line Segment) -> Point

2. The nth mth dividing point of Vector : (Vector) -> Point

3. perpendicular bisector of Line Segment : (Line Segment, Plane) -> Line

4. angular bisector : (Angle) -> Ray

5. Centroid of triangle : the point of intersection of its three medians.
   Centroid of triangle : (Triangle) -> Point

6. orthocenter of triangle : the point where the three altitudes of the triangle intersect
   orthocenter of triangle : (Triangle) -> Point


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

# Tangency of a circle 圆与直线,三角形心

1. Line intersect circle : (Line, Circle) -> Bool

2. Line is tangent to circle : (Line, Circle) -> Bool

3. line is separate from a circle : (Line, Circle) -> Bool

4. Incircle of triangle : a circle that is tangent to all three sides of the triangle.
   Incircle of triangle : (Triangle) -> Circle

5. Excircle of triangle : a circle that is tangent to one side of the triangle and the extensions of the other two sides.
   Excircle of triangle : (Triangle, Point) -> Circle

6. circumcircle of triangle : the circle that passes through all three vertices of the triangle.
   circumcircle of triangle : (Triangle) -> Circle

7. incenter of triangle : the point of intersection of the angle bisectors of the triangle。
   incenter of triangle : (Triangle) -> Point

8. Excenter of triangle : center of one of the excircles.
   Excenter of triangle : (Triangle, Point) -> Point

9. Circumcenter of Triangle : the point of intersection of the perpendicular bisectors of the sides of the triangle.
   Circumcenter of Triangle : (Triangle) -> Point

# Translation, Rotation, Symmetry, and Central Symmetry 平移，旋转，对称，中心对称
1. Translation : to move every point of a figure the same distance in the same direction(Determined by a Vector).
   Translation : ({-,-}, Vector) -> {-,-}

2. 2d_Rotation : to turn a figure around a fixed point, known as the center of rotation, by a certain angle.
   2d_Rotation : ({-,-}, Point, [0,360°)) -> {-,-}

3. 3d_Rotation : ({-,-}, Ordered Line, [0,360°)) -> {-,-}

4. 2d_Reflection : flipped across a line (in 2D) or a plane (in 3D), resulting in a mirror image of the original figure.
   2d_Reflection : ({-,-}, Line) -> {-,-}

5. 3d_Reflection : ({-,-}, Plane) -> {-,-}

6. 2d_Central_Symmetry : rotated 180°.
   2d_Central_Symmetry : ({-,-}, Point) -> {-,-}

7. 3d_Central_Symmetry : ({-,-}, Line) -> {-,-}

8. Dilation : Scaling a figure up or down by a specific factor, preserving the shape but changing the size.
   Dilation : ({-,-}, Vector) -> {-,-}

# similarity and homothety 相似与位似
1. Is Similar with : shapes that have the same shape but may differ in size.
   Is Similar with : ({-,-}, {-,-}) -> Bool

2. Is Similar Triangle : (Triangle, Triangle) -> Bool

3. homothety : a figure is moved along a straight line through a fixed point (the center of homothety), with distances multiplied by a constant scale factor(a real number, when negtive, then the figure is of the two sides of the center).
   homothety : ({-,-}, Point, Real Number) -> {-,-}

4. Is_Homothetic_With : ({-,-}, {-,-}, Point) -> Bool

# Internal and External 内部与外部
1. 2d_Internal_Of : the region inside the object(for simple closed curve, the Jordan Curve Theorem give the definition, but for others, the definition is customary, e.g : the Internal of Parabola).
   2d_Internal_Of : ({-,-}) -> Set

2. 3d_Internal_Of : ({-,-}) -> Set

3. 2d_External_Of : ({-,-}) -> Set

4. 3d_External_Of : ({-,-}) -> Set

# distance 距离
1. Distance_Of : the minimial distance of points in the two object.
   Distance_Of : ({-,-}, {-,-}) -> [0, +∞)

# Triangle shape 三角形形状

1. Is_Isosceles_Triangle \\ in Triangle : Two sides are equal, and the angles opposite those sides are equal.
   Is_Isosceles_Triangle : (Triangle) ->Bool

2. Is_Equilateral_Triangle \\ in Isosceles Triangle : All sides are equal, and all angles are 60°.
   Is_Equilateral_Triangle : (Triangle) ->Bool

3. Is_Scalene_Triangle \\ in Triangle : All sides and angles are different.
   Is_Scalene_Triangle : (Triangle) ->Bool

4. Is_Acute_Triangle \\ in Triangle : All angles are less than 90°.
   Is_Acute_Triangle : (Triangle) ->Bool

5. Is_Right_Triangle \\ in Triangle : One angle is exactly 90°.
   Is_Right_Triangle : (Triangle) ->Bool

6. Is_Obtuse_Triangle \\ in Triangle : One angle is greater than 90°.
   Is_Obtuse_Triangle : (Triangle) ->Bool

7. Is_Isosceles_Right_Triangle \\ in Isosceles Triangle, in Right Triangle : A right triangle where the two legs are equal, and the angles are 45° 45° 90°.
   Is_Isosceles_Right_Triangle : (Triangle) ->Bool

# 几何图形的参数
1. Height_Of : the height of triangle, Trapezoid, Prism, Pyramid, Frustum and so on.
   Height_Of : ({-,-}) -> Positive Real Number

2. Base_Length_Of : The base length of a triangle, Parallelogram.
   Base_Length_Of : ({-,-}) -> Positive Real Number

3. Upper_Base_Length_Of : (Trapezoid) -> Positive Real Number

4. Lower_Base_Length_Of : (Trapezoid) -> Positive Real Number

5. Length_Of : The length of rectangle, rectangular prism.
   Length_Of : ({-,-}) -> Positive Real Number

6. Width_Of : The width of rectangle, rectangular prism.
   Width_Of : ({-,-}) -> Positive Real Number

7. Side_Length_Of : (Rhombus) -> Positive Real Number

8. Edge_Length_Of : (Cube) -> Positive Real Number

9. Bottom_Area_Of : the bottom area of Prism, Pyramid, Cylinder, and Cone.
   Bottom_Area_Of : ({-,-}) -> Positive Real Number

