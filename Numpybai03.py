import numpy as np
#==================================BUOI 04======================
#cac khai niem co ban cua numpy
#phat song, ban sao va dang xem, vector hoa, mang co cau truc

#ban sao va dang xem
"""a=np.arange(1,7)
b=a
print(a)
print(b)
print("=====================")
a[0]=0
print(b)#b chi la dang xem, cach goi moi cua ham a, chu khong tao thanh mot mang moi khac mang a
c=a[0:3]
print(c)
a[0]=2
print(c)"""#khi cat mot mang thi no cung chi la mot dang xem cua mang cho khong phai mang rieng biet

#vector hoa
#neu khong dung vector hoa thi se co mo ham phuc tap de thuc hien cac phep tinh
"""vd: for(i<0;i<rows;i++)
            c[i]=a[i]*b[i]
do la mang 1 chieu, con mang 2 chieu thi phai lam 2 vong lap for"""

#phat song
#khai niem la tao them, phong dai mot 
#ma tran de ma tran co so chieu bang voi so chieu cua ma tran thuc hien bai toan
vd=np.arange(0,4)
print(10+vd)
vdkhac=np.arange(0,16).reshape(4,4)
vd1=vdkhac+vd
print(vd1)
