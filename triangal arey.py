import math
a=int(input("Enter the fast vlue="))
b=int(input("Enter the Second vlue="))
c=int(input("Enter the thard vlue="))
s=(a+b+c)/2
if((a+b)>c) and ((a+c)>b):
    arey=math.sqrt(s*(s-a)*(s-b)*(s-c))
    print("Enter the Triangal Arey=",arey)
else:
    print("Enter the Triangal Arey not pssible")