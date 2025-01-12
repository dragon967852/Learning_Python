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
