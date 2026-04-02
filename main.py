from fuunciones import *

dic_clientes = {}
dic_product = {}
dic_orders ={}

print("\n")
print("""
                 ╔════════════════════════════╗
------------------Welcome to the sales register -----------------------
                 ╚════════════════════════════╝
\n""")

keep_register = "yes"
while keep_register == "yes":
        try: 
            option = int(input(f"""
        -------------------------------------------------------------
        ╔════════════════════════════╗
                    MENU
        ╚════════════════════════════╝
        1. register.
        2. add product.
        3. add order.
        4. Registered Order Consultation.
        5. Daily Income Calculation. 
        6. Final Report Generation.
        7. Exit.
        --------------------------------------------------------------                   
        enter a option => """))
            
            if option == 1:
                    register(dic_clientes)

            elif option == 2:
                    add_product(dic_product)

            elif option == 3:
                    creation_orders(dic_clientes,dic_product,dic_orders)

            elif option == 4:
                    order_consultation(dic_orders)

            elif option == 5:
                    print()

            elif option == 6:
                    print()

            elif option == 7:
                   keep_register = "no"

            else:
                    print("Error, option invalide, try again")
                    continue
            
        except ValueError:
                print("Enter the option number")
                continue

print("thank you for using the program :)" \
"")
                
                
                
        


