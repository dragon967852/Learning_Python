# 函數
# 基本函數
def sum(a, b) :
  print(a + b)
def add(a, b) :
  return a + b
sum(5, 6)
print(add(5, 5))
# 變量作用域
num1 = 100
list = [1, 2, 3, 4, 5]
def f() :
  global num1# 不可變數據類型，納入引用要加global，list則不用
  print(list, num1)
f()
