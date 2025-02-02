import pytest
import pytest_asyncio
from unittest.mock import AsyncMock
from bank_system import Account, Bank, InsufficientFundsError


@pytest.fixture
def account_fixture():
    return Account(account_number="12345", owner="John Doe", balance=100.0)

@pytest.fixture
def bank_fixture():
    return Bank()

def test_deposit(account_fixture):
    account_fixture.deposit(50.0)
    assert account_fixture.balance == 150.0

def test_withdraw_success(account_fixture):
    account_fixture.withdraw(50.0)
    assert account_fixture.balance == 50.0

def test_withdraw_insufficient_funds(account_fixture):
    with pytest.raises(InsufficientFundsError):
        account_fixture.withdraw(150.0)

@pytest_asyncio.fixture
async def async_transfer_setup():
    account1 = Account(account_number="12345", owner="John", balance=100.0)
    account2 = Account(account_number="67890", owner="Jane", balance=50.0)
    return account1, account2

@pytest.mark.asyncio
async def test_transfer_success(async_transfer_setup):
    account1, account2 = async_transfer_setup
    await account1.transfer(account2, 50.0)
    assert account1.balance == 50.0
    assert account2.balance == 100.0

@pytest.mark.asyncio
async def test_transfer_insufficient_funds(async_transfer_setup):
    account1, account2 = async_transfer_setup
    with pytest.raises(InsufficientFundsError):
        await account1.transfer(account2, 200.0)

def test_create_account(bank_fixture):
    account = bank_fixture.create_account("11111", "Alice", 500.0)
    assert account.account_number == "11111"
    assert account.owner == "Alice"
    assert account.balance == 500.0

def test_get_account(bank_fixture):
    bank_fixture.create_account("22222", "Bob", 300.0)
    account = bank_fixture.get_account("22222")
    assert account.owner == "Bob"

def test_get_account_non_existent(bank_fixture):
    with pytest.raises(ValueError):
        bank_fixture.get_account("99999")

@pytest.mark.asyncio
async def test_process_transaction_mocked(bank_fixture):
    mock_transaction = AsyncMock()
    await bank_fixture.process_transaction(mock_transaction)
    mock_transaction.assert_awaited_once()
