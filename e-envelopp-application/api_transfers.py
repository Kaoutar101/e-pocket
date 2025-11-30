from fastapi import APIRouter
from models import TransferRequest

router = APIRouter()

@router.post("/simulate-transfer")
def simulate_transfer(data: TransferRequest):
    """
    Simulate a bank transfer before executing
    """
    return {
        "msg": "Simulation successful",
        "from_account": data.from_account,
        "to_iban": data.to_iban,
        "estimated_time": "24 hours"
    }

@router.post("/process-transfer")
def process_transfer(data: TransferRequest):
    """
    Process an actual bank transfer
    """
    return {
        "msg": "Transfer completed",
        "from_account": data.from_account,
        "to_iban": data.to_iban,
        "amount": data.amount
    }
