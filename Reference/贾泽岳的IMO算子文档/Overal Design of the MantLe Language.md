# Overal Design of the MantLe Language
## Introduction

Automatic mathematical problem solving has always been a critical issue in the field of artificial intelligence as it's a necessary path towards enhancing AI capabilities. Only when AI can independently provide reliable and trustworthy answers to mathematical problems can it be considered to have reasoning abilities. Meanwhile, automatic mathematical problem solving requires AI to have a series of other capabilities, including natural language processing, knowledge representation and modeling, and autonomous learning. However, previous models mainly focused on simple application problems: they read the problem, processed the semantics, and guessed an expression that could provide the answer. Many works have adopted the method of neural networks and expected it to cover all the induction works, which consequently introduced noise into the data, and can be very destructive for a symbol system that is extremely sensitive to input. In addition, neural network methods require a large amount of data, and there is too little high-quality, complex mathematical problem data for these tasks, which is also the reason that limits the further progress of neural network methods in mathematical problem solving.

Moreover, in terms of knowledge representation, previous research focused on extracting knowledge from problems and outputting it in a given form, which is insufficient for problem solving. The imperfection of knowledge representation methods and the gap between natural language and machine language resulted in this deficiency. Recent research on assertional logic allows us to express knowledge in a way that is both close to natural language and friendly to machines, bridging this gap and closely combining the understanding system and the automatic reasoning system.

The rapid development of recent large language models has grabbed great attention. On the one hand, the scale of large language models has been unprecedentedly enhanced. On the other hand, they still show many deficiencies, especially in mathematics: they may make calculation errors or erroneously reason or commit fallacies. Although some studies have enabled them to call external tools and plugins such as Mathematica to assist in mathematical calculation and proof, these methods still require the language model to perform logical reasoning tasks, generate the final expressions to be calculated, and then hand them over to these plugins. The correctness of such calculation expressions is still hard to verify. In addition, GPT's answers to mathematical problems are often very similar to answers that can be retrieved online, making us doubt whether GPT has the ability to solve mathematical problems independently or if it merely remembers these problems and gives answers from memory. A significant problem encountered by the mathematical community recently is that mathematicians often write complex and lengthy papers for important issues, which are hard to verify. These deficiencies of language models now severely limit their application in mathematical research.

To solve these problems, in this paper, we propose a solution that can perform mathematical reasoning using rules and methods within the IMO range, solve mathematical induction and sequence problems, and provide reliable and trustworthy proofs and calculation processes. We extended a formal language based on assertional logic (hereinafter referred to as MantLe), then used some methods to translate mathematical problems into this language (we mainly adopted manual annotation, the construction of semantic understanding systems, and large language model prompt word engineering); subsequently, we constructed a rule-based reasoning system that can use mathematical methods (MiSaL) that receives MantLe and uses them for reasoning. MiSaL's reasoning is reliable because it is entirely based on rules and methods, making every step reliable, and thus their combinations are reliable.

In summary, MantLe is a knowledge equation form representation of knowledge. MiSaL receives MantLe transformed from the problem stem, transforms the knowledge equation in it into memory in a structured way, and abstracts it into the relationship between three levels of objects: Individual - operator - assertion. Subsequently, the system derives new relationships from these relationships between objects according to the rules. At the same time, the system will also try to decompose the problem according to some inherent mathematical methods, thereby reducing the complexity of each step of problem solving.

When the value required by the problem is deduced, or the proposition required by the problem is deduced, the task of MiSaL is completed.

MantLe generally includes three parts: a fact list, a query list, and a reasoning process. The fact list and the query list are generated from the problem, and any first n lines of the reasoning process represent the status of MiSaL at a certain moment.

## Related Works

## MantLe Language Design

MantLe documents use '.ant' as the suffix, and the '.ant' documents are defined as follows:

```BNF
<Document>                ::= <Fact List><Query List><Reasoning Process>
<Fact List>               ::= Fact List<eos><assertions>|""
<Query List>              ::= Query List<eos><queries>|""
<Reasoning Process>       ::= Global Scope<sentences>
<assertions>              ::= <assertions><assertion>|""
<queries>                 ::= <queries><eos><query>|""
<assertion>               ::= <expression><eos>
<query>                   ::= <expression><eos>|Proof(<expression>)<eos>
<sentences>               ::= <sentences><sentence>|
                        <sentences><Scope><sentences>|""
<sentence>                ::= <sentence index>"|"<body>"||"<sentence indexes><base><eos>
<body>                    ::= <expression>|<declaration>
<declaration>             ::= <variable>: <concept>
<base>                    ::= Rule: <Rule>|
                        Method: <Method>
<sentence indexes>        ::= <sentence indexes>,<sentence index>|<sentence index>
<expression>              ::= <literal>|<operator>(<arguments>)|<arithmetic expression>
<arguments>               ::= <arguments>,<expression>|<expression>
<arithmetic expression>   ::= <expression><binary operator><expression>|
                        <monocular operator><expression>
<literal>                 ::= <value literal>|<variable literal>
<variable literal>        ::= <variable>|<concept literal>|<concept>|{<elements>}
<concept literal>         ::= <export tuple>@<concept literal>|
                        {<Scope in concept>}
<Scope>                   ::= "\"<Scope index><eos><sentences with indent>
<Scope in concept>        ::= <Scope in concept>,<body>
<eos><Rule><Method><operator><variable><concept><binary operator><monocular operator> are defined externally
```

In MiSaL, \<eos\> is defined as a newline character, and Rule, Method, operator, variable, concept, binary operator, monocular operator are given in Appendix 1. We do not care about the existence of spaces as long as they do not cause morpheme adhesion.

### Interpretation of MantLe Semantics by Human and MiSaL

As outlined in Chapter 3, we desired MantLe to align closely with both natural language and machine states during its design phase. In this chapter, we elucidate the correlation between the syntax of MantLe and the natural language expressions of mathematical problems, as well as the MiSaL states they signify.

#### Individuals, Operators, and Concepts

The mathematical domain's syntactic structure is inherited from assertive logic and constitutes individuals, operators, and concepts. 

In mathematics, the function of a concept is akin to a set, the role of an operator is analogous to a mapping between sets, and an individual represents known and unknown quantities. A crucial observation in the field of IMO automatic problem solving is that any concept itself is an individual, and as a mapping, the operator can also be incorporated into the individual. In this study, we pioneered the modeling of the use of mathematical methods by the reasoning engine and the intermediate language, and implemented them using induction as an example.

In MantLe, the individuals we utilize are represented by literals. Known quantities without names are represented by value literals, known sets without names are represented by concept literals, and named objects are represented by built-in variables and concepts. The complete list of individuals, operators, and concepts involved can be found in Appendix 1.

#### Assertions

Assertions, also inherited from assertive logic, represent propositions. In basic assertive logic, an assertion must be written in the form of an equation $a=b$. We have expanded this by viewing $=$ as an operator and trivially equating any assertion $a$ with $a=true$, thus writing $a=true$ directly as $a$ in our representation. This allows us to use operators of the following form directly as assertions:

$$
ForAll(\ Concept,\ Statement\ )
$$

In addition, the declaration of variables is also conducted via assertions. For a `<declaration>`, i.e., `<variable>: <concept>`, it signifies the existence of an object named `<variable>` of type `<concept>`.

#### Scope

+ Scope

  Scope is a specific knowledge structure defined in MantLe. Essentially, for a Scope $\langle S\rangle$, it records two types of information: the variable list V and the assertion list A. Such a Scope can be written as $\langle S| V, A\rangle$.

  A Scope can derive SubScopes, with each SubScope inheriting the information of V and A from its ParentScope. We refer to this process as Scope Chaining, through which all Scopes form a tree, termed the Scope Tree.

+ Macro Scope

  We use Macro Scope to represent the process of problem proof. A Macro Scope records two additional types of information: Fact List and Query. We merge V and A into Current State, written as $\langle S | F, Q, C \rangle$. Here, $F$ and $C$ are arrays formed by assertions, and Q is an Assertion. The semantics of Macro Scope is: $C$ can be deduced from $F$. We can note that for $\langle S| F, Q, C\rangle = \langle S| V, A\rangle$, we have $F\subseteq C\subseteq A$. In Macro Scope, V can be implicitly defined by F and omitted.

  In MantLe, Macro Scope will always be written explicitly.

+ Micro Scope

  Micro Scope refers to the scope of variables. A variable declaration will add the information of this variable to the smallest Micro Scope that contains it. In MantLe, there are three types of Micro Scopes:

  + Every Macro Scope is also a Micro Scope;
  + Each Operator implicitly introduces a Micro Scope, all of the operator's parameters contained in this Micro Scope;
  + Each Concept Literal explicitly introduces a Micro Scope, which describes the elements of the Concept.

  Generally, every Micro Scope only contains the variables directly declared in itself, but there is an exception, which is called Concept Exports.

+ Concept Exports

  Our most basic Concept Literal looks like `{ a: Integer, a >= 1 }`, which defines a set, similar to $\{a\in \mathbb{N}: a \geq 1\}$. We notice that, syntactically, the variable 'a' is only defined within the confines of the curly braces, causing many issues such as our inability to reference this Concept Literal's representative element within our `ForAll` assertion.

  Our expression `ForAll( { a: Integer, a >= 1 }, a^2 >= 1 )` in fact contains an implicit Concept Export. The explicit form of this is prefixed by an `<export tuple>`, such as `(b=2*a)@{ a: Integer, a >= 1 }`. During the Concept Export process, the `@` symbol is preceded by an export tuple, which consists of a series of equalities. The left-hand side defines the variable, while the right-hand side comprises expressions contained within the Concept Literal's Micro Scope. As a result, it can reference the variables within the Concept Literal, while the variables on the left-hand side are defined within the outermost Micro Scope. By using Concept Exports, we can refer to a representative element defined within one Concept argument in other parameters within the operator.

#### Individuals, Operators and Concepts
The concepts of individuals, operators, and concepts are derived from predicate logic and form the syntactic structure in the field of mathematics. They represent known and unknown quantities, mappings between sets, and sets, respectively. In MantLe, literals are used to represent individuals. Known quantities without names are represented by value literals, known sets without names are represented by concept literals, and named objects are represented by built-in variables and concepts.

#### Assertions
Assertions, representing propositions, are also derived from predicate logic. In the basic predicate logic, assertions must be written in the form of equations $a=b$. MantLe has expanded this, viewing $=$ as an operator and equating any assertion $a$ with $a=true$. This allows operators of the following form to be used directly as assertions:

$$
ForAll(\ Concept,\ Statement\ )
$$

Variable declarations are also made through assertions. A declaration of `<variable>: <concept>` represents the existence of an object named `<variable>` of type `<concept>`.

#### Scope
The concept of Scope in MantLe, denoting a special knowledge structure, is introduced. A Scope records two types of information: a list of variables V and a list of assertions A. It can be written as $\langle S| V, A\rangle$. Scope can be further divided into Macro Scope and Micro Scope, each with its own specific semantics.

The Macro Scope represents the proof process of a problem, while the Micro Scope represents the scope of variables. 

The work on the MiSaL model embodies these concepts from MantLe. The internal structure of MiSaL's inference engine creates the structure of the Scope Tree and contains common methods for inductive sequence problems in the scope of IMO. When MiSaL is working, it reads the MantLe representing the problem, and uses its Fact List and Query List to derive the Global Scope from the Knowledge Scope. Inference in MiSaL is carried out by finding embedding mappings between Scopes.

#### Scope Embedding
For a mapping $f:\langle S_1|V_1,A_1\rangle\to\langle S_2|V_2,A_2\rangle$, if it satisfies the conditions below:
$$
\begin{align*}
f:& & \langle S_1| V_1, A_1 \rangle &\to \langle S_2| V_2, A_2\rangle\\
& & v \in V_1 &\mapsto f(v)\in V_2\\
& & a( v_1, v_2, ..., v_n ) \in A_1 &\mapsto a(f(v_1), f(v_2), ..., f(v_n) )\in A_2
\end{align*}
$$
 then $f$ is called an embedding from $S_1$ to $S_2$ and is denoted as $f:S_1\hookrightarrow S_2$. 

Furthermore, if it is an embedding from Macro Scopes $\langle S_1|F_1,Q(v_1,v_2,...,v_n)\rangle $ to $\langle S_2|F_2,Q(u_1,u_2,...,u_n)\rangle$, then it is called a q-embedding and denoted as $f:S_1\triangleleft S_2$.

#### Method
A new concept, method, is introduced in this work, which is regarded as the decomposition of propositions in mathematics. By applying methods, complex propositions can be transformed into combinations of simpler ones.

We denote a method in the form below:
$$
\left\langle M|
    {\small\left\langle S_M|F_M,Q_M \right\rangle}|
    \{(F_i,Q_i)\}_{1\leq i \leq n}
\right\rangle
$$
When a method M is applied on a Scope S, it functions as follows:
$$
f:S_M \triangleleft S \Rightarrow
\langle S| F, Q\rangle \stackrel{M}\mapsto \oplus_{i=1}^n\langle S_i|F\cup F_i,Q_i\rangle
$$

#### Rule

Rules in MantLe and MiSaL are used to represent theorems, axioms, and definitions in mathematics. They form the basis of our reasoning and proof. The form and meaning of the Rule are similar to the ForAll operator.

We denote a Rule in the form below:
$$
\langle R| S_R, A_R\rangle \Leftrightarrow ForAll( S, A )
$$
When a Rule R is applied on a Scope $S$, it functions as follows:
$$
f: S_R \hookrightarrow S \Rightarrow
\langle S | F, Q, C \rangle \stackrel{R} \mapsto \langle S | F, Q, C \cup f(A_R)\rangle
$$
