Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> x="hellow world"
>>> print("hello world")
hello world
>>> x="20"
>>> print("20")#int
20
>>> x="20.5"
>>> print("20.5")#float
20.5
>>> x="1j"
>>> print("1j")#comple
1j
>>> x='apple","banana","cherry"
SyntaxError: unterminated string literal (detected at line 1)
>>> x=("apple","banana","cherry")
>>> print("apple","banana","cherry")#list
apple banana cherry
>>> x=("apple","banana","cherrry")
>>> print("apple","banan","cherry")
apple banan cherry
>>> x="range
SyntaxError: unterminated string literal (detected at line 1)
>>> x="range"
>>> print"("range")
SyntaxError: unterminated string literal (detected at line 1)
>>> x="range"
>>> print("range")#range
range
>>> x=("name":"johan","age":36)
SyntaxError: invalid syntax
>>> x=("apple","banana","cherry")
>>> print("apple","banana","cherry")#set
apple banana cherry
>>> x="true"
>>> print("true")#bool
true
>>> x="b hellow"
>>> print("b hellow")#bytes
b hellow
