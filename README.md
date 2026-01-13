# 🏦 Core Banking System (Python OOP + CLI)

A **Python-based core banking system** built to practice **Object-Oriented Programming (OOP)** concepts and design a real-world inspired **command-line interface (CLI)** application.

This project simulates essential banking operations such as account creation, deposits, withdrawals, fund transfers, overdraft handling, and transaction history tracking.

---

## 🚀 Features

- Object-Oriented design with clean class separation
- Savings and Checking account support
- Custom exception handling for banking errors
- Menu-driven CLI interface
- Account-to-account money transfer
- Transaction history with timestamps
- Overdraft facility for checking accounts
- Interest and penalty logic for savings accounts

---

## 🧠 Concepts Used

- Classes & Objects
- Inheritance and Method Overriding
- Encapsulation
- Custom Exceptions
- CLI-based user interaction
- Real-world domain modeling

---

## 📁 Project Structure

```
core_banking_system/
├── bank.py
├── main.py
├── README.md
└── .gitignore
```


---

## 🏦 Account Types

### 🔹 Account
Base class providing common banking functionality:
- Deposit
- Withdraw
- Balance inquiry
- Transaction history

### 🔹 SavingsAccount
- Minimum balance requirement
- Interest calculation
- Penalty if balance falls below minimum

### 🔹 CheckingAccount
- Overdraft limit support
- Withdrawals using overdraft balance

---

## ⚠️ Custom Exceptions

The system uses custom exceptions for safe and clear error handling:
- `AccountNotFoundError`
- `InsufficientBalanceError`
- `InvalidAmountError`

---

## 🖥️ CLI Operations

Users can:
1. Create savings or checking accounts
2. Deposit money
3. Withdraw money
4. Transfer funds
5. Check balance
6. View transaction history
7. Check overdraft balance (checking accounts)

---

## ▶️ How to Run

Ensure Python is installed, then run:

```bash 
python main.py
```




## 📜 License

This project is licensed under the MIT License.
You are free to use, modify, and distribute this project for learning purposes.

 ## ⚠️ Disclaimer

This project is a learning and demonstration project only.
It does not represent a real banking system and should not be used for
financial, commercial, or production purposes.

