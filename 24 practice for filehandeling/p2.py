#  writing multiplication table of difffernt numbers in different files 

from asyncore import read


for i in range (1,11):
    with open (f'multiplication table of {i}.txt','w') as f:
        for j in range (1,11):
         a=f.write(f'{i}X{j}={i*j}\n')

