from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import math
img = np.asarray(Image.open('face.png'))
N=40
tri=np.triu(np.ones(N))
tri2=np.ones((N,N))-tri
#print(tri)
y1=np.arange(N)+np.zeros((N,1))
y2=y1.T*tri/(N-1)
y1=(N-y1-1)*tri/(N-1)
y3=tri-y1-y2
print(y1)#[0,0])
print(y2)#[N-1,N-1])
print(y3)#[0,N-1])
interp=np.ones(np.shape(img))
X=math.floor(np.shape(img)[0]/N)
Y=math.floor(np.shape(img)[1]/N)
print(X,Y)
for c in range(4):
  for i in range(X):
    for j in range(Y):
      interp[N*i:N*i+N,N*j:N*j+N,c]= ((y1+y1.T*tri2)*img[N*i,N*j,c])/255
      interp[N*i:N*i+N,N*j:N*j+N,c]+=(y2+y2.T*tri2)*img[N*i+N-1,N*j+N-1,c]/255
      interp[N*i:N*i+N,N*j:N*j+N,c]+= y3.T*tri2*img[N*i+N-1,N*j,c]/255
      interp[N*i:N*i+N,N*j:N*j+N,c]+= y3*img[N*i,N*j+N-1,c]/255
err=np.ones(np.shape(img))
err[:,:,0:3] = (abs(img[:,:,0:3]/255-interp[:,:,0:3]))
#err[:,:,0]=img[:,:,0]
print(np.shape(img))
print(err)
#plt.plot(np.random.rand(100))
print(interp[:,:,0])
plt.imshow(interp)
plt.show()
