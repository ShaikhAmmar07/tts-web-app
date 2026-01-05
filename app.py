from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os
import uuid
from duration_lock import generate_with_duration_lock

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class TTSRequest(BaseModel):
    text: str
    target_duration: float

@app.post("/generate")
async def generate_tts(request: TTSRequest):
    if not request.text.strip():
        raise HTTPException(status_code=400, detail="Text cannot be empty")
    
    if request.target_duration not in [30, 60]:
        raise HTTPException(status_code=400, detail="Duration must be 30 or 60 seconds")
    
    filename = f"{uuid.uuid4()}.wav"
    output_path = os.path.join("temp_audio", filename)
    
    try:
        success, actual_duration, attempts = generate_with_duration_lock(
            request.text,
            request.target_duration,
            output_path
        )
        
        if not success:
            raise HTTPException(
                status_code=500,
                detail=f"Could not match target duration after {attempts} attempts"
            )
        
        return FileResponse(
            output_path,
            media_type="audio/wav",
            filename="speech.wav",
            background=cleanup_file(output_path)
        )
    
    except Exception as e:
        if os.path.exists(output_path):
            os.remove(output_path)
        raise HTTPException(status_code=500, detail=str(e))

def cleanup_file(filepath: str):
    """Background task to clean up temp file after response."""
    import asyncio
    async def remove():
        await asyncio.sleep(1)
        if os.path.exists(filepath):
            os.remove(filepath)
    return remove

@app.get("/health")
async def health():
    return {"status": "ok"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
