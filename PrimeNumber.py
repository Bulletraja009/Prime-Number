n=int(input("Enter Number"))
i=2
while(i<n):
    if n%i==0:
       print("Not Prime")
       break
    i+=1
else:
    if n==1:
        print("Not Prime")
    else:
        print("Prime")
