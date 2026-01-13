class BankError(Exception):
    pass

class AccountNotFoundError(BankError):
    pass

class InsufficientBalanceError(BankError):
    pass

class InvalidAmountError(BankError):
    pass


from datetime import datetime

class Account:

    account_counter = 1085

    def __init__(self,acc_holder):

        Account.account_counter += 1
        self.acc_num = Account.account_counter
        self.acc_holder = acc_holder
        self._balance = 0
        self.tra_history = []

    def deposit(self,amount):

        if amount < 0:
            raise InvalidAmountError('Amount must be positive')
        self._balance += amount
        self.tra_history.append(f'Deposited: ${amount} {datetime.now().strftime("%H:%M:%S")}')
        return True
    
    def withdraw(self,amount):

        if self._balance < amount:
             raise InsufficientBalanceError('Not enough balance')
        if amount < 0:
            raise InvalidAmountError('Amount must be positive')
        self._balance -= amount
        self.tra_history.append(f'Withdrawn: ${amount} {datetime.now().strftime("%H:%M:%S")}')
        return True
    
    def check_balance(self):
        return f'Balance: {self._balance}'
    
    def display_transactions(self):
        
        if self.tra_history == []:
            return False
        return self.tra_history
    
    def __str__(self):
        return f'Account holder: {self.acc_holder} Account number: {self.acc_num} Balance: {self._balance}'
    
class SavingsAccount(Account):

    min_balance = 200

    def __init__(self, acc_holder):
        super().__init__(acc_holder)
        self.interest = 1.05

    def apply_interest(self):
        
        if self._balance >= SavingsAccount.min_balance:
            interest_earned = (self._balance * self.interest) - self._balance
            self._balance *= self.interest
            self.tra_history.append(f'Interest earned of ${interest_earned}')
        else:
            penalty_fee = 10
            self._balance -= penalty_fee
            self.tra_history.append(f'Penaly fee of ${penalty_fee} was deducted')
        
class CheckingAccount(Account):

    def __init__(self, acc_holder):
        super().__init__(acc_holder)
        self.overdraft_limit = 500

    def withdraw(self, amount):

        if amount > self._balance + self.overdraft_limit:
            raise InsufficientBalanceError('Not enough balance')

        if amount <= self._balance:
            self._balance -= amount
            self.tra_history.append(f'Witrhdrawed: ${amount} {datetime.now().strftime("%H:%M:%S")}')
        else:
            overdraft_used = amount - self._balance
            self._balance = 0
            self.overdraft_limit -= overdraft_used
            self.tra_history.append(f'Withdrawn using overdraft: ${amount} {datetime.now().strftime("%H:%M:%S")}')
        return True
    
    def display_overdraft(self):
        return f'overdraft amount: {self.overdraft_limit}'
    
class Bank:

    def __init__(self,bank_name):
        self.name = bank_name
        self.accounts = {}

    def add_accounts(self,account):
        self.accounts[account.acc_num] = account

    def get_account(self,acc_num):
        return self.accounts.get(acc_num)
    
    def transfer(self,from_acc_num,to_acc_num,amount):
        
        sender = self.get_account(from_acc_num)
        receiver = self.get_account(to_acc_num)

        if not sender or not receiver:
            raise AccountNotFoundError('Account not found')
        
        if amount > sender._balance:
            raise InsufficientBalanceError('Insufficient balance for transfer')
        
        sender._balance -= amount
        receiver._balance += amount 

        sender.tra_history.append(f'Transferred ${amount} to {to_acc_num} {datetime.now().strftime("%H:%M:%S")}')

        receiver.tra_history.append(f'Received ${amount} from {from_acc_num} {datetime.now().strftime("%H:%M:%S")}')

        return True