'use client'

import { useState } from 'react'
import { generateSpeech } from '@/lib/api'

export default function TTSForm() {
  const [text, setText] = useState('')
  const [duration, setDuration] = useState<30 | 60>(30)
  const [loading, setLoading] = useState(false)
  const [audioUrl, setAudioUrl] = useState<string | null>(null)
  const [error, setError] = useState<string | null>(null)

  const handleGenerate = async () => {
    if (!text.trim()) {
      setError('Please enter some text')
      return
    }

    setLoading(true)
    setError(null)
    setAudioUrl(null)

    try {
      const blob = await generateSpeech(text, duration)
      const url = URL.createObjectURL(blob)
      setAudioUrl(url)
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Failed to generate speech')
    } finally {
      setLoading(false)
    }
  }

  const handleDownload = () => {
    if (!audioUrl) return
    const a = document.createElement('a')
    a.href = audioUrl
    a.download = 'speech.wav'
    a.click()
  }

  return (
    <div className="w-full max-w-2xl mx-auto space-y-6">
      <textarea
        value={text}
        onChange={(e) => setText(e.target.value)}
        placeholder="Enter your script here..."
        className="w-full h-48 p-4 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent resize-none"
        disabled={loading}
      />

      <div className="flex items-center gap-4">
        <label className="font-medium text-gray-700">Duration:</label>
        <button
          onClick={() => setDuration(30)}
          className={`px-6 py-2 rounded-lg font-medium transition ${
            duration === 30
              ? 'bg-blue-600 text-white'
              : 'bg-gray-200 text-gray-700 hover:bg-gray-300'
          }`}
          disabled={loading}
        >
          30s
        </button>
        <button
          onClick={() => setDuration(60)}
          className={`px-6 py-2 rounded-lg font-medium transition ${
            duration === 60
              ? 'bg-blue-600 text-white'
              : 'bg-gray-200 text-gray-700 hover:bg-gray-300'
          }`}
          disabled={loading}
        >
          60s
        </button>
      </div>

      <button
        onClick={handleGenerate}
        disabled={loading}
        className="w-full py-3 bg-blue-600 text-white rounded-lg font-medium hover:bg-blue-700 disabled:bg-gray-400 disabled:cursor-not-allowed transition"
      >
        {loading ? 'Generating...' : 'Generate Speech'}
      </button>

      {error && (
        <div className="p-4 bg-red-50 border border-red-200 rounded-lg text-red-700">
          {error}
        </div>
      )}

      {audioUrl && (
        <div className="space-y-4 p-6 bg-white border border-gray-200 rounded-lg">
          <audio controls className="w-full" src={audioUrl} />
          <button
            onClick={handleDownload}
            className="w-full py-2 bg-green-600 text-white rounded-lg font-medium hover:bg-green-700 transition"
          >
            Download Audio
          </button>
        </div>
      )}
    </div>
  )
}
