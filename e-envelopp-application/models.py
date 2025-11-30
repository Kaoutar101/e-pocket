from pydantic import BaseModel
from typing import List, Optional

# Account model
class Account(BaseModel):
    account_id: str
    balance: float

# Payment (wallet-to-wallet or wallet-to-merchant)
class PaymentRequest(BaseModel):
    from_wallet: str
    to_wallet: str
    amount: float

class MerchantPaymentRequest(BaseModel):
    envelope_id: str
    merchant_id: str
    amount: float

# Withdraw / Deposit
class CashRequest(BaseModel):
    account_id: str
    amount: float

# Bank transfer
class TransferRequest(BaseModel):
    from_account: str
    to_iban: str
    amount: float

# Account creation
class AccountCreationRequest(BaseModel):
    user_id: str
    initial_deposit: float
