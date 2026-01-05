import subprocess
import wave
import os

def get_audio_duration(filepath: str) -> float:
    """Get duration of WAV file in seconds."""
    with wave.open(filepath, 'rb') as audio:
        frames = audio.getnframes()
        rate = audio.getframerate()
        return frames / float(rate)

def estimate_duration(text: str, speed: float = 1.0) -> float:
    """Estimate speech duration based on text length and speed."""
    words = len(text.split())
    base_wpm = 150
    adjusted_wpm = base_wpm * speed
    return (words / adjusted_wpm) * 60
