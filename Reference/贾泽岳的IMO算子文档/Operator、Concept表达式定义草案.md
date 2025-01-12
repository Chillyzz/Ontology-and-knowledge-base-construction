Operator、Concept表达式定义草案
===

[TOC]

# Individual

## 一些定义的简单写法
```KE
a: Real = 1 // 将声明和等于关系合写
b := 1 //声明，并根据右侧等于的值推导最严格的Concept
```


以下语法的引入，是为了增广目前知识方程的表示能力，
兼容算子、概念的外部定义，并且保持断言语义，
同时，让语言与一般的面向对象语言保持相似，
另外还要兼容模块化

# Concept
## Concept Literal
是旧有语法

## Concept restriction

### 为什么需要？
为知识库设计：
1. 需要静态地存储知识；
2. 很多知识有多层级的结构，例如 半群-群-阿贝尔群，每一个概念都是上一个的子集（或限制）
3. 只用ForAll系列+Concept Literal能表示大部分，但很繁琐
4. 当需要集成更外部的语言时，Concept Literal难以完成，例如确定一个Concept相关的表达式如何翻译到Wolfram语言
5. 按旧有写法会占据名称，如下例中，每处均需要占据`a`的名称
```KE
Positives: Concept
ForAll( a@Positives, In( a, Real ) )
// 说明Positives是Real的限制的旧有语法
ForAll(
    a@Positives,
    floor( a ) = Max( {
        t: PositiveInteger,
        t < a
    } )
)
// 展开算子绑定
```

### syntax
使用restirctionOf（或简写`<:`）定义

Syntax:
```BNF
<identifier> restrictionOf <identifier> {
    // 此block中的`this`代指定义的Concept的代表元
    <relationships>
}
```

```KE
Positives <: Real { // 表示Positives是一个Concept，且是Real的子集
    this > 0,
    // 以上定义一个ForAll断言
    // this指Positives的代表元
    // 表示Positives的任意元素均大于0
    
    sqrt( this ): Positives 
        = Wolfram`Sqrt[this]`,
    // 以上定义绑定算子
    // 表示sqrt( a: Positives )的返回值是Positives
    // 且可以被表示为Wolfram表达式；
    // Wolfram被称为handle语言，
    // 后续需要对每一个handle语言，定义接口（即传递的this的形式）
    // 有此定义后，声明a: Positives即可使用sqrt(a)
    
    floor( this ): PositiveInteger
        = Max( {
            a: PositiveInteger,
            a < this
        } ), // 允许大括号最后冗余的逗号
    // 以上定义绑定纯函数
    // 纯函数是特殊的算子，它只展开为断言逻辑表达式，而不包含handle语言的调用
    
    add( this, that: Positives ): Positives
        = this + that,
        // 不止使用自身的函数绑定
} // 这样就定义了一个Concept，以及与之关联的算子

a: Positives // 定义一个Positives
sqrt( a ) > 2 // 一个断言
floor: PositiveInteger // 全局地定义了一个叫floor的PositiveInteger
// 此后如果写floor(a)则名字会冲突，以下有名称解析规则
Positives::floor( a ) = 4 // 使用::表示Positives绑定的名字
```


# Operator

## 纯函数
只展开为断言逻辑表达式（而不会调用外部handle）的算子称为纯函数。

使用`->`定义纯函数（`=>`已经被用于定义数学函数了）。
:::info
纯函数属于的Concept写法还没想好，可能需要讨论；
但是肯定是可以自动推导地写的
:::

```KE
floor := // 前述自动推导类型的语法
    ( a: Positives ) -> // 此处括号包裹参数列表
    // 或许可以不标注类型，即只写(a) -> ... ， 但总之要求以下表达式对于传入的a合法
        Max( {
            t: PositiveInteger,
            t < a
        } )

a: Positives
floor( a ) = 2 // 给出一个断言
```

## 描述函数
描述函数根据输入，构建一个individual并且给出这个individual的一些assertion。当证明完成时，解题的Scope中描述函数构建的individual应当可以被唯一确定，或已经被分类讨论/归纳了。

使用`:>`定义描述函数，后面跟一个块，块内给出构造的对象的关系，用`this`指代它。

```KE
Min := ( c: Concept ) :> {
    ForAll( that@c, this <= that )
}

InCenter := ( G: Triangle ) :> {
    { A, B, C } := VertexesOf( G ), // A, B, C是G的三个顶点
    distance( A, this ) = distance( B, this ),
    distance( B, this ) = distance( C, this ),
    distance( C, this ) = distance( A, this ),
}
```


可以看到，我们的算子表达式和一般面向对象语言有一定的对偶关系。纯函数对应于函数，描述函数对应于构造函数/工厂函数。

# 模块化
每个名字会被默认地导出

导入时使用`with`块

```KE
// 知识库中, base.ke文件
Positives <: Real {
    this > 0,
    sqrt( this ): Positives 
        = Wolfram`Sqrt[this]`,
    floor( this ): PositiveInteger
        = Max( {
            a: PositiveInteger,
            a < this
        } ),
    add( this, that: Positives ): Positives
        = this + that,
}

// 表示题目时，index.miant文件
Fact List
with { Positives as Number } from "base" {
    a: Number,
    a < 0 // 能推导出矛盾
}
b: PositiveInteger
b > a // with将此块视为Concept Literal，并采用默认导出，因此a的名字在Global Scope中
// 也可以不使用块，直接
with { Positives as Number } from "base"
// 此处以下具有Number的名字
```

## 名称解析规则
解析顺序： Scope Chain中的名字 > Scope Chain中定义的绑定 > 模块以外，被隐式导入的名字



3.13修改
===

1. 声明简写和推导

   声明简写不变

   ```miant
   a: Real = 1
   ```

   推导规则改为：内建类型
   **组会讨论**： 暂时不做推导

2. 映射类型（概念）

   映射的类型直接由输入和输出的类型表示（借用旧的数学函数，`=>`运算符写法）

   ```miant
   ( Real, Real ) => Real
   ```

3. 语言内的纯函数定义

   ```miant
   floor: ( Positive( Real ) ) => PositiveInteger =
   	( a: Positive( Real ) ) ->
   		Max( {
   			t: Positive( Integer ),
   			t < a
   		} )
   ```

4. 提取一些性质算子

   ```miant
   Positive: ( Concept ) => Concept =
       ( c: Concept ) ->
           c_positive <: c {
               this > 0
           }
   ```
:::info
下一阶段：
在JavaScript，python, mathematica等语言中完整地定义接口
:::















