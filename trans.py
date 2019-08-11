amt=0
while True:
    str=input("enter transaction:")
    transaction=str.split(" ")
    type=transaction[0]
    amt=int(transaction[1])
    if type=="D" or type=="d":
        amt +=amt
    elif type=="W" or type=="w":
        amt-=amt
    else:
        pass
    str=input("want to continue(Y for yes):")
    if not(str[0]=="Y" or str[0]=="y"):
        break
print ("net amount: ", amt)
