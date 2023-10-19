## 
#  This program tests the Country class.
#
def Countrydemo():
    import argparse 
    import textwrap
    from Country import Country

    parser = argparse.ArgumentParser(prog='Country test program',
                                    formatter_class=argparse.RawDescriptionHelpFormatter,
                                    description=textwrap.dedent('''\
                                                        Countries
                                     ------------------------------------------------------------------------------------------
                                     Stores the name of the country, its population, its area, and calculates the country's density. 

                                     Methods:
                                     1) largestArea_list: finds the country with the largest area from a list
                                        @return the country with the largest area

                                     2) largestArea_dict: finds the country with the largest area from a dictionary
                                        @return the country with the largest area

                                     3) largestPop_list: finds the country with the largest population from a list
                                        @return the country with the largest population
                                                                
                                     4) largestPop_dict: finds the country with the largest population from a dictionary
                                        @return the country with the largest population
                                        
                                     3) largestDen_list: finds the country with the largest density from a list
                                        @return the country with the largest density
                                                                
                                     3) largestDen_dict: finds the country with the largest density from a dictionary
                                        @return the country with the largest density
                                     '''),
                                    epilog=textwrap.dedent('''\
                                                Usage
                                     --------------------------------
                                      canada = Country("Canada",1200000,1500) # initialize an object
                                      largest_area_country_list = Country.largestArea_list() # returns the country with the largest area from a list
                                      largest_area_country_list = Country.largestArea_dict() # returns the country with the largest area from a dictionary
                                     ''')
                    )

    parser.add_argument('--init_country', default= " ", type=str)
    parser.add_argument('--init_pop', default=0.0, type=float)
    parser.add_argument('--init_area', default=0.0, type=float)
    parser.add_argument('--run_demo', action='store_true', help='runs this program')

    args = parser.parse_args()

    if args.run_demo:
        canada = Country("Canada",1200000,1500)
        philippines = Country("Philippines",1000000,1200)
        us = Country("USA",20000000,1000)


        largest_area_country_list = Country.largestArea_list()
        largest_area_country_dict = Country.largestArea_dict()
        print(largest_area_country_list,largest_area_country_dict)
        print("Expected: us")

        largest_pop_country_list = Country.largestPop_list()
        largest_pop_country_dict = Country.largestPop_dict()
        print(largest_pop_country_list,largest_pop_country_dict)
        print("Expected: us")

        largest_dense_country_list = Country.largestDen_list()
        largest_dense_country_dict = Country.largestDen_dict()
        print(largest_dense_country_list,largest_dense_country_dict)
        print("Expected: us")

if __name__ == '__main__':
    Countrydemo()









