actual_amount=(int(input("Enter the actual amount: ")))
sales_amount=(int(input("Enter the sales amount: ")))
if sales_amount>actual_amount:
    amount=sales_amount-actual_amount
    print("total profit is {0}".format(amount))
else:
    print("there is no profit")
