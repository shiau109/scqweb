

# services/upload.py
import os
from fastapi import UploadFile


def save_upload_file(file: UploadFile, feature: str, user: str) -> str:
    save_dir = os.path.join("uploads", user, feature)
    os.makedirs(save_dir, exist_ok=True)

    file_path = os.path.join(save_dir, file.filename)

    with open(file_path, "wb") as f:
        f.write(file.file.read())

    return file_path
