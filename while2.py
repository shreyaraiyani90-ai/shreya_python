Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> i=1
>>> while i<10
SyntaxError: expected ':'
>>> i=1
>>> while i<10:
...     print(i)
...     i=i+1
... 
...     
1
2
3
4
5
6
7
8
9
>>> n=int(input("enter n;"))
enter n;10
>>> i=1
>>> s=0
>>> while i<=n:
...     s=s+i
...     i=i+1
...     print("sum=",s)
... 
...     
sum= 1
sum= 3
sum= 6
sum= 10
sum= 15
sum= 21
sum= 28
sum= 36
sum= 45
sum= 55
>>> num=int(input("enter number:"))
enter number:10
>>> i=1
>>> while i<=10:
...     print(num,"x","i","=",num *i)
...     i=i+1
... 
...     
10 x i = 10
10 x i = 20
10 x i = 30
10 x i = 40
10 x i = 50
10 x i = 60
10 x i = 70
10 x i = 80
10 x i = 90
10 x i = 100
