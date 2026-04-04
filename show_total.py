def d_calculation(dic_orders):
    print("\n" + "*" * 50)
    print("DAILY INCOME REPORT".center(50))
    print("*" * 50)
    
    total_every_customer = 0
    for orders in dic_orders.values():
         for order in orders:
             total_every_customer += order["subtotal"]

    print(f"\nThe total income for the day is: {total_every_customer}")
    print("-" * 50 + "\n")
    
    return total_every_customer
