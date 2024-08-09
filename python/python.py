year = int(input("enter the year"));
"""if(year%400==0):
   print("leap year")
else:
    if(year%100!=0):
        if(year%4==0):
            print("leap year")
        else:
             print(" not leap year")
    else:
         print(year,"not a leap year")"""


if(year%400==0):
    print("leap year")
elif(year%100!=0 & year%4==0):
    print(year, "leap year")
else:
    print("not leap year")

