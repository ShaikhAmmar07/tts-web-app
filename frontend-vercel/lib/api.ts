const API_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000'

export async function generateSpeech(text: string, targetDuration: number): Promise<Blob> {
  const response = await fetch(`${API_URL}/generate`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      text,
      target_duration: targetDuration,
    }),
  })

  if (!response.ok) {
    const error = await response.json()
    throw new Error(error.detail || 'Failed to generate speech')
  }

  return response.blob()
}
