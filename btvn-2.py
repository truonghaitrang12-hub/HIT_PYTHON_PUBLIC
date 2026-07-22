#bai1
thang = int(input("nhap thang:"))
nam = int(input("nhap nam:"))
if thang in [1,3,5,7,8,10,12]:
    print(31)
elif thang in [4,6,9,11]:
    print(30)
elif thang ==2:
    if(nam % 400 == 0 ) or (nam % 4 ==0 and nam % 100==0):
        print(29)
    else:
        print(28)
else:
    print("thang khong hop le.")

#bai2
ngay = int(input("nhap ngay sinh:"))
thang = int(input("nhap thang sinh:"))
so_ngay_trong_thang = {1:31, 2:29, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
if thang < 1 or thang > 12:
    print("thang ko hop le")
if ngay < 1 or ngay > so_ngay_trong_thang[thang]:
    print("so ngay ko hop le")
if (thang == 3 and ngay >= 21) or (thang == 4 and ngay<=19):
    print("Bach duong")
elif (thang==4 and ngay>=20)or(thang==5 and ngay<=20):
    print("Kim nguu")
elif (thang==5 and ngay>=21)or(thang==6 and ngay<=20):
    print("Song tu")
elif (thang==6 and ngay>=21)or(thang==7 and ngay<=22):
    print("Cu giai")
elif (thang==7 and ngay>=23)or(thang==8 and ngay<=22):
    print("Su tu")
elif (thang==8 and ngay>=23)or(thang==9 and ngay<=22):
    print("Xu nu")
elif (thang==9 and ngay>=23)or(thang==10 and ngay<=22):
    print("Thien binh")
elif (thang==10 and ngay>=23)or(thang==11 and ngay<=21):
    print("Bo cap")
elif (thang==11 and ngay>=22)or(thang==12 and ngay<=21):
    print("Nhan ma")
elif (thang==12 and ngay>=22)or(thang==1 and ngay<=19):
    print("Ma ket")
elif (thang==1 and ngay>=20)or(thang==2 and ngay<=18):
    print("Bao binh")
elif (thang==2 and ngay>=19)or(thang==3 and ngay<=20):
    print("Song ngu")
else:
    print("ngay thang ko hop le.")

#bai3
n = int(input("nhap so nguyen n:"))
tongchuso = 0
dem = 0
n_abs = abs(n)
check = True

if (n == 0): 
    tongchuso = 0
    dem = 1
else:
    while n_abs > 0:
        tongchuso += n_abs % 10
        dem += 1
        n_abs //= 10

if n <= 1:
    check = False
else:
    i = 2
    while i < n:
        if n % i == 0:
            check = False
            break
        i += 1

print(f"- Tổng chữ số của n là {tongchuso}")
print(f"- Số chữ số của n là {dem}")
if check == False:
    print(f"- Số n = {n} không phải số nguyên tố!")
else:
    print(f"- So n = {n} là số nguyên tố!")

#bai4
n = int(input("- Nhập số xu: "))
while n <=0:
    n = int(input("- Nhập lại số xu"))
GIA = 28
DOI = 3
sochai = n // GIA

if sochai > 0:
    vochai = sochai
    while vochai >= DOI:
        sochai += (vochai//DOI)
        vochai -= (vochai//DOI)*DOI

print(f"- Với {n} xu, số chai bia tối đa có thể uống là {sochai}")

