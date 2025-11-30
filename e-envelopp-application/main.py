# Import the FastAPI framework to create the main application
from fastapi import FastAPI

# Import each API router from its file and give it a short alias
# These routers contain the endpoints for each banking feature.
from api_open_account import router as open_router          # Open/Activate Account API
from api_check_balance import router as balance_router      # Check Balance API
from api_payments import router as payments_router          # Wallet-to-wallet & merchant payments API
from api_cash import router as cash_router                  # Deposit/Withdraw API
from api_transfers import router as transfers_router        # Bank Transfers API

# Create the main FastAPI application

app = FastAPI(title="E-Envelope Banking App API")

# Attach (mount) all the API routers to the main app

# Routes for opening/activating accounts
app.include_router(open_router, prefix="/api")

# Routes for checking account balance
app.include_router(balance_router, prefix="/api")

# Routes for sending/receiving payments (wallet-to-wallet, wallet-to-merchant)
app.include_router(payments_router, prefix="/api")

# Routes for withdrawing or depositing cash
app.include_router(cash_router, prefix="/api")

# Routes for simulating or processing bank transfers
app.include_router(transfers_router, prefix="/api")
