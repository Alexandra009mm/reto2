def creation_orders(dic_customers, dic_product, dic_orders):
    keep_register = "yes"

    while keep_register == "yes":
        print("\n" + "=" * 50)
        print("              CREATE ORDER")
        print("=" * 50)

        a = 1
        while a == 1:
            try:
                ask_Id = int(input("\nEnter your ID: "))
                if ask_Id <= 0:
                    print("Enter valid ID :/")
                    print("*" * 50 + "\n")
                    continue
                else:
                    a = 2
            except ValueError:
                print("Error, enter your numeric ID")
                print("*" * 50 + "\n")
                continue

        print("-" * 50)

        if ask_Id in dic_customers:

            print("AVAILABLE PRODUCTS")
            print("-" * 50)

            for key_product, value in dic_product.items():
                print(f"Product ID: {key_product} | Product: {value[0]} | Price: {value[1]}")
            
            print("-" * 50)

            b = 1
            while b == 1:
                try:
                    order_product = int(input("Enter the product ID you want to order: "))
                    if order_product <= 0:
                        print("Enter valid product ID :/")
                        print("*" * 50 + "\n")
                        continue
                    else:
                        b = 2
                except ValueError:
                    print("Enter a valid number")
                    print("*" * 50 + "\n")
                    continue

            print("-" * 50)

            if order_product in dic_product:

                c = 1
                while c == 1:
                    try:
                        quantity = int(input("Enter the quantity: "))
                        if quantity <= 0:
                            print("Invalid quantity :/")
                            print("*" * 50 + "\n")
                            continue
                        else:
                            c = 2
                    except ValueError:
                        print("Enter a valid number")
                        print("*" * 50 + "\n")
                        continue

                subtotal = dic_product[order_product][1] * quantity

            else:
                print("Product ID not found")
                print("*" * 50)
                keep_register = "no"
                break

            print("-" * 50)

            d = "yes"
            while d == "yes":
                confirmation = input("Are you sure you want to place this order? yes/no: ").lower().strip()

                if confirmation == "yes":
                    dic_new_orders = {
                        "customer": dic_customers[ask_Id]["name"],
                        "product": dic_product[order_product][0],
                        "quantity": quantity,
                        "subtotal": subtotal
                    }

                    if ask_Id not in dic_orders:
                        dic_orders[ask_Id] = ()

                    dic_orders[ask_Id] = dic_orders[ask_Id] + (dic_new_orders,)

                    print("\n" + "=" * 50)
                    print("        ORDER SUCCESSFULLY PLACED! :)")
                    print("=" * 50)

                    e = 1
                    while e == 1:
                        ans = input("Do you want to add another order? yes/no: ").lower().strip()

                        if ans == "yes":
                            keep_register = "yes"
                            e = 2
                        elif ans == "no":
                            keep_register = "no"
                            e = 2
                        else:
                            print("Error, answer must be yes or no.")

                    d = "no"

                elif confirmation == "no":
                    print("OK, order cancelled")
                    d = "no"
                    keep_register = "no"

                else:
                    print("Error, answer yes or no.")

        else:
            print("User ID not found.")
            keep_register = "no"

    return dic_orders