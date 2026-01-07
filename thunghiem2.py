"""a=float(input("Nhap diem trung binh 0-10 "))
if(a<5):
    print("YEU")
elif (a<6.4): print("trung binh")
elif (a<7.9): print("Kha")
elif (a<8.9): print("gioi")
elif (a<10): print("Xuat sac")
else: print("Diem khong hop le")"""

"""a= int(input("Nhap so dien da su dung: "))
if(a<=50): print("so tien phai tra la ",a*2000)
elif(a<=100): print("so tien phai tra la ",50*2000+(a-50)*2500)
else: print("so tien phai tra la ",50*2000+50*2500+(a-100)*3000)"""

a=int(input("Cap hoc hien tai"))
Toan=float(input("nhap diem toan: "))
Van= float(input("nhap diem van: "))
Anh= float(input("Nhap diem anh: "))
match a:
    case 1:
        print("Ban la hoc sinh tieu hoc")
        print("diem tong ket: ",(Toan+Van+Anh)/3)
    case 2:
        print("diem tong ket: ",(Toan*2+Van*2+Anh)/5)
    case 3:
        print("diem tong ket: ",(Toan+Van+Anh*2)/4)    
