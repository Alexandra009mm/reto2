from register import register
from add_product import add_product
from create_orders import creation_orders
from show_total import d_calculation
from final_report import report_menu
from order_consultation import order_consultation

dic_customers = {}
dic_product = {}
dic_orders ={}

print("""
                 ╔════════════════════════════╗
------------------Welcome to the sales register -----------------------
                 ╚════════════════════════════╝
\n""")

option = 0
while option != 7:
        try: 
            option = int(input(f"""\n
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
                    register(dic_customers)

            elif option == 2:
                    add_product(dic_product)

            elif option == 3:
                    creation_orders(dic_customers,dic_product,dic_orders)

            elif option == 4:
                    order_consultation(dic_orders)

            elif option == 5:
                    d_calculation(dic_orders)

            elif option == 6:
                    report_menu(dic_orders)

            elif option == 7:
                   print("thank you for using the program :)")

            else:
                    print("Invalid option, try again.")
                    continue
            
        except ValueError:
                print("Enter the option number")
                continue

print("thank you for using the program :)")
                
                
                
        


