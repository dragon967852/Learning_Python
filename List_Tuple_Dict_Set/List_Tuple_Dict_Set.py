# 列表
list1 = [] # 空列表
print(list1)
list2 = [1, 2, 3, True, False, 'Hello']
print(list2)
list3 = list("123465") # 類型轉換 : 把參數轉換為列表
print(list3)
print(list3[1])
list3.append("777")# 列表常用方法 : 變量.方法名()
print(list3)


# Tuple 組 : 相較於列表，元素不能被修改
tuple1 = (1, 2, 3, True, "Hello")
print(tuple1)
tuple2 = () # 空 tuple
print(tuple2)
tuple3 = tuple(list3) # list -> tuple
print(tuple3)
print(tuple3[2])
del tuple3 # 刪除tuple
# tuple1[0] = 123 # 會報錯，不能修改
a = tuple1.count("Hello")# Tuple常用方法 : 變量.方法名()
print(a)# 有幾個函數


# 字典
# 重複的鍵值隊會被覆蓋掉
d = {
  "name" : "Jen", # 鍵值對
  "gender" : False
}
print(d)
d1 = {} # 空字典
print(d1)
d["height"] = 170 # 新增
print(d)
print(d["name"])
del d1 # 刪除鍵值對
for i in d :# 打印字典
  print(i, d[i])


# set 集合
s =set() # 空集合
print(s, type(s))
s = {1, 2, 3, 4, 1, 2}
print(s) # 不能有重複的，會被覆蓋掉
s = set([1, 2, 3, 1])# 轉換 list -> set
print(s)
s = set({1 :'a', 'a' : 2})# 轉換 dict -> set
print(s)
s.remove('a')# set常用方法 : 變量.方法名()
print(s)
