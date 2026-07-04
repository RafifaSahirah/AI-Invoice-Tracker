"""Google Sheets service for persisting invoice data"""

import gspread
from google.oauth2.service_account import Credentials
import os

scopes = ['https://www.googleapis.com/auth/spreadsheets',
          'https://www.googleapis.com/auth/drive']

credentials_path = os.path.join(os.path.dirname(__file__), '..', '..', 'config', 'credentials.json')
credentials = Credentials.from_service_account_file(
    credentials_path,
    scopes=scopes
)

gc = gspread.authorize(credentials)

sh = gc.open("Pembukuan Otomatis")
worksheet = sh.sheet1

# Function to save data into the spreadsheet
def save_invoice(invoice_request):
    new_row = [
      invoice_request.date,
      invoice_request.name,
      invoice_request.nominal
    ]
    worksheet.append_row(new_row)