def Prime():
      Num=int(input("Enter the number "))
      if Num<=1:
            print("Not prime Number")
      else:
            Count=0
            for i in range(2,Num):
                  if (Num%i==0):
                        Count+=1
            if Count==0:
                  print("prime Number")
            else:
                  print("Not prime Number")
      
if __name__=="__main__":
      Prime()