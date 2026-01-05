# Frontend Deployment (Vercel)

## Setup

1. Install dependencies:
   ```
   npm install
   ```

2. Create `.env.local`:
   ```
   NEXT_PUBLIC_API_URL=http://localhost:8000
   ```

3. Run locally:
   ```
   npm run dev
   ```

## Vercel Deployment

1. Import project to Vercel
2. Add environment variable:
   - Key: `NEXT_PUBLIC_API_URL`
   - Value: Your Render backend URL
3. Deploy
