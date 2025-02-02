class InsufficientFundsError(Exception):
    pass


class Account:
    def __init__(self, account_number: str, owner: str, balance: float = 0.0):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance

    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        
        self.balance += amount

    def withdraw(self, amount: float):
        if amount > self.balance:
            raise InsufficientFundsError("Insufficient funds.")
        
        self.balance -= amount

    async def transfer(self, to_account, amount: float):
        if amount > self.balance:
            raise InsufficientFundsError("Insufficient funds.")
        
        await self._simulate_async_operation()
        self.withdraw(amount)
        to_account.deposit(amount)

    async def _simulate_async_operation(self):
        import asyncio
        await asyncio.sleep(0.5)


class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number: str, owner: str, initial_balance: float):
        if account_number in self.accounts:
            raise ValueError(f"Account with number {account_number} already exists.")
        
        new_account = Account(account_number, owner, initial_balance)
        self.accounts[account_number] = new_account
        
        return new_account

    def get_account(self, account_number: str):
        if account_number not in self.accounts:
            raise ValueError(f"Account {account_number} does not exist.")
        
        return self.accounts[account_number]

    async def process_transaction(self, transaction_func):
        await transaction_func()
