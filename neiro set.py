import numpy as np
import matplotlib.pyplot as plt

input_dim=4
out_dim=3
h_dim=3
h2_dim=3

loss_srr=[]

def relu(t):
	return np.maximum(t,0)

def softmax(t):
	out = np.exp(t)
	return out/np.sum(out)

def sparse_cross_entopy(z,y):
	return -np.log(z[0,y])

def tp_full(y, num_classes):
	y_full = np.zeros((1, num_classes))
	y_full[0,y]=1
	return y_full

def relu_deriv(t):
	return (t>=0).astype(float)

x=np.random.randn(1,input_dim)
y=np.random.randint(0,input_dim-1)

w1=np.random.randn(input_dim,h_dim)
b1=np.random.randn(1,h_dim)

w2=np.random.randn(h_dim,h2_dim)
b2=np.random.randn(1,out_dim)

w3=np.random.randn(h2_dim,out_dim)
b3=np.random.randn(1,out_dim)


num_epochs=400
ALPHA=0.002

for ep in range(int(float(num_epochs))):
	for i in range(5):
		t1=x@ w1 + b1
		h1=relu(t1)
		t2=h1@ w2 + b2
		h2=relu(t2)
		t3=h2@w3+b3
		z=softmax(t3)
		E=sparse_cross_entopy(z,y)
			#backwarm
		y_full=tp_full(y, out_dim)
		dE_dt2=z-y_full
		dE_dw2=h1.T @ dE_dt2
		dE_db2= dE_dt2

		
		dE_dh1= dE_dt2 @ w2.T 
		dE_dt1=dE_dh1 * relu_deriv(t1)
		dE_dw1=x.T @ dE_dt1
		dE_db1= dE_dt1


				#updaate
		w1=w1- ALPHA * dE_dw1
		b1= b1 - ALPHA * dE_db1
		w2=w2 - ALPHA * dE_dw2
		b2= b2 - ALPHA * dE_db2
		loss_srr.append(E)

#print(z)
#print("w1",w1)
#print("w2",w2)
#print("b1",b1)
#print("b2",b2)
#plt.plot(loss_srr)
#plt.show()


new_x=np.array([[0,0,1,0]])
t1=new_x@ w1 + b1
h1=relu(t1)
t2=h1@ w2 + b2
z2=softmax(t2)

print(z2)