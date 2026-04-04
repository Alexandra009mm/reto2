def order_consultation(dic_orders):
    keep_register = "yes"

    while keep_register == "yes":

        print("\n" + "=" * 50)
        print("         ORDER CONSULTATION")
        print("=" * 50)

        try:
            ask_Id = int(input("Enter your ID: "))

        except ValueError:
            print("Error, enter your numeric ID")
            print("*" * 50)
            continue

        print("-" * 50)

        if ask_Id not in dic_orders:
            print("The customer has not placed any orders.")
            print("*" * 50)
            keep_register = "no"

        else:
            my_order = dic_orders[ask_Id]

            print(f"\nORDER DETAILS (ID: {ask_Id})")
            print("-" * 50)

            for i in my_order:
                for k, v in i.items():
                    print(f"{k}: {v}")
                print("-" * 50)

            keep_register = "no"

    return