"""Main application file for the AI Invoice Tracker API.

This module provides the FastAPI entry points for uploading invoices,
extracting data using AI, and saving the results to Google Sheets.
"""

from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from app.services.google_sheet_service import save_invoice
from app.services.gemini_service import extract_invoice
from app.schemas.invoice_record import InvoiceRecord
from app.services.storage_service import upload_file
import os

app = FastAPI()

origins = [
    "http://127.0.0.1:5500"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# Endpoint
@app.get("/")
def read_root():
    return {"message": "API is running"}

@app.post("/invoice/process")
async def process_invoice(file: UploadFile = File(...)):
    storage_file = await upload_file(file)

    invoice = await extract_invoice(file)

    invoice_record = InvoiceRecord(
        date=invoice.date,
        reference_number=invoice.reference_number,
        name=invoice.name,
        amount=invoice.amount,
        invoice_url=storage_file.url
    )
    
    save_invoice(invoice_record)

    return {
        "message": "Invoice extracted and saved successfully",
        "invoice": invoice_record
    }