def DigitSum():
    Num=int(input("Enter the number "))
    sum=0
    while Num>0:
        digit=Num%10
        sum=sum+digit
        Num=Num//10
    print("sum of Digit is ",sum)

if __name__=="__main__":
    DigitSum()