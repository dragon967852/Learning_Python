# 判斷分支
# if
age = int(input("Please enter your age : \n"))
if age <= 18 and age > 12:
    print("go out")# 要注意縮排
elif age <=12 and age >=0 :
    print("stay in home")
else :
    print("you can go out")
# match
x = 4
match x :
    case 1 :
        print(1)
    case 2 :
        print(2)
    case _ :# default 
        print("other")

# 循環
n = 1
result = 0
# 高斯 1+..+100
while n < 101 :
  result += n
  n += 1
print(result)
n1 = 1
result1 = 0
for n1 in range(101) :
  result1 += n1
print(result1)
my_dict = {'a': 1, 'b': 2, 'c': 3}
for key, value in my_dict.items(): # 字典的循環
    print(f"Key: {key}, Value: {value}")


# break
while True :
  name = input("Please enter your name :")
  if name == "Jen" :
    print("welcome sir")
    break
  else :
    print("no welcome")
# continue
for i in range(10) :
  if i == 2 :
    continue
  print(i)
