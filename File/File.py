# 文件
# 讀取
f = open("test.txt", mode = 'r', encoding = 'utf-8')# 打開文件，要同層，否則要加路徑
print(f.read())
f.close() # 記得關掉
import os
print(os.getcwd())# 此python的路徑
# 寫入文件
f = open("test.txt", mode = 'w', encoding = "utf-8")# 如果原先檔案有內容會被覆蓋掉
f.write("你好\n")
f.write("你好2\n")
f.close()


# with : 會自動關閉
with open("test.txt", mode = 'r', encoding = "utf-8") as txt_with :
  print(txt_with.read())


# csv
import csv
with open("data.csv", mode = 'r', encoding = "utf-8") as csv_with :
  print(csv_with.read())
with open("data.csv", mode = 'a', encoding = "utf-8") as csv_with :
   csv_writer = csv.writer(csv_with)
   csv_writer.writerow(['tom', 'c', '50'])
