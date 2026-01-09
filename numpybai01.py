import numpy as np
#bai 1
"""a= np.arange(1,21)
b=a*a
print(b)"""

#bai 2
"""Tạo ma trận 3×4 số nguyên ngẫu nhiên từ 1–100:

Tính trung bình từng cột

Tìm giá trị lớn nhất của mỗi hàng
bai2=np.arange(1,13).reshape(3,4)
print(bai2)"""

#===============================BUOI1================================================
#Học lại từ cơ bản buổi đầu chương 3 từ trang 51 đến trang 58
#mục tiêu học được tất cả thao tác cơ bản cửa ndarray: dtype, dim,size, shape,type,itemsize, data
#học được cách tạo 1 mảng và phân tích các thành phần chỉ số của nó

"""a=np.array([[1,2,3],[4,5,6]],dtype=int)

print(type(a))#kiểm tra xem đối tượng có phải là ndarray hay ko
print(a.ndim)#tính số chiều của ma trận
print(a.size)#tính tổng số phần tử có trong ma trận
print(a.data)#bộ nhớ đệm
print(a.itemsize)#8=(64/8) vì là kiểu int64
print(a.shape)#số hàng số cột
print(a.dtype)#kiểu dữ liệu của phần tử
print(a)

chuoi=np.array([['a','b'],['c','d']])
print(chuoi.dtype.name)"""

#==============================BUOI2====================================
#MỤC TIÊU: học được cách tạo mảng (ma trận) bằng các cách khác nhau (zeros, ones, arange, random,linespace
#các toán tử cơ bản cộng, trừ, nhân, toán tử tăng, giảm
#hàm phổ quát, hàm tổng hợp

"""các cách tạo mảng"""
"""ones=np.ones((3,3))
print("ma tran don vi 3x3:\n ",ones)
zeros=np.zeros((3,3))
print("ma tran 0 3x3\n ",zeros)
arange=np.arange(0,12)
print("Ma tran phan tu theo trinh tu:\n ",arange)
ashape=arange.reshape(3,4)
print("Ma tran arange nhung hinh dang 3x4:\n ",ashape)
aline3=np.arange(0,12,3)
print("Ma tran arange moi phan tu cach 3 don vi: ",aline3)
linespace=np.linspace(0,12,4)#doi so thu 3 chi so phan tu de tach
print("ma tran giong arange co doi so\n ",linespace)
randoms=np.random.random((2,3))
print("ma tran ngau nhien 2x3:\n ",randoms)"""

#cac toan tu cua mang==================

#a=np.arange(0,4).reshape(2,2)
#b=np.arange(5,9).reshape(2,2)

"""print("phep cong a+4: \n",a+1)
print("phep tru a-1:\n",a-1)
print("phep nhan a*2\n",a*2)
print("cong 2 ma tran a+b\n",a+b)"""

"""print("ma tran a:\n",a)
print("ma tran b:\n",b)
print("nhan 2 ma tran a*b\n",a*b)#chuc năng của riêng numpy nhân từng phần tử
print("nhan 2 ma tran dot(a,b)\n",np.dot(a,b))"""#nhân 2 ma trận đúng

"""a+=1#có thể tăng giá trị của từng phần tử trong a tùy ý, vd:2,3,..n
print("toan tu tang a+=1\n",a)
a-=1#có thể giảm giá trị của từng phần tử trong a tùy ý,vd: 2,3,..n
print("toan tu giam a-=1\n",a)"""
"""a*=2
print("toan tu tang a*2\n",a)"""

#hàm phổ quát và hàm tổng hợp

vd=np.arange(1,5)
print("can tung phan tu\n",np.sqrt(vd))
print("sin tung phan tu\n",np.sin(vd))
print("log tung phan tu\n",np.log(vd))

vd2=np.array([3.3,4.5,1.2,5.7,0.3])
print("phep cong tong hop: ",vd2.sum())
print("phan tu nho nhat trong mang: ",vd2.min())
print("phan tu lon nhat trong mang ",vd2.max())
print("trung bình phan tu: ",vd2.mean())
print("độ lệch chuẩn: ",vd2.std())




