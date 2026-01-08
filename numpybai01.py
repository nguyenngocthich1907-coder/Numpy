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

#Học lại từ cơ bản buổi đầu chương 3 từ trang 51 đến trang 58
#mục tiêu học được tất cả thao tác cơ bản cửa ndarray: dtype, dim,size, shape,type,itemsize, data
#học được cách tạo 1 mảng và phân tích các thành phần chỉ số của nó

a=np.array([[1,2,3],[4,5,6]],dtype=int)

print(type(a))#kiểm tra xem đối tượng có phải là ndarray hay ko
print(a.ndim)#tính số chiều của ma trận
print(a.size)#tính tổng số phần tử có trong ma trận
print(a.data)#bộ nhớ đệm
print(a.itemsize)#8=(64/8) vì là kiểu int64
print(a.shape)#số hàng số cột
print(a.dtype)#kiểu dữ liệu của phần tử
print(a)

chuoi=np.array([['a','b'],['c','d']])
print(chuoi.dtype.name)