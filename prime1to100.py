for num in range(2,100):
    t=0
    for i in range(2,num):
        if num%i==0:
            t=1
            break
    if t==0:
       # print(num," is prime")
       print(num,end=" ")


        