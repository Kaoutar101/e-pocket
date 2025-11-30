from fastapi import APIRouter
from models import AccountCreationRequest, Account

router = APIRouter()

# Simple in-memory DB
ACCOUNTS = {}

@router.post("/open-account")
def open_account(data: AccountCreationRequest):
    """
    Open or activate a new bank account.
    """
    if data.user_id in ACCOUNTS:
        return {"msg": "Account already exists"}

    ACCOUNTS[data.user_id] = Account(account_id=data.user_id, balance=data.initial_deposit)
    return {"msg": "Account created", "account": ACCOUNTS[data.user_id]}
