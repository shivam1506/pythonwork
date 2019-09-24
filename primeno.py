num=19
t=0
for i in range(2,num):
    if num%i==0:
        t=1
        break
if t==1:
    print("its not prime")
else:
    print("its prime")


        