from fastapi import APIRouter
from models import Account

router = APIRouter()

from api_open_account import ACCOUNTS

@router.get("/balance/{account_id}")
def get_balance(account_id: str):
    """
    Check account balance
    """
    account = ACCOUNTS.get(account_id)
    if not account:
        return {"error": "Account not found"}
    return {"account_id": account.account_id, "balance": account.balance}
