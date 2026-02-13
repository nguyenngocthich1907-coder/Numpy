import pandas as pd
import numpy as np

"""s=pd.Series([12,-4,7,9])
print(s)

s=pd.Series([12,-4,7,9],index=['a','b','c','d'])
print(s)
print(s.values)
print(s.index)
print(s['b'])

print(s['a':'c'])
print(s[['a','d']])
s=pd.Series([12,-4,7,9],index=['a','b','c','d'])
arr=np.array([1,2,3,4])
s3=pd.Series(arr)
s4=pd.Series(s)
print(s3)
print(s4[s4>8])#loc gia tri chi la gia tri lon hon 8

print(s3/2)

print(np.log(s))#co the dung phep toan cua numpy cho series"""

#danh gia cac gia tri==============
"""serd=pd.Series([1,0,2,1,2,3],index=['white','white','blue','green','green','yellow'])
print(serd)
print(serd.unique())#xuat gia tri doc nhat
print(serd.value_counts())#dem so lan cua 1 gia tri

print(serd.isin([2]))#kiem tra gia tri co trong 1 cau truc hay khong?
print(serd[serd.isin([2])])"""

#gia tri NaN
#day la mot gia tri dac biet (not a number) bieu dien gia tri trong hoac gia tri khong phai so
"""s2=pd.Series([5,-3,np.nan,14])#co the the gia tri NaN vao bang thu vien np (gio thi dung nan)
print(s2)
print(s2.isnull())
print(s2.notnull())"""

#series dong vao tro nhu tu dien
"""mydict={'red':2000,'blue':1000,'yellow':400,'orange':500}
myseries=pd.Series(mydict)
print(myseries)
colors=['red','blue','yellow','orange','green']#them green khong trung voi mydict se la nan
myserie=pd.Series(mydict,index=colors)
print(myserie)
#hoat dong giua cac Series
mydict2={'red':4000,'blue':1000,'black':300}
myseries2=pd.Series(mydict2)

print(myseries+myseries2)"""#khong cung nhan se ko cong duoc va khong xuat duoc

data={'color':['blue','green','yellow','red','white'],
      'object':['ball','pencil','paper','mug','tango'],'price':[1.2,1.4,2,4,5]}
frame=pd.DataFrame(data)
print(frame)