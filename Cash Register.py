bills = [100_000, 50_000, 20_000, 10_000, 5_000, 2_000, 1_000, 500, 200, 100]

def cash_register(bill, paid):
    change = (paid - bill)
    bills_returned = []
    var = 0
    while change >= 0 and var < 10:
        if change >= bills[var]:
            bills_returned.append(bills[var])
            change -= bills[var]
        else:
            var += 1
    return bills_returned


bill = int(input("Enter the amount needed: "))
paid = int(input("Enter the amount paid: "))
print(cash_register(bill,paid), f"Rp.{sum(cash_register(bill,paid)):,}")


