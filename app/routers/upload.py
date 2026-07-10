from fastapi import APIRouter, UploadFile, File, HTTPException
import shutil

router = APIRouter(
    prefix = "/upload",
    tags = ["Upload"]
)


@router.post("/")
async def upload_file(
    file:UploadFile = File(...)
):
    allowed_types = [
        "application/pdf",
        "image/jpeg",
        "image/png"
    ]

    if file.content_type not in allowed_types:
        raise HTTPException(status_code=400,detail="only pdf , jpeg, png are allowed")
    
    file_path = f"uploads/{file.filename}"

    with open(file_path,"wb") as buffer:
        shutil.copyfileobj(file.file,buffer)

    return {
        "filename":file.filename,
        "content_type":file.content_type,
        "file_path":file_path
    }