p=int(input("enter phy marks: "))
c=int(input("enter chem marks: "))
m=int(input("enter maths marks: "))
x=(p+c+m)/300*100
if  x>=75:
    print("u r passed with",x,"%. u have secured hon:")
elif x<75 and x>=60:
    print("u r passed with",x,"%. u have secured hon:")
 
else:
    print("u r passed with",x,"%. do more practice")
