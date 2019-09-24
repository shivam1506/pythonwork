names="modi yogi raj rajnath amit nirmla ajeet vksingh"
nm=names.split()
l=len(nm)
test=input("enter name:")
if test in names:
    print(test," found in:",l,"names")
else:
    print(test," not found in:",l,"names")