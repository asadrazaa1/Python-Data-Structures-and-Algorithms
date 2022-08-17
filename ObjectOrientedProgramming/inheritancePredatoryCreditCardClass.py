class CreditCard():
    """
    A consumer of credit card
    """

    def __init__(self, customer, bank, acnt, limit) -> None:
        """”””Create a new credit card instance.
        The initial balance is zero.
        
        customer the name of the customer (e.g., John Bowman )
        bank the name of the bank (e.g., California Savings )
        acnt the acount identifier (e.g., 5391 0375 9387 5309 )
        limit credit limit (measured in dollars)"""

        self._customer = customer
        self._bank = bank
        self._acnt = acnt
        self._limit = limit
        self._balance = 0
    
    def get_customer(self):
        """Return name of the customer"""
        return self._customer

    def get_account(self):
        """Return account identifier"""
        return self._acnt
    
    def get_bank(self):
        """Return name of the bank"""
        return self._bank

    def get_limit(self):
        """Return credit card limit"""
        return self._limit

    def get_balance(self):
        """Return customer balance"""
        return self._balance

    def charge(self, price):
        """Charge given price to the card, assuming sufficient credit card limit.
        Return True if charge was processed else return False"""

        if price + self._balance > self._limit:# if charge would exceed limit,
            return False                       #cannot accept charge
        self._balance += price
        return True
    
    def make_payment(self, amount):
        """Process customer payment that reduces balance"""
        self._balance -= amount


class PredatoryCreditCard(CreditCard):
    """An extension of the CreditCard that compounds interests and fees."""

    def __init__(self, customer, bank, acnt, limit, apr) -> None:
        """Create a new predatory credit card instance.
        
        The initial balance is zero.

        customer    the name of the customer (e.g., John Bowman )
        bank        the name of the bank (e.g., California Savings )
        acnt        the acount identifier (e.g., 5391 0375 9387 5309 )
        limit       credit limit (measured in dollars)
        apr         annual percentage rate (e.g., 0.0825 for 8.25% APR)

        """
        super().__init__(customer, bank, acnt, limit) # call super constructor
        self._apr = apr
    
    def charge(self, price):
        """Charge given price to the card, assuming sufficient credit card limit.
        
        Return True if charge was processed.
        Return False and assess $5 if charge was denied
        """
        success = super().charge(price)             # call inherited method

        if not success:
            self._balance += 5                      # asses penalty
        return success                              # caller expects return value

    def process_month(self):
        """Assess monthly interest on the outstanding balance."""

        if self._balance > 0:
            # if positive balance, convert APR to monthly multiplicative factor
            monthly_factor = pow(1+self._apr, 1/12)
            self._balance *= monthly_factor
            



# if __name__ == '__main__' :
#     wallet = [ ]
#     wallet.append(CreditCard( "John Bowman" , "California Savings" ,
#     "5391 0375 9387 5309", 2500) )
#     wallet.append(CreditCard( "John Bowman" , "California Federal" ,
#     "3485 0399 3395 1954", 3500) )
#     wallet.append(CreditCard( "John Bowman" , "California Finance" ,
#     "5391 0375 9387 5309", 5000) )

#     for val in range(1, 17):
#         wallet[0].charge(val)
#         wallet[1].charge(2*val)
#         wallet[2].charge(3*val)

#     for c in range(3):
#         print(" Customer = ", wallet[c].get_customer())
#         print(" Bank = ", wallet[c].get_bank())
#         print(" Account = ", wallet[c].get_account())
#         print(" Limit = ", wallet[c].get_limit())
#         print(" Balance = ", wallet[c].get_balance())
#         while wallet[c].get_balance( ) > 100:
#             wallet[c].make_payment(100)
#             print(" New balance = ", wallet[c].get_balance())
#         print( )