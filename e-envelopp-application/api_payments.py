from fastapi import APIRouter
from models import PaymentRequest, MerchantPaymentRequest

router = APIRouter()

# Simple wallets DB
WALLETS = {
    "main": 5000,
    "groceries": 0,
    "savings": 0
}

@router.post("/wallet-transfer")
def wallet_transfer(data: PaymentRequest):
    """
    Send/Receive Payments (wallet-to-wallet)
    """
    if WALLETS.get(data.from_wallet, 0) < data.amount:
        return {"error": "Insufficient balance"}
    WALLETS[data.from_wallet] -= data.amount
    WALLETS[data.to_wallet] = WALLETS.get(data.to_wallet, 0) + data.amount
    return {"msg": "Transfer successful", "wallets": WALLETS}

@router.post("/merchant-payment")
def merchant_payment(data: MerchantPaymentRequest):
    """
    Send/Receive Payments (wallet-to-merchant)
    """
    if WALLETS.get(data.envelope_id, 0) < data.amount:
        return {"error": "Insufficient envelope balance"}
    WALLETS[data.envelope_id] -= data.amount
    return {
        "msg": "Payment successful",
        "merchant_id": data.merchant_id,
        "remaining_balance": WALLETS[data.envelope_id]
    }
