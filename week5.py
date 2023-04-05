'''str="파이썬수업 파이썬수업 파이썬썬수업 파이썬수업 파이썬수업 파이썬수업"
print(str.replace("파이썬","자바",3))

print((str.replace("파이썬","자바",3)).count("파이썬"))

print(str)
print("find: ", str.find("파이썬썬"), "index: ", str.index("파이썬썬"))

str2="파이썬수업, 씨수업, 자바수업, 이썬수업, 파이썬수업"
print(str2.split(","))
print(str2.split("업"))

print("**".join(str))

print(3, "+", 4, "=", 7)

#format
f="{} + {} = {}".format(3,4,3+4)
f2="{0} {1} {0} {1} {2} {2}".format(1,2,3)
f3="{0} {1:10f} {0:10d} {1:10.3f} {2} {2}".format(1,2.0,3.0)

print(f)
print(f2)
print(f3)

print(type(True), type(False))
a="hello"
print(bool(a))
print(bool("hello"), bool("hi"), bool(3), bool(1.2))
print(bool(0), bool(" "), bool(""), bool(-1))'''

'''h=9
if h<12:
    print("오전")
elif h<18:
    print("오후")
else:
    print("저녁")'''

'''lunch=str(input("점심 먹을래? Y/N\n"))
if lunch=="N":
    print("먹지마")
elif lunch=="Y":
    lunch=str(input("학식? Y/N \n"))
    if lunch=="Y":
        print("8호관 ㄱㄱ")
    else:
        print("학식 싫어하는구나")
        lunch=str(input("그럼 서브웨이? Y/N \n"))
        if lunch=="Y":
            print("8관 1층 ㄱㄱ")
        else:
            print("꺼져")


else:
    print("꺼져")'''

'''for i in 1,2,3,4,5,6:
    print("i:", i)

for i in range(0,20,1):
    print(i)

for i in range(20):
    print(i)'''

'''sum=0
for i in range(1,11,1):
    sum+=i
print(sum)
sum=0
for i in(1,2,3,4,5,6,7,8,9,10):
    sum+=i
else:
    print(sum)'''

'''sum=0
n=0
while n<11:
    sum +=n
    print(n,"번째 sum:",sum)
    n+=1
print("while밖의 sum:",sum)'''

'''while True:
    word = input("단어입력")
    if word =="exit":
        print("exit --> break")
        break
        print("break뒤의 문장")
    elif word=="apple":
        print("apple-->continue")
        continue
        print("continue뒤의 문장")
    else:
        for i in range(3):
            print(word)'''

#import random
#print(random.randint(0,10))

'''from random import randint
from random2 import randint

print(randint(0,100000))'''

n=0
while n<4:
    h=int(input("키가 몇이니?"))
    if h>=150:
        n+=1
        print("네 타세요")
    else:
        print("타지 마세요")
print("출발합니다")
