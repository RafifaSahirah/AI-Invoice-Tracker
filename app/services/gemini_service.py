"""Gemini service: extracts invoice data from image/PDF using Gemini model."""

import json
import os

from dotenv import load_dotenv
from fastapi import UploadFile
import google.genai as genai
from google.genai import types
from google.genai.types import Part

from app.schemas.invoice_request import InvoiceRequest

load_dotenv()
gemini_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=gemini_key)

async def extract_invoice(file: UploadFile) -> InvoiceRequest:
    file_content = await file.read()

    image_part = Part.from_bytes(
        data=file_content,
        mime_type=file.content_type
    )

    prompt = """
    Extract the following information from this invoice image:
    - date
    - name
    - nominal

    If a field cannot be found:
    - Use an empty string for date and name.
    - Use iso format for date (YYYY-MM-DD).
    - Use 0 for nominal.
    
    Do not return a list. Return exactly one object matching the requested schema.
    """
    
    response = client.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents=[prompt, image_part],
        config=types.GenerateContentConfig(
            response_mime_type="application/json"
        )
    )

    print(repr(response.text))

    # Extract the JSON string to dict
    data = json.loads(response.text)
    invoice_request = InvoiceRequest(**data)

    return invoice_request