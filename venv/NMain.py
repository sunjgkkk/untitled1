# 数据库操作
import psycopg2

conn = psycopg2.connect(database='postgres',user='postgres',password='19821027kkk',host='127.0.0.1',port='5432')
cur = conn.cursor()
print("Open database successfully")

cur.execute("select * from students_table,teachers_table;")
rows = cur.fetchall()
print(rows)
for i in rows:
    print(i)
conn.commit()
cur.close()
conn.close()




# 入门开始
print("Hello World!");

#3.1  列表 定义
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
#列表 打印
print(bicycles)
#3.1.1  访问列表元素
print(bicycles[0])
#3.1.2  列表索引从0开始而不是1开始
print(bicycles[0].title())
print(bicycles[1].title())
print(bicycles[2].title())
print(bicycles[3].title())
#列表 返回最后一一个元素
print(bicycles[-1])


message = "My first bicycle was a " + bicycles[0].title()+"."
print(message)

#3.2  修改、添加和删除元素
motorcycles=['honda','yamaha','suzuki']
print (motorcycles)
#3.2.1  修改列表元素
motorcycles[0]='ducati'
print(motorcycles)

#3.2.3 在列表中添加元素
motorcycles.append('dukati')
print (motorcycles)

motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')

print(motorcycles)

#  在列表中插入元素

motorcycles.insert(0,'ducati')
print(motorcycles)

#3.2.3 从列表中删除元素
#1.使用del语句删除元素
del  motorcycles[0]
print(motorcycles)
#2.使用方法pop()删除元素
popped_motorcycles=motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)

motorcycles=['honda','yamaha','suzuki']
last_owned = motorcycles.pop()
print("The last motocycle I owned was a "+ last_owned.title()+".")

#3.弹出列表中任何位置处的元素
motorcycles=['honda','yamaha','suzuki']
first_owned = motorcycles.pop(0)
print('The first motocycle I owned was a '+first_owned.title()+'')
print(motorcycles)
#4 根据值删除元素
motorcycles = ['honda','yamaha','suzuki','ducati']
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)

motorcycles = ['honda','yamaha','suzuki','ducati']
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA "+too_expensive.title()+" is too expensive for me.")

#3.3  组织列表
#3.3.1 使用sort()对列表进行永久性排序
cars =['bmw','audi','toyota','subaru']
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)

# 3.3.2 使用函数sorted()对列表进行临时排序
cars =['bmw','audi','toyota','subaru']
print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original list again:")
print(cars)

#3.3.3 倒着打印列表
cars =['bmw','audi','toyota','subaru']
print(cars)
cars.reverse()
print(cars)

#3.3.4 确定列表的长度
print(len(cars))


#3.4 使用列表时避免索引错误
motorcycles =['honda','yamaha','suzuki']
print(motorcycles)

print(motorcycles[-1])
#4.1 遍历整个列表
#4.1.1 深入地研究循环
magicians = ['alice','david','carolina']
for magician in magicians:
    print(magician)

#4.1.2 在for循环中执行更多的操作
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title()+",that was a great trick!")

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title()+",that was a great trick!")
    print("I can't wait to see your next trick," + magician.title()+".\n")


magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title()+",that was a great trick!")
    print("I can't wait to see your next trick," + magician.title()+".\n")
print("Thank you, everyone. That was a great magic shouw!")

#4.2 避免缩进错误
#4.2.1 忘记缩进
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)

#4.3 创建数值列表
#4.3.1 使用函数range()
for value in range(1,5):
    print(value)
#4.3.2 使用range()创建数字列表
numbers = list(range(1,6))
print(numbers)

even_numbers = list(range(2,11,2))
print(even_numbers)



squares = []
for value in range(1,11):
    #square =value**2
    squares.append(value**2)
    print(squares)
print(squares)

#4.3.3 对数字列表执行简单地统计计算
print(min(squares))
print(max(squares))
print(sum(squares))

#4.3.4 列表解析
squares =[value**2 for value in range(1,11)]
print(squares)


print([value for value in range(1,21)])


squares =[]
for value in range(1,1000001):
    squares.append(value)

print(min(squares))
print(max(squares))
print(sum(squares))


even_numbers = list(range(1,21,2))
for even_number in even_numbers:
    print(even_number)
print(even_numbers)

numbers = list(range(1,10))
for number in numbers:
    print(number**3)
print(numbers)

# 4.4使用列表的一部分
#4.4.1 切片

players = ['charles','martina','michael','flrence','eli']
print(players[0:3])

#4.42  遍历切片
players = ['charles','martina','michael','flrence','eli']
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())

#4.4.3 复制列表

my_foods = ['pizza','falafel','carrot cake']
friend_foods = my_foods[:3]
print("My favoraite foods are:")
print(my_foods)

print("\nMy friend's favorate foods are:")
print(friend_foods)


# 4.5 元祖
#4.5.1 定义元祖
dimensions = (200,50)
print(dimensions[0])
print(dimensions[1])

#4.5.2 遍历元组中的所有值
# dimensions[0] = 250
for dimension in dimensions:
    print(dimension)

# 4.5.3 修改元组变量
dimensions = (200,50)
print("Original dimension:")
for dimension in dimensions:\
print(dimension)

dimensions = (400,100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)

#4.6 设置代码格式
#4.6.1 格式设置指南
#4.6.2 缩进  PEP8 建议每级缩进都使用4个空格
#4.6.3 行长：每行不超过80字符
#4.6.4  空行
#4.6.5 其他格式设置指南
    #四个空格
    #tab

#第五章 if语句

#5.1 一个简单示例
cars = ['audi','bmw','subaru','toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
#5.2  条件测试
#5.2.1 检查是否相等
# car = 'bmw' , car == 'bmw' , True
# car = 'audi' , car == 'bmw' , False
#5.2.2 检查是否相等时不考虑大小写
# car = 'Audi'  car == 'audi'  False
#car = 'Audi'  car.lower() == 'audi' True
#5.2.3 检查是否不相等
requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print("Hold the anchovies")
#5.2.4 比较数字
answer = 17
if answer !=42:
    print("That is not the correct answer . Please try again!")

# < <= > >=

#5.2.5 检查多个条件
#1. 使用and检查多个条件
age_0=22
age_1=18
if age_0>=21 and age_1>=21:
    print("false")

age_1 = 22

if age_0>=21 and age_1>=21:
    print("true")
#2. 使用or 检查多个条件
#5.2.6 检查特定值是否包含在列表中
requested_topping = ['mushrooms','onions','pineapples']

if 'mushrooms' in requested_topping:
    print("mushrooms in requested_topping")
else:
    print("mushrooms not in requested_topping")


if 'pepperoni' in requested_topping:
    print("False")
else:
    print("pepperoni ont in requested_topping")

#5.2.7 检查特定值是否不包含在列表中
banned_users = ['andrew','carolina','david']
user = 'marie'

if user not in banned_users:
    print(user.title()+", you can post a response fi you wish.")
else:
    print(user.title()+", you can't post a response fi you wish.")
#5.2.8 布尔表达式
game_active = True
can_edit = False

car = 'subaru'
print("Is car =='subaru'? I predict True.")
print("\nIs car == 'audi'? I perdict False.")
print(car == 'audi')

#5.3 if语句
#5.3.1 简单地if语句
#if conditional_test:
#    do something

age = 19
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")

#5.3.4 if-else语句
age = 17
if age >=18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry,you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")

#5.3.3 if-elif-else结构

age = 12
if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $5.")
else:
    print("Your admission cost is $10.")
#5.3.4 使用多个elif代码块

age = 12
if age<4:
    price = 0
elif age < 18:
    price = 5
elif age <65:
    price = 10
else:
    price = 5
print("\nYour admission cost is $" + str(price)+".")

#5.3.5 省略else代码块
age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
elif age >=65:
    price = 5
    print("Your admission cost is $" + str(price) + ".\n")

#5.3.6 测试多个条件
requested_toppings = ['mushrooms','extra cheese']
if 'mushrooms' in requested_toppings:
    print("Adding mushroom.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")

    print("\nFinished making your pizza!")


# 第六章 字典
#6.1 一个简单地字典

alien_0 = {'color':'green','points' :5}

print(alien_0['color'])
print(alien_0['points'] )

#6.2 使用字典
#在Python 字典是一系列键-值对。每个键都与一个值关联
alien_0 = {'color':'green'}
#6.2.1 访问字典中的值
alien_0 = {'color':'green'}
print("\n" + alien_0['color'])
#6.2.2 添加键-值对
alien_0 = {'color':'green','points':5}
print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

#6.2.3 创建一个空字典
alien_0 = {}
print(alien_0)

alien_0['color'] = 'green'
alien_0['points'] = 5

print(alien_0)

#6.2.4 修改字典中的值

alien_0 = {'color':'green'}
print("\nThe alien is " + alien_0['color'] + ".")

alien_0['color'] = 'yellow'
print("\nThe alien is now " + alien_0['color'] + ".")


#对一个能够以不同速度移动的外星人的位置进行跟踪
alien_0 = {'x_position':0,'y_position':25,'speed':'medium'}
print("\nOriginal x_position: " + str(alien_0['x_position']))

#向右移动外星人
#据外星人当前速度觉得将其移动多远
if alien_0['speed'] == 'slow':
    x_increament = 1
elif alien_0['speed'] == 'medium':
    x_increament = 2
else:
# 这个外星人的速度一定很酷
    x_increament = 3
# 新位置等于老位置加上增量
alien_0['x_position'] = alien_0['x_position'] + x_increament
print('New x-position: ' + str(alien_0['x_position']))

#6.2.5 删除键-值对

alien_0 ={'color':'green','points':5}
print(alien_0)

del alien_0['points']
print(alien_0)

#6.2.6 由类似对象组成的字典

favorite_languages = {
    'jen' : 'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
     }

print("Sarah's favorite language is "+
      favorite_languages['sarah'].title()+
      ".")
# 6.3 遍历字典

#6.3.1 遍历所有的键-值对
user_0 = {
    'username':'efermi',
    'first':'enrico',
    'last':'fermi',
    }
for key,value in user_0.items():
    print("\nKey: " + key)
    print("Value: " + value)



favorite_languages = {
    'jen' : 'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
     }
for name,language in favorite_languages.items():
    print("Name: " + name)
    print("Language: " + language)



#6.4 嵌套

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)


# 创建一个用于存储外星人的空列表

aliens = []
#创建30个绿色的外星人
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5,'speed': 'slow'}
    aliens.append(new_alien)
#显示前五个外星人
for alien in aliens[:5]:
    print(alien)
print('...')
# 显示创建多少个外星人
print("Total number of aliens: " + str(len(aliens)))


