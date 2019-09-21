sbin=input("enter the binary string")
exp=len(sbin)-1
num=0
##l=len(sbin)
##num=0
##for c in range(0,l):
##    if not(c=='0' or c=='1'):
##        print("Enter a valid binary string")
##        break
##exp=l-1
##while(exp>=0):
for d in sbin:
        dec=int(d)*2**exp
        num=num+dec
        exp=exp-1
print("the decimal equivalent of {} is {} ".format(sbin,num))
