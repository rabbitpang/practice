import os
import numpy as np
import pandas as pd

##got endstate from statespace

state_space = 'phage11.txt'
with open(state_space) as file:
    lines0 = file.readlines()
    lines = []
    for row in lines0:
        lines.append(row.strip())

end_states = []
for i in range(1,len(lines)):
    state = lines[i]
    sep= lines[i].split()
    CI2 = int(sep[4])
    Cro2 = int(sep[5])

    if CI2 == 1 and Cro2 == 47:
        print(state)
        end_states.append(sep[0])

end_A = end_states.copy()
a = end_states[0]
del end_states[0]
print("endstate include a is")
print(end_A)
print("absorbing state is " +str(a))
print("endstate WITHOUT a is ")
print(end_states)

###########USE END STATE and oringinal matrix to get absorbing matrix

name ="phage0_matrix.txt"
with open(name) as file:
    line = (file.readline()).split()
output = "p0absorbing.txt"
#with open(output, 'a') as writer1:
 # writer1.write(line)

oldmtx = np.loadtxt(name,skiprows=1)
u, indice = np.unique(oldmtx[:,1], return_index=True)
ind = np.delete(indice, 0)
y = np.split(oldmtx, ind)
print(y)

sum_ele = 0
lines = []
###
for i in range(0, len(u)):
    block = y[i]
    rate_a = 0
    xj = int(u[i])
    print("xj is " + str(xj))
    ##xj is end or not?
    if str(xj) not in end_A:
        for j in range(0, len(block)):
            xi = int(block[j][0])
            rate = block[j][2]
            print(xi)
            if str(xi) not in end_A:
                print("xi not in end_A")
                lines.append(str(xi)+' '+str(xj)+' '+str(rate)+"\n")
                sum_ele += 1
               # with open(output, 'a') as writer1:
                #writer1.write(str(xi)+' '+str(xj)+' '+str(rate)+"\n")

            elif str(xi) in end_A:
                print("xi in end_A")
                rate_a  += rate
        if rate_a != 0 :
            print("xj and rate_a are "+ str(xj)+"  "+str(rate_a)+"\n")
            lines.append(str(a)+' '+str(xj)+' '+str(rate_a)+"\n")
            sum_ele += 1
            #with open(output, 'a') as writer1:
             # writer1.write(str(a)+' '+str(xj)+' '+str(rate_a)+"\n")


    elif str(xj) in end_A:
        continue

with open(output, 'a') as writer1:
    writer1.write(line[0]+" "+ str(sum_ele)+"\n")
    for row in lines:
        writer1.write(row)

