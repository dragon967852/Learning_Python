import Module # 調用外部library
Module.add(3, 4)
from Module import add # 自module調用add function
add(3, 4)

# 模塊包的使用
# 可以將多個模塊組合再一起，形成一個大的工具庫
# 包裡面要新建名為 : __init__.py，裡面可以寫也可以不寫
# 包裡面就可以放自己撰寫的library
# 引用時 : from 自己的包 import 自己撰寫的.py or import 自己的包，裡面有寫function
# 常見的標準庫 : os, sys, time, random, math
import random
a = random.randint(1, 100)
print(a)

# 更新第三方庫
# cmd > pip install library_name
