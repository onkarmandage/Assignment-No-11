def Palindrome():
    Num=int(input("Enter the Number "))
    original=Num
    reverse=0
    while Num>0:
        digit=Num%10
        reverse=reverse*10+digit
        Num=Num//10
    if(original==reverse):
        print("Number is palindrome")
    else:
        print("number is not palindrome")

if __name__=="__main__":
    Palindrome()