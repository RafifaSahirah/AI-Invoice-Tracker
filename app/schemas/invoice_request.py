"""Schema for invoice creation requests"""

from pydantic import BaseModel

class InvoiceRequest(BaseModel):
  date: str
  name: str
  amount: int