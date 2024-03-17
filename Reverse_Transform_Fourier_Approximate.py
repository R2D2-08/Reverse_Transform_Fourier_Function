import numpy as np 
import matplotlib.pyplot as plt 
x=np.arange(-3.141592,3.141592,6.283184/202)
output_matrix=[(
np.sin(i)+2*np.sin(2*i)+3*np.sin(3*i)+4*np.sin(4*i)+5*np.sin(5*i)+np.cos(i)+2*np.cos(2*i)+3*np.cos(3*i)+4*np.cos(4*i)+5*np.cos(5*i)) for i in x]
input_matrix_1=np.zeros((202,202),dtype=float)
count=0
for i in x:
    if count==202 : break
    for n in range(1,102):
        input_matrix_1[count,n-1]=np.cos(n*i)
        input_matrix_1[count,(n+100)]=np.sin(n*i)
    count+=1    
input_matrix_2=np.matmul(np.linalg.inv(input_matrix_1),output_matrix)
for i in range(202):
    if np.abs(input_matrix_2[i])<0.001 : 
        input_matrix_2[i]=0
for i in input_matrix_2 : print(i)