def final_generation(dic_orders): 
    print("\n" + "-" * 50)
    print("ORDERS BY CUSTOMER".center(50))
    print("-" * 50)

    a = 1
    while a == 1:   
        try:
            ask_Id = int(input("\nenter your ID: "))
            if ask_Id <= 0:
                print("enter ID valide :/")
                print("*" * 50 + "\n")
                continue
            else: 
                a = 2
        except ValueError:
            print("error, enter your number ID")
            print("*" * 50 + "\n")
            continue

    if ask_Id not in dic_orders:
        print("This customer has no orders.")
        print("*" * 50 + "\n")
        return
    
    else:
        total_orders = 0
        t_quantity = 0

        print(f"your ID:{ask_Id}")
        print("-" * 50)

        for order in dic_orders[ask_Id]:
            print(f"name :  {order['customer']}")
            print(f"Product: {order['product']} | Quantity: {order['quantity']} | Subtotal: {order['subtotal']}")
            print("-" * 30)
            t_quantity += order["quantity"]
            total_orders += order["subtotal"]

        orderss = len(dic_orders[ask_Id])
        print(f"Total number of orders placed by the customer: {orderss}" )     
        print(f"total orders: {total_orders}")
        print(f"total product quantity: {t_quantity}" )
        print("*" * 50)

    return

def final_report(dic_orders): 
    print("\n" + "*" * 60)
    print("FINAL REPORT".center(60))
    print("*" * 60)

    # 1 - Total de pedidos
    total_orders = 0
    for orders in dic_orders.values():
        total_orders += len(orders)
    print(f"\nTotal orders: {total_orders}" )
    
    # 2 - Total de ingresos
    total = 0
    for orders in dic_orders.values():
        for order in orders:
            total += order["subtotal"]
    print(f"Total income: $ {total}")
    
    # 3 - Pedidos por cliente
    print("\n" + "Orders by customer:".center(60, "-"))
    for customer_id, orders in dic_orders.items():
        print(f"Customer ID: {customer_id}")
        for order in orders:
            print(f"Product: {order['product']}")
            print(f"Quantity: {order['quantity']}" )
            print(f"Subtotal: ${order['subtotal']}" )
            print("-" * 50)
    
    # 4 - Productos vendidos
    print("\n" + "Products sold:".center(60, "-"))
    for orders in dic_orders.values():
        for order in orders:
            print(f"Product: {order['product']} | Quantity: {order['quantity']}" )
            print("-" * 50)
    print("*" * 60 + "\n")

def report_menu(dic_orders):
    print("\n" + "=" * 40)
    print(" REPORT MENU ".center(40, "="))
    print("=" * 40)
    print("1. Customer report")
    print("2. General report")
    print("=" * 40)

    a = 1
    while a == 1:
        option = input("\nChoose an option: ")

        if option == "1":
            final_generation(dic_orders)
            a = 2

        elif option == "2":
            final_report(dic_orders)
            a = 2

        else:
            print("Invalid option, try again.")
            print("*" * 40)
