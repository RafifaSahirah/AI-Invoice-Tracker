from google.oauth2.service_account import Credentials
import os

scopes = ['https://www.googleapis.com/auth/spreadsheets',
          'https://www.googleapis.com/auth/drive']

credentials_path = os.path.join(os.path.dirname(__file__), 'credentials.json')
credentials = Credentials.from_service_account_file(
    credentials_path,
    scopes=scopes
)