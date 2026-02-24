Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
for i in range (1,11):
    print(i)

    
1
2
3
4
5
6
7
8
9
10

 
for  i in range (1,15):
    if i%2==0:
        print(i)

        
2
4
6
8
10
12
14

for i in range(1,16):
    if i%2!=0
    
SyntaxError: expected ':'
KeyboardInterrupt
for i in range(1,16):
    if i%2!=0:
        printi(i)

        
Traceback (most recent call last):
  File "<pyshell#13>", line 3, in <module>
    printi(i)
NameError: name 'printi' is not defined. Did you mean: 'print'?
for i in range(1,16):
    if i%2!=0:
        print(i)

        
1
3
5
7
9
11
13
15


for i in range(1,11):
    print("5*",i,"=",5*i)

    
5* 1 = 5
5* 2 = 10
5* 3 = 15
5* 4 = 20
5* 5 = 25
5* 6 = 30
5* 7 = 35
5* 8 = 40
5* 9 = 45
5* 10 = 50
>>> 
>>> name="atmiya"
>>> print("letter")
letter
>>> 
>>> name="atmiya"
... print("letter")
SyntaxError: multiple statements found while compiling a single statement
>>> name("atmiya")
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    name("atmiya")
TypeError: 'str' object is not callable
>>> for letter in name:
...     print("letter")
... 
...     
letter
letter
letter
letter
letter
letter
>>> 
>>> for i in range(1,6):
...     total=total+1
...     print("sum is:",total)
... 
...     
Traceback (most recent call last):
  File "<pyshell#35>", line 2, in <module>
    total=total+1
NameError: name 'total' is not defined
>>> sum of number from 1 to 5
SyntaxError: invalid syntax
>>> total=0
>>> for i in range(1,6):
...     total=total 1+i
...     
SyntaxError: invalid syntax
>>> for i in range(1,6):
...     total=total+1
...     print("sum is :",total)
... 
...     
sum is : 1
sum is : 2
sum is : 3
sum is : 4
sum is : 5
>>> 
>>> print list element
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
>>> number=[10,20,30,40]
>>> for n in number:
...     print(n)
... 
...     
10
20
30
40
