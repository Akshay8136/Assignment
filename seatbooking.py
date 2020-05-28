s=int(input("Enter a seat number:"))
if s>0 and s<73:
    if s%8==1 or s%8==4:
        print("lower berth")
    elif s%8==2 or s%8==5:
        print("middle berth")
    elif s%8==3 or s%8==6:
        print("upper berth")
    elif s%8==7:
        print("side lower berth")
    else:
        print("side upper berth")
else:
    print("invalid seat number")
