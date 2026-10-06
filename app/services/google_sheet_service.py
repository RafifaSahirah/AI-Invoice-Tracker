"""Google Sheets service for persisting invoice data"""

import gspread
from config.google_config import credentials

gc = gspread.authorize(credentials)

sh = gc.open("Pembukuan Otomatis")
worksheet = sh.sheet1

# Function to save data into the spreadsheet
def save_invoice(invoice_request):
    image_link = f'=HYPERLINK("{invoice_request.invoice_url}"; "Image Link")'
    new_row = [
        invoice_request.date,
        invoice_request.reference_number,
        invoice_request.name,
        invoice_request.amount,
        image_link
    ]
    worksheet.append_row(
        new_row,
        value_input_option="USER_ENTERED"
    )