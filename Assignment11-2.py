Num=int(input("Enter the number"))
if Num==0:
    count=1
else:
    count=0
    while Num>0:
        count+=1
        Num=Num//10
    print("Count of Digits =",count)