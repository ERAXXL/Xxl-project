import numpy as np
xx=[]
yy=[]
for i in range(0,15):
    x=1
    y=0
    xx.append(x)
    yy.append(y)
f1=open(r'C:\Users\palua\OneDrive\Рабочий стол\game\\My 3\info.txt','w')
f1.write('hi\n')
f1.writelines('x and y \n')
np.savetxt(r'C:\Users\palua\OneDrive\Рабочий стол\game\\My 3\info.txt',xx,fmt='%.2f')
np.savetxt(r'C:\Users\palua\OneDrive\Рабочий стол\game\\My 3\info.txt',xx,fmt='%.2f')
f1.close()
print(xx,yy)