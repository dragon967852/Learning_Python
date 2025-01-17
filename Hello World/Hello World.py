# print
year = 2025
month = 1
day = 10
week = "Monday"
weather = "Sun"
temp = 20.5
print("Hello World", year, sep="===", end="\t")# sep中間區隔方式，end結尾方式
print("Next Line")
print("Today is %d year %02d month %02d day | week %s | weather %s | temperature %.2f" %(year, month, day, week, weather, temp))

# input()
print("Enter your age : ")
age = input()
print(type(age))# 查看type
age = int(age)# 類型轉換
print("your birthday year is ", year - age)

# 變量
# 不能以數字為開頭，不能與關鍵字重名
# 沒有專門的常量類型，一般約定使用大寫表示常量
PI = 3.1415926

# 數據類型
# 整數、浮點數、複數(3.14j)、布林、字串
# 列表[1, 'a', 2.3]
# 組 (1, 'a', 2.3)相較於列表，這是不可變的
# 集合 {1, 2, 3}
# 字典 {'name' : 'John', 'age' : '30'} 鍵值對的集合
s1 = "Hello"
print(s1 * 3)

# String
s = "hello world"
print(s[-1])
# 變量名[起始索引:結束索引+1:步數] # 步數若唯1，可以省略不寫
print(s[0:6:2])
print(s[::2])
print(s[::-2])# 反轉


# string to 進制
s1 = "1a"
print(int(s1, 16))