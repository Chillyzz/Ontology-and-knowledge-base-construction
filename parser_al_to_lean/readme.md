在ANTLR4路径下，先在vscode终端用下列命令分别生成对应的Lexer.py、Listener.py、Parser.py以及Visitor.py文件：

java -jar .\antlr-4.13.2-complete.jar -Dlanguage=Python3 AssertionalLogic.g4

java -jar .\antlr-4.13.2-complete.jar -Dlanguage=Python3 -visitor AssertionalLogic.g4

