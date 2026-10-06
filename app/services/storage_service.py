from supabase import Client, create_client
import os
from dotenv import load_dotenv
from fastapi import UploadFile
from app.schemas.uploaded_file import UploadedFile

from datetime import datetime
import uuid

BUCKET_NAME = os.getenv("SUPABASE_BUCKET_NAME")

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

supabase: Client = create_client(
    SUPABASE_URL,
    SUPABASE_KEY
)

async def upload_file(file: UploadFile) -> UploadedFile:
    today = datetime.now()
    file_id = str(uuid.uuid4())
    _, extension = os.path.splitext(file.filename)

    path = (
        f"{today:%Y/%m/%d}/{file_id}{extension}"
    )

    file_content = await file.read()
    file.file.seek(0)

    supabase.storage.from_(BUCKET_NAME).upload(
        path=path,
        file=file_content,
        file_options={
            "content-type": file.content_type
        }
    )
    url = supabase.storage.from_(BUCKET_NAME).get_public_url(path)

    return UploadedFile(
        path=path,
        url=url
    )
