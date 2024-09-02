# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 10:06:32 2024

@author: W1960
"""

name ='tencent'
stock_price = 19.9
stock_code = 672
stock_price_daily_growth_factor = 1.2
growth_days = 7
money = stock_price*stock_price_daily_growth_factor**growth_days
print("公司：%s,股票代码：%s,当前股价：%.2f,每日增长系数:%.2f,经过七天增长后,股价达到了:%.2f" % (name,stock_code,stock_price,stock_price_daily_growth_factor,money))

user_name = input("请输入您的姓名：")
user_type = input("请输入您的账户类型：")
print("您好，%s,您是尊贵的 %s 用户，欢迎您的光临！" % (user_name,user_type))
bool_1=True
print("bool_1的内容是：%s,类型是：%s"%(bool_1,type(bool_1)))

print("欢迎来到黑马儿童游乐场，儿童免费，成人收费。")
age = input('请输入你的年龄：')
age = int(age)
if age >= 18:
    print("您已成年，请补票10元。")
print('祝您游玩愉快！')
print("欢迎来到黑马动物园")
height = int(input("请输入您的身高："))
if height >= 130:
    print("您的身高超出120cm,游玩需要购票10元。")
else:
    print("您的身高未超出120cm，可以免费游玩。")
print("祝您游玩愉快")


num = 1
if int(input("请输入第一次猜想的数字：") == num):
    print("恭喜你，猜对啦！")
elif int(input("不对，再猜一次：")) == num:
    print("恭喜你，猜对啦！")
elif int(input("不对，再猜最后一次："))==num:
    print("恭喜你，猜对啦！")
else:
    print("sorry,全部都猜错了，我想的是：10")
    
    
    
import random
num = random.randint(1, 10)
caice = int(input("请输入您的猜测："))
if caice == num :
    
    print("恭喜你，猜对了！")

elif caice != num :
    if caice > num :        
        print("猜大了")
        caice = int(input("请再猜一次："))
        if caice > num :
            print("猜大了")
            caice = int(input("请再猜一次："))
            if caice != num :
                print("sorry, 您猜错了")
            else:
                print("恭喜您，猜对了")
        elif caice < num :
            print("猜小了")
            caice = int(input("请再猜一次："))
            if caice != num :
                print("sorry, 您猜错了")
            else:
                print("恭喜您，猜对了")
            
            
    if caice < num :
        print("猜小了")
        caice = int(input("请再猜一次："))
        if caice > num :
            print("猜大了")
            caice = int(input("请再猜一次："))
            if caice != num :
                print("sorry, 您猜错了")
            else:
                print("恭喜您，猜对了")
        elif caice < num :
            print("猜小了")
            caice = int(input("请再猜一次："))
            if caice != num :
                print("sorry, 您猜错了")
            else:
                print("恭喜您，猜对了")
                
                
a= 1                
b=0                

while a<=100:
    b += a
    a += 1
print(b)
            
            

import random
num = random.randint(1, 100)
ci = 0
i=int(input("请输入数字："))
while i != num:
    if i>num:
        print("猜大了")
        ci +=1
        i=int(input("请输入数字："))
        
    if i < num:
        print("猜小了")
        ci +=1
        i=int(input("请输入数字："))
print("你一共猜了%s次" % ci)





i = 1
while i <= 9:
    j=1
    while j <=i:
        print("%s*%s"%(j,i),end=' ')

        j+=1
    print()
    i+=1


name = "itheima is a brand of itcast"
j=0 
for k in name:
   
    if k == "a":
        j+=1
print("其中含有%d个英文字母a"%j)


count = 0
for i in range(0,100):
    if i % 2 ==0:
        count +=1
print("一共有%s个偶数"%count)
        
    
    

for i in range(5):
    print(i)
print(i)
    



for i in range(1,10):
    j=1
    for j in range(1,i+1):
        print("%s*%s=%s" %(j,i,j*i),end=(' '))
    print()
    
    
import random
money = 10000
people = 20
for i in range(1,21):
    num = random.randint(1, 10)
    if num < 5:
        print("员工%s,绩效分%s,低于5，不发工资，下一位"%(i,num))
        continue
    elif money == 0:
        print("工资发完了，请下个月再领取")
        break
    else:
        money -= 1000
        print("向员工%s发放工资1000元，帐户余额还剩余%s元"%(i,money))
    
def welcome_hesuan():
    
    print("欢迎查核酸")
    
    
def check(x):
    if x <=37:
        print("欢迎来到我家，请出示健康码，您的提问是%s,体温正常，请进！" %x)
    else:
        print("您的体温不正常，需要隔离")
        
       
    
    
def add(x,y):
    """
    
    """
    result = x+y
    print(f"两数相加的结果是：{result}")
    return result
a= add(1, 2)
print(a)







money = 5000000
name = input("请输入您的姓名：")
def cunqian():
    print("----------------存钱----------------")
    print("请输入您要存的钱。")
    global money
    qian = int(input())
    xianqian = money + qian
    print("%s您好，您存款%s元成功"%(name,qian))
    # print("%s您好，您的余额剩余：%s元"%(name,xianqian))
    money = xianqian

def quqian():
    print("----------------取钱----------------")
    print("请输入您要取的钱。")
    qian = int(input())
    global money
    xianqian = money - qian
    print("%s您好，您取款%s元成功"%(name,qian))
    # print("%s您好，您的余额剩余：%s元"%(name,xianqian))
    money = xianqian

def chaxun(key):
    if key:
        print("----------------查询余额----------------")
    print("%s您好，您的余额剩余：%s元"%(name,money))
def main_menu():
    print("----------------主菜单----------------")
    print("%s，您好，欢迎来到黑马银行atm。请选择操作："%name)
    print("查询余额\t[输入1]")
    print("存款\t\t[输入2]")
    print("取款\t\t[输入3]")
    print("退出\t\t[输入4]")
    return input("请输入您的选择：")
# 设置无限循环，保障程序不退出
while True:
    caozuo = main_menu()
    if caozuo == "1":
        key=True
        chaxun(key)
        continue
    elif caozuo == "2":
        key = False
        cunqian()
        chaxun(key)
        continue
        main_menu()
    elif caozuo == "3":
        key = False
        quqian()
        chaxun(key)
        continue
    elif caozuo == "4":
        break
    

age_list = [21,25,21,23,22,20]
age_list.append(31)
age_list.extend([29,33,30])
first = age_list.pop(0)
last = age_list.pop(-1)
index = age_list.index(31)
print(f"{first}")
print(f"{last}")
print(f"{index}")


num1 = []

for i in num:
    if i %2 ==0:
        num1.append(i)
print(f"通过for循环，从列表中取出偶数得到的新列表为：{num1}")




num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
index = 0
num1 = []
while index < len(num):
    if num[index] % 2 == 0 :
        num1.append(num[index])
    index +=1
print(f"{num1}")
        

num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
index = 0
num1 = []

while index < len(num):
    if num[index] % 2 == 0:  # Check if the current element is even
        num1.append(num[index])  # Append the even element to num1
    index += 1  # Increment the index to move to the next element

print(f"{num1}")



t1 = ('周杰伦',11,['football','music'])
age = t1.index(11)
print(f'{age}')
print(t1[0])
del t1[2][0]
t1[2].append('coding')
print(t1)



str_1 = "itheima itcast boxuegu"
num = str_1.count('it')
str_1.strip()
str_2=str_1.replace(' ', '/')
list_1= str_2.split("/")
print(f"{num}")
print(f'{str_2}')
print(f'{list_1}')
    
str_3 = '万过薪远，员序程马黑来，nohtyp学'
str_4 = str_3[::-1]
str_5 = str_4.split("，")
str_6 = str_5[1]
str6_=str_6.replace("来",'')
print(str6_)
print(f'{str_5[1]}')



my_list = ['黑马程序员','船只博客','黑马程序员','船只博客','itheima','itcast','itheima','itcast']
my_set = set()
for i in my_list:
    my_set.add(i)
print(my_set)    

my_dict={
    
    "王力宏":{
        
        "部门":"科技部",
        "工资": 3000,
        "级别": 1,
        },
    "周杰伦":{
        "部门":"市场部",
        "工资":5000,
        "级别":2,
        },
    "林俊杰":{
        "部门":"市场部",
        "工资":7000,
        "级别":3,
        },
    "张学友":{
        "部门":"科技部",
        "工资":4000,
        "级别":1,    
        },
    "刘德华":{
        
        "部门":"市场部",
        "工资":6000,
        "级别":2,   
        }
    
    }
keys = my_dict.keys() 
for i in keys:
    if my_dict[i]["级别"] == 1:
        my_dict[i]["级别"] +=1
        my_dict[i]["工资"] +=1000
print(f'{my_dict}')






















































