from fastapi import APIRouter
from models import CashRequest
from api_open_account import ACCOUNTS

router = APIRouter()

@router.post("/deposit")
def deposit_cash(data: CashRequest):
    """
    Deposit cash into account
    """
    account = ACCOUNTS.get(data.account_id)
    if not account:
        return {"error": "Account not found"}
    account.balance += data.amount
    return {"msg": "Deposit successful", "new_balance": account.balance}

@router.post("/withdraw")
def withdraw_cash(data: CashRequest):
    """
    Withdraw cash from account
    """
    account = ACCOUNTS.get(data.account_id)
    if not account:
        return {"error": "Account not found"}
    if account.balance < data.amount:
        return {"error": "Insufficient balance"}
    account.balance -= data.amount
    return {"msg": "Withdrawal successful", "new_balance": account.balance}
