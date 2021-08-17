tsum = 0
for x in range(0,100):
    a = [] 
    sum = 0
    a.append(int(1*(1 + 0.1*x)))
    a.append(int(2*(1 + 0.1*x)))
    a.append(int(4*(1 + 0.1*x))) 
    a.append(int(8*(1 + 0.1*x)))     
    a.append(int(12*(1 + 0.1*x)))
    a.append(int(20*(1 + 0.1*x)))
    a.append(int(32*(1 + 0.1*x))) 
    a.append(int(50*(1 + 0.1*x))) 
    a.append(int(80*(1 + 0.1*x))) 
    a.append(int(140*(1 + 0.1*x)))  
    a.append(int(250*(1 + 0.1*x)))  
    a.append(int(500*(1 + 0.1*x)))
    a.append(int(1000*(1 + 0.1*x)))
    a.append(int(2000*(1 + 0.1*x)))
    for i in a:
        sum = sum + i
    print(f'{x}: {sum}')
    tsum = tsum + sum
print(tsum)