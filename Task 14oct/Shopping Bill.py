
def calculateElectronicsGST(a, b):
    Total = a + b
    tax_amount = Total * 18 / 100
    final_amount = Total + tax_amount
    return final_amount


def calculateFashionGST(c, d):
    Total = c + d
    tax_amount = Total * 13 / 100
    final_amount = Total + tax_amount
    return final_amount


def calculateFoodGST(e):
    tax_amount = e * 7 / 100
    return e + tax_amount


def totalBill(a, b, c, d, e):
    electronics_bill = calculateElectronicsGST(a, b)
    fashion_bill = calculateFashionGST(c, d)
    food_bill = calculateFoodGST(e)

    grand_total = electronics_bill + fashion_bill + food_bill
    return grand_total


def calculateDiscountedBill(a, b, c, d, e):
    bill_amount = totalBill(a, b, c, d, e)

    discount_amount = bill_amount * 20 / 100
    payable_amount = bill_amount - discount_amount

    print(f"Total after GST = {bill_amount:.2f}")
    print(f"Discount = {discount_amount:.2f}")
    print(f"Final payable amount = {payable_amount:.2f}")

    return payable_amount


calculateDiscountedBill(100, 100, 100, 100, 100)
