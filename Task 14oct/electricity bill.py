
def calculateElectricityBill(units):
    if units <= 100:
        bill = units * 3.96
    elif units <= 300:
        bill = 100 * 3.96 + (units - 100) * 10.80
    elif units <= 500:
        bill = 100 * 3.96 + 200 * 10.80 + (units - 300) * 15.03
    else:
        bill = 100 * 3.96 + 200 * 10.80 + 200 * 15.03 + (units - 500) * 17.53

    return bill


def calculateFinalBill(units):
    bill = calculateElectricityBill(units)
    charge = bill * 5 / 100
    return bill + charge


units = int(input("Enter electricity units: "))

bill = calculateElectricityBill(units)
final_bill = calculateFinalBill(units)

print(f"Electricity Bill = {bill:.2f}")
print(f"Final Bill = {final_bill:.2f}")
