## 
#  This program tests the Customer class.
#
def Customerdemo():
    import argparse 
    import textwrap
    from Customer import Customer

    parser = argparse.ArgumentParser(prog='Customer discount program',
                                    formatter_class=argparse.RawDescriptionHelpFormatter,
                                    description=textwrap.dedent('''\
                                                 Customer Loyalty Marketing Campaign
                                     ------------------------------------------------------------------------------------------
                                     A track of customer purchases and the total discount they have earned 

                                     Methods:
                                     1) makePurchase: Adds an amount of the purchase to the total amount of purchases of the customer
                                        @param price of the purchase

                                     2) discountReached: Checks if the total amount of purchases is greater than 100 USD which will be eligible for a 10 USD discount.
                                        @return the total amount of discounts earned

                                     3) getTotalpurchases: Gets the number of items in the current sale.
                                        @return the total amount of purchases made
                                     '''),
                                    epilog=textwrap.dedent('''\
                                                Usage
                                     --------------------------------
                                      customer1 = Customer() # initialize an object
                                      customer1.makePurchase(50) # add an item
                                      customer1.getTotalpurchases # prints out the total amount purchased
                                     ''')
                    )

    parser.add_argument('--init_amount', default=0.0, type=float)
    parser.add_argument('--run_demo', action='store_true', help='runs this program')

    args = parser.parse_args()

    if args.run_demo:
        customer1 = Customer()
        customer1.makePurchase(50)
        customer1.makePurchase(50)
        print(customer1.discountReached())
        print("Expected: 10")
        customer1.makePurchase(50)
        print(customer1.discountReached())
        print("Expected: 10")
        customer1.makePurchase(80)
        print(customer1.discountReached())
        print("Expected: 20")

if __name__ == '__main__':
    Customerdemo()