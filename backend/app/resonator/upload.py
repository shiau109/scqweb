from fastapi import UploadFile, File, Depends, HTTPException
from app.services.upload import save_upload_file
from app.resonator.parser import parse_resonator_file
import os
from app.services.user import get_current_user


async def upload_resonator_file(
    files: list[UploadFile] = File(...),
    user: str = Depends(get_current_user)
):
    for file in files:
        path = save_upload_file(file, feature="resonator", user=user)
        try:
            data = parse_resonator_file(path)
        except Exception as e:
            os.remove(path)  # delete invalid file
            raise HTTPException(status_code=400, detail=str(e))#detail="Invalid file format")

