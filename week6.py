#리스트=["a","b","c"]   수정 가능
#튜플=("a","b","c")     수정 불가
#딕셔너리={"a1":"b1", "a2":"b2"}

lst1=[]
lst1.append("김밥")
lst1.append("떡볶이")
lst1.append("튀김")
lst1.append("순대")
lst1.append("김밥")
lst1.append("식혜")
'''print(lst1)
############################################################
lst1.insert(0,"식혜")
print(lst1)
lst1.insert(0,"콜라")
print(lst1)
############################################################
print("list 3번째 값",lst1[2])
############################################################
for i in range(len(lst1)):
    print(lst1[i])

for item in lst1:
    print(item)
############################################################
lst1.insert(0,"김밥")
print(lst1)
print(lst1.count("김밥"), lst1.index("김밥"))
############################################################
#sclicing
#print(start:end:step)
print(lst1)
#print(lst1[::])#전체
#print(lst1[0:len(lst1):1])#전체
print(lst1[::-1])
############################################################
print(lst1)
lst1.remove("김밥")
print(lst1)
############################################################
print(lst1)
print(lst1.pop())
print(lst1.pop(2))
print(lst1)

dst=["케이크","커피","우유","와플"]
print(dst)
print(lst1)
lst1.extend(dst)
print(lst1)
print(lst1)
sorted(lst1)
print(lst1)
print(sorted(lst1))
print(lst1)
lst1.sort()
print(lst1)
############################################################
print(lst1)
lst1.reverse()
print(lst1)

lst1.clear()
print(lst1)

l1=[]
for i in range(11):
    l1.append(i)

print(l1)

l2=[i**2 for i in range(11)]
print(l2)

l3=['hello' for i in range(10)]
print(l3)

l4=[i**2 for i in range(0,11,2)]
print(l4)

l5=[i**2 for i in range(11) if(i%2==0)]
print(l5)'''

a=[0,1,2,3,4,5]
b=a
print(a)
print(b)

a.pop()
print(a)
print(b)

print(a is b)

b.append(333)

print(a)
print(b)

c=a[:]

print(a)
print(c)

a.append(111)

print(a)
print(c)

