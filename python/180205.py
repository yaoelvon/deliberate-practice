# coding: utf-8
"""
闭合/工厂函数：一个可以记住嵌套作用域的变量值的函数，尽管这个作用域已经不存在了。

lambda： 是一个表达式，匿名函数，将会生成后面调用的一个新的函数，与def语句很类似。由于它是一个表达式，
所以可以用在def语句不能使用的地方，例如，在一个列表或字典的常量之中？？what？
"""

def func():
	x = 4
	action = (lambda n, x=x: x ** n)
	return action

x = func()
print x(2)