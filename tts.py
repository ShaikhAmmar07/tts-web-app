import subprocess
import os
import shutil

PIPER_MODEL = "models/en-us.onnx"
PIPER_BIN = shutil.which("piper") or "./piper_bin"

def generate_audio(text: str, output_path: str, speed: float = 1.0):
    """Generate audio using Piper TTS with specified speed."""
    length_scale = 1.0 / speed
    
    cmd = [
        PIPER_BIN,
        "--model", PIPER_MODEL,
        "--output_file", output_path,
        "--length_scale", str(length_scale)
    ]
    
    process = subprocess.Popen(
        cmd,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    
    stdout, stderr = process.communicate(input=text)
    
    if process.returncode != 0:
        raise RuntimeError(f"Piper TTS failed: {stderr}")
    
    if not os.path.exists(output_path):
        raise RuntimeError("Audio file was not generated")
