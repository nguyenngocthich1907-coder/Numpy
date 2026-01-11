import numpy as np

#======================buoi03================
#hoc ve chi muc, cat lat, lap lai trong numpy

#chi muc co 2 loai chi muc duong va chi muc am
#danh cho 2 loai mang la mang 1 chieu va mang 2 chieu
#a=np.arange(10,16)
"""print("ma tran a la: ",a)
print("Phan tu thu 2 trong mang: ",a[1])
print("phan tu cuoi cung trong mang ",a[5])
print("phan tu thu cuoi trong mang nhung chi muc am ",a[-1])
print("in cac phan tu o vi tri 1,3,4 ",a[[1,3,4]])"""

"""b=a.reshape(2,3)
print("ma tran b\n",b)
print("phan tu hang 1 cot 2",b[0,1])
print("phan tu hang 2 cot 3",b[-1,-1])"""

#cat lat// khai niem la xem 1 phan cua mang
""""ve cat lat mang 1 chieu:
co 2 doi so [chi muc dau:chi muc cuoi:khoang cach]
neu bo qua chi muc dau thi tu dong lay 0
neu bo qua chi muc cuo thi tu dong lay chỉ mục cuối trong mảng
nếu bỏ khoảng cách thì mặc định khoảng cách là 1"""

"""a=np.arange(10,16)
print("lat cat tu phan tu 1 den 5",a[1:5])
print("lat cat tu phan tu 1 va cat 2 don vi", a[1::2])
print("lat cat tu phan tu 0 khoang cach 2 don vi ",a[:5:2])"""

"""lat cat mang 2 chieu:
in ra hang, in ra cot, in ra cac hang lien tiep, in ra cac hang ko lien tiep
phuong thuc day du: A[hang,cot] // A[muc dau hang: muc cuoi hang,muc dau cot: muc cuoi cot]"""

"""vd=np.arange(10,19).reshape(3,3)
print("Ma tran 3x3: \n",vd)
print("in ra hang 0",vd[0,:])
print("in ra cot 0: ",vd[:,0])
print("in ra cac dong lien tiep\n",vd[0:2,0:2])
print("in ra 2 phan tu hang 0 va hang 2\n",vd[[0,2],0:2])"""

#===========Tiếp tục buổi 3=========================
#lap lai

vd2=np.arange(5,17).reshape(3,4)
"""print(vd2)
for i in vd2:
    for j in i:
        print(j)
for row in vd2:
    print(row)"""


"""vd3=np.apply_along_axis(np.mean,axis=0,arr=vd2)#truc so axis-0 thi theo hang doc
print(vd3)

vd4=np.apply_along_axis(np.mean,axis=1,arr=vd2)#truc so axis=1 thi theo hang ngang
print(vd4)"""

#điều kiện và mảng bool
"""vd5=np.array([[1,5,6],[1,2,7],[3,9,8]])
print(vd5>5)#se cho thay dap an cua tung phan tu co dung voi dk
print(vd5[vd5>5])#in ra man hinh cac so thoa dieu kien"""

#thao tac hinh dang
vd6=np.random.random(12)
dang1=vd6.reshape(3,4)
print(dang1)
"""vd6.shape=(4,3)
print(vd6)
vd6=vd6.ravel()
print(vd6)"""
print("============================")
dang2=dang1.transpose()
print(dang2)