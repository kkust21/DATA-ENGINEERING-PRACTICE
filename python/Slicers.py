msg = input("enter the string: " );
def fun(a,temp):
    if(a == temp):
        print("it is palidrom")
    else:
        print("not a palidrom")
a=msg[::-1]
temp=msg[::-1]
fun(a,temp)    

