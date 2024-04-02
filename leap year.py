n=int (input("enter the year"))
if(n%4==0 and n%100!=0):
    print("leap year not a century year")

elif(n%400==0 and n%100==0):
    print("leap year and is a century year")

else: 
    print("not a leap year")
