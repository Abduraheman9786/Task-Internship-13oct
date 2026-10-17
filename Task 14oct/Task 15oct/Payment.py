
# balance = 5000

# amount = int(input("Enter shopping amount: "))

# if amount>=0:
#     if amount>balance:
#         print("Insufficient balance")
#     else:
#         print("Payment Success")
# else:
#     print("Invalid Amount")


# balance = 5000

# amount = int(input("Enter shopping amount: "))

# if amount >= 0:
#     if amount > balance:
#         print("Insufficient Balance")
#     elif amount == balance:
#         print("Payment Success")
#         print("Account khali ho gaya hain")
#     else:
#         print("Payment Success")
# else:
#     print("Invalid Amount")


balance = 5000

amount = int(input("Enter shopping amount: "))

if amount >0:
    if amount > balance:
        print("Insufficient Balance")
    elif amount == balance:
        print("Payment Success")
        print("Account khali ho gaya hain")
    else:
        print("Payment Success")
        balance = balance - amount
        print("Remaining Balance =", balance)
else:
    print("Invalid Amount")
