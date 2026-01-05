from typing import Tuple
from duration import estimate_duration, get_audio_duration
from tts import generate_audio
import os

def generate_with_duration_lock(
    text: str,
    target_duration: float,
    output_path: str,
    max_attempts: int = 5,
    tolerance: float = 0.5
) -> Tuple[bool, float, int]:
    """
    Generate audio with target duration using adaptive speed adjustment.
    
    Returns:
        (success, actual_duration, attempts_used)
    """
    speed = 1.0
    
    for attempt in range(max_attempts):
        generate_audio(text, output_path, speed)
        
        actual_duration = get_audio_duration(output_path)
        diff = actual_duration - target_duration
        
        if abs(diff) <= tolerance:
            return True, actual_duration, attempt + 1
        
        speed_adjustment = actual_duration / target_duration
        speed *= speed_adjustment
        
        speed = max(0.5, min(2.0, speed))
    
    return False, actual_duration, max_attempts
