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
"""vd=np.arange(0,4)#phat song duoc thuc hien khi ca 2 mang tuong thich. 
#Dieu kien tuong thich: cac chieu phai bang nhau, hoac 1 trong so chung bang 1. vd: 2 ma tran 3x3, vd2: ma tran 3x3 va 3x1
print(10+vd)
vdkhac=np.arange(0,16).reshape(4,4)
vd1=vdkhac+vd
print(vd1)"""

#mang co cau truc
"""structs=np.array([(101,'trang',8.9),(102,'hoang',7.6)],dtype=('i2,S6,f4'))
print(structs)
print(structs[0])#truy cap theo chi muc
print(structs['f1'])#truy cap theo tên trường
structs.dtype.names=('id','ten','diem')#đổi tên trường
print(structs['diem'])#truy cập theo tên trường

vd3=np.array([(201,'hoang',5.0),(202,'nhat',4.9)],dtype='int16,U6,float32')
print(vd3)"""

"""vd4=np.random.random((3,3))
print(vd4)"""
#np.save('thunghiem',vd4)

load1=np.load('thunghiem.npy')
print(load1)