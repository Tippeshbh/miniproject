# Bank Account Management System (Mini Project)

This is a simple **Bank Account Management System** built using **Python and Object-Oriented Programming (OOP)** concepts.

The project demonstrates real-world banking operations such as creating accounts, depositing money, withdrawing money, and checking balances.

---

## Features

- Create Savings and Current accounts
- Deposit money
- Withdraw money
- Check account balance
- Interest calculation for Savings Account
- Overdraft facility for Current Account

---

## OOP Concepts Used

### 1. Encapsulation
- Balance is stored as a protected variable `_balance`

### 2. Inheritance
- `SavingsAccount` and `CurrentAccount` inherit from `Account` class

### 3. Polymorphism
- Withdraw method is overridden in `CurrentAccount`

### 4. Abstraction
- Bank class manages account creation and access

---

## Classes

### Account
- Create account
- Deposit money
- Withdraw money
- Check balance

### SavingsAccount
- Calculate interest

### CurrentAccount
- Withdraw with overdraft limit

### Bank
- Create accounts
- Store accounts
- Get account details

---

## Example Output
