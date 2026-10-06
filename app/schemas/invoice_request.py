"""Schema for invoice creation requests"""

from pydantic import BaseModel

class InvoiceRequest(BaseModel):
    date: str
    reference_number: str
    name: str
    amount: int