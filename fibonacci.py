num = int(input("enter number : "))
 
first = 0
second = 1
 
print("fibonacci series is:")
print(first,",",second,end=",")
 
for i in range(2, num):
	next = first + second
	print(next,end=",")
 
	first = second
	second = next