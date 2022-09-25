import numpy as np

a=np.array([[14,56,77],[47,58,6],[78,58,49]])

b=np.array([[10,11,12],[1783,184,515],[516,147,518]])

print("addition\n",a+b)# additon
print("subtraction\n",a-b)#subtraction
print("multiply\n",a*b)#multiply
print("division\n",a/b)#division

#dot prodct
print("dot product\n",np.dot(a,b))
sum=0
for i in a:
    for j in i:
        sum+=j
print("sum of all elements\n",sum)
row_sum=0
for i in range(len(a)):
    for j in range(len(a)):
        row_sum+=a[i][j]
    print("Sum row",i+1,"=",row_sum)
    row_sum=0
col_sum=0
for i in range(len(a)):
    for j in range(len(a)):
        col_sum+=a[j][i]
    print("Sum col",i+1,"=",col_sum)
    col_sum=0
c=np.transpose(a)
print("transpose\n",c)
prin_dia=0
for i in range(len(a)):
    prin_dia+=a[i][i]
print("principal diagonal sum\n",prin_dia)
sec_dia=0
for i in range(len(a)):
    sec_dia+=a[i][(len(a)-1)-i]
print("secondary diagonal sum\n",sec_dia)
