num=int(input("Enter the decimal number"))
bstring=""
if num==0:
    bstring=0
    print("the binary equivalent of {} is {}".format(num,bstring))
else:
    while(num>0):
        rem=num%2
        num=int(num/2)
        bstring=str(rem)+bstring
        print("{}  {}          {}".format(num,rem,bstring))
    print("the binary equivalent of {} is {}".format(num,bstring))
