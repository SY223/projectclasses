# 🏦 Banking System in Python

This project simulates a simple banking system that supports **Savings** and **Current** accounts.  
It demonstrates object-oriented programming concepts in Python and emphasises **clear documentation** practices.

---

## ✨ Features
- Create accounts with unique account numbers (max 10 digits).
- Deposit and withdraw funds safely.
- Retrieve account details including balance and account type.
- Specialised account types:
  - **Savings Account** → earns quarterly interest.
  - **Current Account** → allows overdraft facility.

---

## 📂 Project Structure

---

## 🚀 Usage

### Example: Creating a Savings Account
```python
from projects import SavingsAccount

# Create a new savings account
customer = SavingsAccount(1297784537, "Savings", 300200.89, "Bailey Gumfrost")

# Access account details
print(customer.get_account_details())
