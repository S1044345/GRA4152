
# Create a customer class to handle a customer loyalty marketing campaign
# After 100 usd purchases, the customer will receive a 10 usd discount on the next purchase

class Customer:

    _customerID = 0 #A class variable for each customer
    Discount = 10 #A class constant for the discount

    #Constructs a customer class with accumulated purchases amount
    def __init__ (self):
        self._totalpurchases = 0
        self._discountearned = 0

        Customer._customerID = Customer._customerID + 1
        

    #method that increases the total purchases amount
    def makePurchase (self, amount):
        self._totalpurchases += amount
        

    #method that will check if the total purchases amount is greater than 100 usd
    def discountReached (self):
        if self._totalpurchases >= 100:
            self._discountearned = (self._totalpurchases // 100)*10
        return self._discountearned
    
    #method that gets the total purchases
    def getTotalpurchases (self):
        return self._totalpurchases

