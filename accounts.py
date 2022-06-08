# Andrew Frisby
import random
import datetime



class BasicAccount:
    """
    A class for basic bank accounts. Basic accounts can not be overdrawn. Further information can be found in the
    docstrings for each individual method. 

    As a note, when any monetary amount is printed, it is rounded to 2 decimal places for clarity and readability.
    The amount is not actually rounded when doing any transactional computations. 

    Attributes:
        name: str
            Full name of account holder
        balance: float
            Amount of money in account, in pounds
        acNum: int
            Account number, unique number, autogenerated upon initialization
        cardNum: str
            If a card is issued, the 16-digit card number
        cardExp: tuple (int, int)
            If a card is issued, the expiration date for the card in (month, year) format. 
            E.g., January 2024 = (1, 24)
    """

    # account number counter that will be incremented and assigned when an account is initialized
    account_num = 0 

    @classmethod 
    def openAccount(cls): 
        """
        openAccount will increment the account_num variable and assign it as a new account's account number.
        This function is called in the __init__ function.

        Parameters:
            None
        
        Return:
            Nothing
        """

        BasicAccount.account_num += 1

    def __init__(self, theAcName, theOpeningBalance):
        """
        The initializer initializes the basic account with an opening account balance and the account holder's name.
        It also calls the openAccount() class method to assign account_num to acNum for each new account.

        Parameters:
            theAcName: string - Account holder's full name
            theOpeningBalance: float - Amount of money deposited into the account upon creation, in pounds
        
        Return:
            Nothing
        """

        self.balance = theOpeningBalance
        self.name = theAcName
        self.openAccount()
        self.acNum = BasicAccount.account_num


    def __str__(self):
        """
        String method ensures when an account is printed, a print statement with 
        the account holder's name and available balance is returned as a string

        Parameters:
            None
        
        Return:
            String with account holder's name and available balance
        """

        return f'Account Name: {self.name}, Available balance: £{round(self.balance, 2)}'
    
    def __del__(self):
        """
        __del__ will run the closeAccount() function which will do the required housekeeping before an account can
        be closed

        Parameters:
            None
        
        Return:
            Boolean - True for account that is in good standing and can be closed, False for premium account that is 
            overdrawn and cannot be closed. False can not be returned for basic account
        """

        self.closeAccount()
    
    def deposit(self, amount):
        """
        deposit will deposit the amount into the relevant account and print a statement of confirmation

        Parameters:
            amount: float - the amount to be deposited. Must be positive integer.
        
        Return:
            Nothing
        """

        # Safeguarding input to ensure positive float/integer - use this throughout the other functions
        try:
            flt_amount = float(amount)

        except ValueError:
            print('Not a number. Try again.')
        
        else:    
            if flt_amount < 0.0:
                print('Negative input not allowed.')
            
            else:
                self.balance += flt_amount
                print(f'New balance is: £{round(self.balance, 2)}')
    
    def withdraw(self, amount):
        """
        withdraw will withdraw the amount from the relevant account and print a statement of confirmation

        Parameters:
            amount: float - the amount to be withdrawn. Must be positive integer/float that is 
            less than or equal to the account's balance.
        
        Return:
            Nothing
        """

        try: 
            flt_amount = float(amount)
        
        except ValueError:
            print('Not a number. Try again.')

        else:
            if flt_amount < 0.0:
                print('Negative input not allowed.')
            
            elif flt_amount > self.balance:
                print(f'Can not withdraw £{flt_amount}')
           
            else:
                self.balance -= flt_amount
                print(f'{self.name} has withdrawn £{flt_amount}. New balance is £{round(self.balance, 2)}')

    def getAvailableBalance(self):
        """
        getAvailableBalance will return the relevant account's balance in addition to any 
        available overdraft. No overdraft for basic accounts.

        Parameters:
            None
        
        Return:
            balance: float - the account's balance (no overdraft for basic accounts)
        """

        return float(self.balance)
    
    def getBalance(self):
        """
        getBalance will return the relevant account's balance

        Parameters:
            None
        
        Return:
            balance: float - the account's balance
        """

        return float(self.balance)
    
    def printBalance(self):
        """
        printBalance will print the relevant account's balance 

        Parameters:
            None
        
        Return:
            Nothing
        """

        print(f'{self.name} has a balance of: £{round(self.balance, 2)}')
    
    def getName(self):
        """
        getName will return the account holder's name as a string

        Parameters:
            None
        
        Return:
            name: string - the account holder's name
        """

        return f'{self.name}'
    
    def getAcNum(self):
        """
        getAcNum will return the 16 digit account number associated with the account as a string

        Parameters:
            None
        
        Return:
            acNum: string - the account number
        """

        return f'{self.acNum}'

    def issueNewCard(self):
        """
        issueNewCard will generate a randomized 16 digit card number (cardNum) and 
        an expiration date 3 years into the future from the date the function is called (cardExp).
        The cardNum will be a string and the cardExp will be a tuple of 2 integers (month, 2-digit year).

        Parameters:
            None
        
        Return:
            Nothing
        """

        exp_year = datetime.datetime.now().year + 3
        month = datetime.datetime.now().month
        self.cardExp = (month, int(str(exp_year)[2:]))
        
        # empty string that will be populated with randomized digits
        card_num = ''

        # random digit generator for new card
        for i in range(0, 16):
            x = str(random.randint(0,9))
            card_num += x
        
        self.cardNum = card_num
    
    def closeAccount(self): 
        """
        closeAccount will withdraw the remaining balance from the basic account it is called on and then return True. 
        Function will always return True for basic accounts because they can not be overdrawn.
        This function is run in the __del__ function.

        Parameters:
            None
        
        Return:
            Boolean - True for account that is in good standing and can be closed, False can not be returned here
        """

        self.withdraw(self.balance)
        print('Closing account.')
        return True



class PremiumAccount(BasicAccount):
    """
    A subclass for premium bank accounts. It inherits and overrides functions from its parent class, BasicAccount.
    Premium bank accounts can be overdrawn. Further information can be found in the docstrings for each individual method. 

    As a note, when any monetary amount is printed, it is rounded to 2 decimal places for clarity and readability.
    The amount is not actually rounded when doing any transactional computations. 

    Attributes:
        name: str
            Full name of account holder
        balance: float
            Amount of money in account, in pounds
        acNum: int
            Account number, unique number, autogenerated upon initialization
        overdraftLimit: float
            Overdraft limit for the premium account, in pounds
        overdraft: boolean
            True if account is overdrawn (i.e., negative balance), False if account is not and in good standing
        cardNum: str
            If a card is issued, the 16-digit card number
        cardExp: tuple (int, int)
            If a card is issued, the expiration date for the card in (month, year) format. 
            E.g., January 2024 = (1, 24)
    """

    def __init__(self, theAcName, theOpeningBalance, theInitialOverdraft):
        """
        The initializer initializes the premium account with an opening account balance, the account holder's name,
        and an initial overdraft limit. Similar to the basic account, it also calls the openAccount() class method
        to assign account_num to acNum for each new account. The function will also set the account's overdraft
        boolean variable to False because the account must be opened with a positive amount, and therefore, will
        not be overdrawn. 

        Parameters:
            theAcName: string - Account holder's full name
            theOpeningBalance: float - Amount of money deposited into the account upon creation, in pounds
            theInitialOverdraft: float - Overdraft limit for the account, in pounds
        
        Return:
            Nothing
        """

        super().__init__(theAcName, theOpeningBalance)
        self.overdraftLimit = theInitialOverdraft
        self.overdraft = False


    def __str__(self):
        """
        String method ensures when an account is printed, a print statement with 
        the account holder's name, available balance, and overdraft limit is returned as a string

        Parameters:
            None
        
        Return:
            String with account holder's name, available balance, and overdraft limit
        """

        return f'Premimum Account Name: {self.name}, Available balance: £{round(self.balance, 2)}, Overdraft Limit: £{self.overdraftLimit}, Currently Overdraft? {self.overdraft}'

    def setOverdraftLimit(self, newLimit):
        """
        setOverdraftLimit will set a new overdraft limit for the premium account

        Parameters:
            newLimit: float - the new overdraft limit
        
        Return:
            Nothing
        """

        self.overdraftLimit = newLimit
    
    def getAvailableBalance(self):
        """
        getAvailableBalance will return the relevant account's balance in addition to any 
        available overdraft.

        Parameters:
            None
        
        Return:
            balance + overdraftLimit: float - the account's balance and overdraft limit summed 
        """

        return super().getAvailableBalance() + self.overdraftLimit 
    
    def printBalance(self):
        """
        printBalance will print the relevant account's balance and any overdraft available

        Parameters:
            None
        
        Return:
            Nothing
        """

        super().printBalance() 
        
        if self.overdraft:
            print(f'Overdraft available: £{self.balance + self.overdraftLimit}')
        
        else:
            print(f'Overdraft available: £{self.overdraftLimit}')
    
    def deposit(self, amount):
        """
        deposit will deposit the amount into the relevant account and print a statement of confirmation.
        If the account repays an overdraft, will also change overdraft to False.

        Parameters:
            amount: float - the amount to be deposited. Must be positive integer.
        
        Return:
            Nothing
        """

        super().deposit(amount)
        
        # checking if account was previously overdrawn and has now repayed the overdraft, if so, setting overdraft to False
        if self.overdraft and self.balance > 0.0:
            self.overdraft = False

    def withdraw(self, amount):
        """
        withdraw will withdraw the amount from the relevant account and print a statement of confirmation.
        If withdrawal uses overdraft, will set overdraft to True.

        Parameters:
            amount: float - the amount to be withdrawn. Must be positive integer/float that is 
            less than or equal to the account's balance + overdraft limit.
        
        Return:
            Nothing
        """

        try:
            flt_amount = float(amount)
        
        except ValueError:
            print('Not a number. Try again.')
        
        else:
            if flt_amount < 0.0:
                print('Negative input not allowed.')
                
            elif flt_amount > (self.balance + self.overdraftLimit):
                print(f'Can not withdraw £{flt_amount}')
                    
            else:
                self.balance -= flt_amount
                
                # checking if withdraw used overdraft, if so changing overdraft to True
                if self.balance < 0.0:
                    self.overdraft = True

                print(f'{self.name} has withdrawn £{round(flt_amount, 2)}. New balance is £{round(self.balance, 2)}')

    def closeAccount(self): 
        """
        If the account has a positive balance, closeAccount will withdraw the remaining balance 
        from the account it is called on and then return True by running the function from the parent class.
        If the account has a negative balance (i.e., is overdrawn), close account will print a message saying 
        that is unable to close account because of the negative balance and then return False.
        This function is run in the __del__ function.

        Parameters:
            None
        
        Return:
            Boolean - True for account that is in good standing and can be closed,
            False for account that is overdrawn and cannot be closed. 
        """

        if self.overdraft:
            print(f'Can not close account due to customer being overdrawn by £{round(self.balance, 2)}')
            return False
        
        else:
            super().closeAccount()
