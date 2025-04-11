"""
2043. Simple Bank System
You have been tasked with writing a program for a popular bank that will automate all its incoming transactions (transfer, deposit, and withdraw). The bank has n accounts numbered from 1 to n. The initial balance of each account is stored in a 0-indexed integer array balance, with the (i + 1)th account having an initial balance of balance[i].

Execute all the valid transactions. A transaction is valid if:

The given account number(s) are between 1 and n, and
The amount of money withdrawn or transferred from is less than or equal to the balance of the account.
Implement the Bank class:

Bank(long[] balance) Initializes the object with the 0-indexed integer array balance.
boolean transfer(int account1, int account2, long money) Transfers money dollars from the account numbered account1 to the account numbered account2. Return true if the transaction was successful, false otherwise.
boolean deposit(int account, long money) Deposit money dollars into the account numbered account. Return true if the transaction was successful, false otherwise.
boolean withdraw(int account, long money) Withdraw money dollars from the account numbered account. Return true if the transaction was successful, false otherwise.


Example 1:

Input
["Bank", "withdraw", "transfer", "deposit", "transfer", "withdraw"]
[[[10, 100, 20, 50, 30]], [3, 10], [5, 1, 20], [5, 20], [3, 4, 15], [10, 50]]
Output
[null, true, true, true, false, false]

Explanation
Bank bank = new Bank([10, 100, 20, 50, 30]);
bank.withdraw(3, 10);    // return true, account 3 has a balance of $20, so it is valid to withdraw $10.
                         // Account 3 has $20 - $10 = $10.
bank.transfer(5, 1, 20); // return true, account 5 has a balance of $30, so it is valid to transfer $20.
                         // Account 5 has $30 - $20 = $10, and account 1 has $10 + $20 = $30.
bank.deposit(5, 20);     // return true, it is valid to deposit $20 to account 5.
                         // Account 5 has $10 + $20 = $30.
bank.transfer(3, 4, 15); // return false, the current balance of account 3 is $10,
                         // so it is invalid to transfer $15 from it.
bank.withdraw(10, 50);   // return false, it is invalid because account 10 does not exist.


Constraints:

n == balance.length
1 <= n, account, account1, account2 <= 105
0 <= balance[i], money <= 1012
At most 104 calls will be made to each function transfer, deposit, withdraw.
"""


class Bank:
    def __init__(self, balance: list[int]) -> None:
        self._balance = [0] + balance
        self._balance_temp = 0

    def is_valid_account(self, account: int) -> bool:
        return 1 <= account <= len(self._balance)

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if not self.is_valid_account(account1) and not self.is_valid_account(account2):
            print("Invalid accounts.")
            return False

        current_balance = self._balance[account1]
        if current_balance < money:
            print("Insufficient funds.")
            return False

        if money < 0:
            print("Transfer amount must be positive")
            return False

        print(f"Transfering ${money} from account {account1} to account {account2}")
        self.withdraw(account1, money)
        self.deposit(account2, money)
        print(f"Transferred ${money} from account {account1} to account {account2}")
        return True

    def deposit(self, account: int, money: int) -> bool:
        if not self.is_valid_account(account):
            print("Invalid account.")
            return False

        if money < 0:
            print("Deposit amount must be positive")
            return False

        print(f"Depositing ${money} to account {account}")
        self._balance[account] += money
        print(f"Deposited ${money} to account {account}")
        return True

    def withdraw(self, account: int, money: int) -> bool:
        if not self.is_valid_account(account):
            print("Invalid account.")
            return False

        if self._balance[account] < money:
            print("Insufficient funds.")
            return False

        if money < 0:
            print("Withdrawal amount must be positive")
            return False

        print(f"Withdrawing ${money} from account {account}")
        self._balance[account] -= money
        print(f"Withdrawn ${money} from account {account}")
        return True


if __name__ == "__main__":
    bank = Bank([10, 20, 30])
    # Testing withdrawals with negative amount
    bank.withdraw(account=1, money=-1)
    # Testing succesful withdraw
    bank.withdraw(account=1, money=10)
    # Testing deposit with fake account
    bank.deposit(account=0, money=10)
    # Testing successful deposit
    bank.deposit(account=1, money=10)
    # Transfering from fake account
    bank.transfer(account1=0, account2=1, money=10)
    # Transfering from account with insufficient funds
    bank.transfer(account1=1, account2=2, money=100)
    # Successful transfer
    bank.transfer(account1=1, account2=2, money=10)
