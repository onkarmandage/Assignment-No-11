def Reverse():
    Num=int(input("Enter the number "))
    reverse=0
    while Num>0:
        digit=Num%10
        reverse=reverse*10+digit
        Num=Num//10
    print("Reverse number is ",reverse)
    

if __name__=="__main__":
    Reverse()