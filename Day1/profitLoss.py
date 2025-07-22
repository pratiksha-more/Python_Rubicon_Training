cp=int(input("Enter cost price: "))
sp=int(input("Enter selling price: "))

if sp > cp:
    profit = sp - cp
    print("Profit is:", profit)
elif sp < cp:
    loss = cp - sp
    print("Loss is:", loss)
else:
    print("No profit, no loss")