from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def list_files():
    return {"message": "List all files"}

@router.post("/")
async def upload_file():
    return {"message": "Upload a file"}

@router.get("/{id}")
async def get_file(id: int):
    return {"message": f"Get file with ID {id}"}

@router.post("/{id}")
async def update_file(id: int):
    return {"message": f"Update file with ID {id}"}

@router.delete("/{id}")
async def delete_file(id: int):
    return {"message": f"Delete file with ID {id}"}

@router.post("/merge")
async def merge_files():
    return {"message": "Merge files"}
