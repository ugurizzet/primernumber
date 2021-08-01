a = 1
b = 100
for i in range(a, b):
    if i>1:
        for t in range(2, i):
            if(i%t == 0):
                    break
        else:
             print(i)