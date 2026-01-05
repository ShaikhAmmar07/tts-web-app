import TTSForm from '@/components/TTSForm'

export default function Home() {
  return (
    <main className="min-h-screen py-12 px-4">
      <div className="max-w-4xl mx-auto">
        <h1 className="text-4xl font-bold text-center text-gray-900 mb-2">
          Text-to-Speech Generator
        </h1>
        <p className="text-center text-gray-600 mb-12">
          Generate speech with precise duration control
        </p>
        <TTSForm />
      </div>
    </main>
  )
}
