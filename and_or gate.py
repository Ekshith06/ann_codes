import numpy as np
x = [[1,1], [-1,1], [1,-1], [-1,-1]]
print("1.ADD")
print("2.OR")
ch = int(input("enter the choice(1,2):"))
if ch ==1:
    output = [1,-1,-1,-1]
    print("input matrix -->",x)

    print("output matrix -->",output)
    # lerning rule of perception:
    print("w1=0,w2=0,b=0,theta=o,threshold=(0,1)")

    w1=0;w2=0;b=0#intially take all zeroes
    teta = 0
    alpha = 1
    val=[[w1,w2,b]]
    def activation(f_net) :
        if f_net > teta :
            return 1
        elif f_net >= -(teta) & f_net <= teta :
            return 0
        else :
            return -1

    for i in range(len(x)) :
        f_net = np.dot(np.array([w1, w2]), x[i]) + b
        a = activation(f_net)
        if output[i] != a :
            w1 = w1+alpha*output[i]*x[i][0]
            w2 = w2+alpha*output[i]*x[i][1]
            b=b+alpha*output[i]
        val.append([w1,w2,b])  
    print(val)
else:
    output = [-1,1,1,1]
    print("input matrix -->",x)
    print("output matrix -->",output)
    # lerning rule of perception:
    print("w1=0,w2=0,b=0,theta=o,threshold=(0,1)")

    w1=0;w2=0;b=0#intially take all zeroes
    teta = 0
    alpha = 1
    val=[[w1,w2,b]]
    def activation(f_net) :
        if f_net > teta :
            return 1
        elif f_net >= -(teta) & f_net <= teta :
            return 0
        else :
            return -1

    for i in range(len(x)) :
        f_net = np.dot(np.array([w1, w2]), x[i]) + b
        a = activation(f_net)
        if output[i] != a :
            w1 = w1+alpha*output[i]*x[i][0]
            w2 = w2+alpha*output[i]*x[i][1]
            b=b+alpha*output[i]
        val.append([w1,w2,b])  
    print(val)

