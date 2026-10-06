from pydantic import BaseModel

class InvoiceRecord(BaseModel):
    date: str
    reference_number: str
    name: str
    amount: int
    invoice_url: str