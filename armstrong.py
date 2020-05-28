lower = 10
n=int(input("Emter a number gtreater than 10:"))
for num in range(lower,n):
    order =len(str(num))

    sum=0
    temp=num
    while temp>0:
        digit = temp%10
        sum += digit**order
        temp //=10

    if num == sum:
        print(num)
     
