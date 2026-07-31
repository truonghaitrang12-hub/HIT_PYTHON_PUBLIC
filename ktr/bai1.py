x= int(input("nhap x:"))
a= list(map(int,input("nhap a:").split(',')))
sum=0
for i in range(len(a)):
    sum+=a[i]*x**(x-1)
    print(sum)